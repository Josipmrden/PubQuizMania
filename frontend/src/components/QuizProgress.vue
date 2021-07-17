<template>
  <div class="progress-container">
    <v-progress-linear
      class="progress-bar"
      :color="correctnessGradientHex"
      height="25"
      :value="correctness"
      striped
      ><span v-bind:class="{ 'black-text': correctnessFontColor === 'black' }"
        >Postotak riješenosti - {{ correctness }}%</span
      ></v-progress-linear
    >
    <v-progress-linear
      class="progress-bar"
      color="light-blue"
      height="25"
      :value="completeness"
      striped
      ><span
        >Odgovoreno pitanja: {{ progress.questionsCompleted }}/{{noQuestions}}</span
      ></v-progress-linear
    >
  </div>
</template>


<style scoped>
.progress-container {
  right: 20px;
  left: 20px;
}

.progress-bar {
  margin-bottom: 10px;
  margin-top: 10px;
}
.white-text {
  color: white;
}
.black-text {
  color: black;
}
</style>


<script>
import { mapGetters } from "vuex";
export default {
  name: "QuizProgress",
  computed: {
    ...mapGetters([
      "completeness",
      "correctness",
      "correctnessGradientHex",
      "correctnessFontColor",
      "progress",
      "noQuestions"
    ]),
  },
  methods: {
    progressBarCompletenessTextColor() {
      return "black-text";
    },
  },
};
</script>

