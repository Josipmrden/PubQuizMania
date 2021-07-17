<template>
  <div>
    <div class="container">
      <div class="question-section-form">
        <div class="form">
          <v-select
            :items="categoryNames"
            multiple
            v-model="selectedCategories"
            label="Izaberite kategorije"
            hint="Ostavite prazno za sve kategorije"
            persistent-hint
          ></v-select>
          <v-slider
            class="no-questions-slider"
            v-model="noQuestions"
            color="primary"
            label="Broj pitanja"
            min="1"
            max="100"
            thumb-label
          ></v-slider>
        </div>
        <div class="submit-container">
          <v-btn @click="playQuiz">IGRAJ KVIZ</v-btn>
        </div>
      </div>

      <div>
        <transition name="fade">
          <QuizProgress v-if="quizStarted && progress.questionsCompleted" />
        </transition>

        <transition name="fade">
          <div
            v-if="quizStarted"
            class="quiz-questions-container scroll-bar"
            :key="quizQuestionsKey"
          >
            <QuizQuestion
              v-for="(question, idx) in quiz"
              :key="idx"
              :question="question"
            />
          </div>
        </transition>
      </div>
    </div>

    <transition name="fade">
      <div v-if="isQuizFinished()">
      <div class="quiz-ended-message-container"></div>
        <v-card class="quiz-ended-card">
          <h1>Kviz uspješno završen!</h1>
          <h3>
            Točnost: {{ progress.questionsCorrect }}/{{
              progress.questionsCompleted
            }}
          </h3>
          <v-btn class="playAgainButton" block @click="playAgain">PLAY AGAIN</v-btn>
        </v-card>
      </div>
    </transition>
  </div>
</template>

<style scoped>
.container {
  max-width: 876px;
  padding: 20px;
  margin-top: 10px;
}
.form {
  display: flex;
  vertical-align: middle;
  position: relative;
}
.no-questions-slider {
  position: relative;
  top: 20px;
  margin-left: 20px;
}
.submit-container {
  display: flex;
  justify-content: flex-end;
  flex-flow: row nowrap;
}
.quiz-questions-container {
  width: 100%;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  margin-top: 20px;
  max-height: 700px;
  overflow: auto;
}
.question-section-form {
  padding: 15px;
  border-radius: 10px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.scroll-bar::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  background-color: #f5f5f5;
}

.scroll-bar::-webkit-scrollbar {
  width: 5px;
  background-color: #f5f5f5;
}

.scroll-bar::-webkit-scrollbar-thumb {
  background-color: #0ae;
  background-image: -webkit-linear-gradient(
    45deg,
    rgba(255, 255, 255, 0.2) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.2) 75%,
    transparent 75%,
    transparent
  );
}

.quiz-ended-message-container {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background-color: #000;
  z-index: 1;
  opacity: 0.5;
}

.quiz-ended-card {
  position: absolute;
  padding: 20px;
  max-width: 876px;
  max-height: 500px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
}

.playAgainButton {
  margin-top: 20px;
}
</style>

<script>
import { mapGetters } from "vuex";
import QuizQuestion from "./QuizQuestion";
import QuizProgress from "./QuizProgress";

export default {
  name: "QuizSection",
  components: { QuizQuestion, QuizProgress },
  data() {
    return {
      quizQuestionsKey: 0,
      noQuestions: 10,
      selectedCategories: undefined,
      quizStarted: false,
    };
  },
  mounted() {
    if (this.categoryNames === undefined || this.categoryNames.length === 0) {
      this.$store.dispatch("getCategories");
    }
  },
  computed: {
    ...mapGetters(["categoryNames", "categories", "quiz", "progress"]),
  },
  methods: {
    async playQuiz() {
      var payload = {
        categories: this.getSelectedCategoriesAbbrev(),
        noQuestions: this.noQuestions,
      };

      await this.$store.dispatch("getQuiz", payload);
      this.quizStarted = true;
      this.renderQuestions();
    },
    isQuizFinished() {
      return (
        this.quizStarted === true &&
        this.progress.questionsCompleted === this.quiz.length &&
        this.quiz.length !== 0
      );
    },
    playAgain() {
      this.$store.dispatch("resetQuiz").then(() => {
        this.quizStarted = false        
      })
    },
    renderQuestions() {
      this.quizQuestionsKey += 1;
    },
    getSelectedCategoriesAbbrev() {
      var categoryAbbreviations = [];
      if (this.selectedCategories === undefined) {
        return categoryAbbreviations;
      }
      for (var i = 0; i < this.selectedCategories.length; i++) {
        var selectedCategory = this.selectedCategories[i];
        var categoryAbbrev = this.categories.find(
          (category) => category.name === selectedCategory
        ).abbrev;
        categoryAbbreviations.push(categoryAbbrev);
      }

      return categoryAbbreviations;
    },
  },
};
</script>
