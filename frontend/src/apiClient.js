import Vue from 'vue'

export const API_URL = 'http://localhost:8000'

export const apiClient = {
    getCategories: () => {
        return Vue.axios.get(`${API_URL}/categories/`)
    },
    getUnlabeledQuestion: () => {
        return Vue.axios.get(`${API_URL}/unlabeled/`)
    },
    getLabelingStats: () => {
        return Vue.axios.get(`${API_URL}/label/stats/`)
    },
    getUnlabeledQuestionExcluding: (excludingQuestion) => {
        return Vue.axios.get(`${API_URL}/unlabeled/?excluded_questions=${excludingQuestion}`)
    },
    postLabeledQuestion: (data) => {
        return Vue.axios.post(`${API_URL}/label/`, data)
    },
    getQuiz: (data) => {
        var categoriesQS = data.categories.join(",")
        return Vue.axios.get(`${API_URL}/random_quiz/?no_questions=${data.noQuestions}&categories=${categoriesQS}`, data)
    },
    answerQuestion: (data) => {
        return Vue.axios.post(`${API_URL}/answer_question/`, data)
    }
}
