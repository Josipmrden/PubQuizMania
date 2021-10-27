<template>
  <div
    class="quiz-question"
    v-bind:class="{
      'false-answer': answeredFalsely,
      'correct-answer': answeredCorrectly,
    }"
  >
    <div class="front">
      <p class="question-text">
        <span class="question-number"> {{ question.number }}.</span>
        {{ question.question }}
      </p>
      <div class="answer-section">
        <v-text-field
          :disabled="answeredCorrectly || answeredFalsely"
          class="answer-field"
          v-model="answer"
        ></v-text-field>
        <transition name="fade">
          <strong v-if="!!question.trueAnswer">{{
            question.trueAnswer
          }}</strong>
        </transition>
        <v-btn
          :disabled="question.answered === true"
          color="#eee"
          @click="answerQuestion"
        >
          <v-icon color="#444">mdi-glass-mug-variant</v-icon>
        </v-btn>
      </div>
    </div>
  </div>
</template>

<style scoped>
.quiz-question {
  position: relative;
  border-radius: 15px;
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  padding: 15px;
  margin: 15px 15px;
  transition: 0.15s;
}

.quiz-question:hover {
  --translate-y: -2px;
  box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.5);
}

.question-text {
  font-weight: 300;
  font-size: 18px;
}
.question-number {
  font-size: 20px;
}
.answer-section {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}
.answer-field {
  max-width: 500px;
}
.false-answer {
  background-color: #fa8072;
}
.correct-answer {
  background-color: #50c878;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>

<script>
export default {
  name: "QuizQuestion",
  components: {},
  props: ["question"],
  data() {
    return {
      answeredCorrectly: false,
      answeredFalsely: false,
      answer: "",
    };
  },

  methods: {
    forceRerender() {
      this.btnAnsweredKey += 1;
    },
    async answerQuestion() {
      var payload = {
        questionNumber: this.question.number,
        answer: this.answer,
      };
      await this.$store.dispatch("answerQuestion", payload);
      this.answeredCorrectly = this.question.isCorrect;
      this.answeredFalsely = !this.question.isCorrect;
    },
  },
};
</script>
