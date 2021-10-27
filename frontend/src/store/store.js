import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { MUTATION_CONSTANTS } from './mutationConstants'
import { apiClient } from '../apiClient'

Vue.use(VueAxios, axios)
Vue.use(Vuex)

const state = {
    categories: [],
    question: {},
    stats: {},
    quiz: {},
    progress: {
        questionsCompleted: 0,
        questionsCorrect: 0
    }
}

const initializeEmptyCategories = (question) => {
    store.getters.categories.forEach((category) => {
        question.categories = [...question.categories, {
            'name': category.name,
            'abbrev': category.abbrev,
            'active': false,
        }]
    })
    question.categories = question.categories.sort(function(a, b) {return a.name > b.name ? 1 : -1})
}

const mutations = {
    PUSH_QUESTION(state, question) {
        state.question = question
        initializeEmptyCategories(question)
    },

    ADD_CATEGORIES(state, categories) {
        state.categories = categories
    },
    ADD_STATS(state, payload) {
        Vue.set(state.stats, 'noLabeledQuestions', payload.labeled_questions)
        Vue.set(state.stats, 'noTotalQuestions', payload.total_questions)
    },

    INCREMENT_STATS(state) {
        state.stats.noLabeledQuestions += 1
    },

    SET_QUIZ(state, quiz) {
        state.quiz = quiz
        state.quiz.forEach((question) => {
            Vue.set(question, 'answered', false)
        })
    },
    RESET_PROGRESS(state) {
        state.progress.questionsCompleted = 0;
        state.progress.questionsCorrect = 0;
    },
    UPDATE_QUIZ_PROGRESS(state, payload) {
       var  { questionNumber, isCorrect, trueAnswer } = payload
        state.progress.questionsCompleted += 1
        if (isCorrect) {
            state.progress.questionsCorrect += 1
        }

        var question = state.quiz.find(question => question.number === questionNumber)
        question.answered = true
        question.trueAnswer = trueAnswer
        question.isCorrect = isCorrect
    },
    RESET_QUIZ(state) {
        state.quiz = {}
        state.progress.questionsCompleted = 0
        state.progress.questionsCorrect = 0
    },
}

const actions = {
    async loadQuestion({dispatch, commit }) {
        await dispatch("getCategories")
        apiClient.getUnlabeledQuestion()
            .then((resp) =>  {
                commit(MUTATION_CONSTANTS.PUSH_QUESTION, resp.data.unlabeled_questions[0])
        })

        apiClient.getLabelingStats()
            .then((resp) => {
                commit(MUTATION_CONSTANTS.ADD_STATS, resp.data)
        })
    },
    async getCategories(context) {
        await apiClient.getCategories()
            .then((resp) => {
                context.commit(MUTATION_CONSTANTS.ADD_CATEGORIES, resp.data.categories)
            })
    },
    async acceptLabeledQuestion({ dispatch, commit }, question) {
        return dispatch("labelQuestion", question).then(() => {
            commit(MUTATION_CONSTANTS.INCREMENT_STATS)
            return dispatch("getAnotherQuestion", question)
        })
        .catch(err => {
            throw err
        })
    },
    labelQuestion(context, question) {
        var categoryAbbreviations = question.categories
            .filter(c => c.active === true)
            .map((c) => c.abbrev)

        const data = {
            'question_number': question.number,
            'question': question.question,
            'answer': question.answer,
            'categories': categoryAbbreviations
        }

        return apiClient.postLabeledQuestion(data)
    },
    getAnotherQuestion(context, question) {
        var excludedQuestion = question.number
        apiClient.getUnlabeledQuestionExcluding(excludedQuestion)
          .then((resp) => {
            context.commit(MUTATION_CONSTANTS.PUSH_QUESTION, resp.data.unlabeled_questions[0])
        })
    },
    getQuiz: (context, payload) => {
        apiClient.getQuiz(payload)
            .then((resp) => {
                context.commit(MUTATION_CONSTANTS.SET_QUIZ, resp.data.questions)
                context.commit(MUTATION_CONSTANTS.RESET_PROGRESS)
            })
    },
    answerQuestion: (context, payload) => {
        return apiClient.answerQuestion(payload)
            .then((resp) => {
                context.commit(MUTATION_CONSTANTS.UPDATE_QUIZ_PROGRESS, resp.data)
            })
    },
    resetQuiz: (context) => {
        context.commit(MUTATION_CONSTANTS.RESET_QUIZ);
    }
}

const getters = {
    categories: state => state.categories,
    question: state => state.question,
    categoryNames: state => state.categories.map(category => category.name),
    numberLabeledQuestions: (state) => state.stats.noLabeledQuestions,
    numberTotalQuestions: (state) => state.stats.noTotalQuestions,
    labelingPercentage: (state) => (state.stats.noLabeledQuestions / state.stats.noTotalQuestions).toFixed(2),
    quiz: (state) => state.quiz,
    noQuestions: (state) => state.quiz.length,
    progress: (state) => state.progress,
    correctness: (state) => {
        return (state.progress.questionsCorrect / state.progress.questionsCompleted).toFixed(4) * 100
    },
    completeness: (state) => {
        return (state.progress.questionsCompleted / state.quiz.length).toFixed(4) * 100        
    },
    correctnessGradient: (state, getters) => {
        const correctness = getters.correctness

        var r, g, b = 0;
        if(correctness < 50) {
            r = 255;
            g = Math.round(5.1 * correctness);
        }
        else {
            g = 255;
            r = Math.round(510 - 5.10 * correctness);
        }
        return {
            'r': r,
            'g': g,
            'b': b
        }
    },
    correctnessGradientHex: (state, getters) => {
        const { r, g, b } = getters.correctnessGradient
        var h = r * 0x10000 + g * 0x100 + b * 0x1;
        return '#' + ('000000' + h.toString(16)).slice(-6);
    },
    correctnessFontColor: (state, getters) => {
        var progress = getters.correctness
        console.log(progress)

        if (progress > 40) {
            return "black"
        }

        return "white"
    }
}

export const store = new Vuex.Store({
    state,
    mutations,
    actions,
    getters,
})