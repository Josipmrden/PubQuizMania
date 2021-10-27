<template>
  <div class="mb-5">
    <div v-if="numberTotalQuestions() !== undefined">
      <h2 class="stats">
        Labelirano: {{ numberLabeledQuestions() }} /
        {{ numberTotalQuestions() }} ({{ labelingPercentage() }}%)
      </h2>
      <v-progress-linear stream :buffer-value="progressValue" color="cyan">
      </v-progress-linear>
    </div>
    <div v-else>
      <h2>Učitavanje...</h2>
      <v-progress-linear indeterminate color="cyan"> </v-progress-linear>
    </div>
  </div>
</template>

<style scoped>
.stats {
  color: var(--v-blue-base);
}
</style>

<script>
import { mapGetters } from "vuex";

export default {
  name: "LabelingStats",
  methods: {
    ...mapGetters([
      "numberLabeledQuestions",
      "numberTotalQuestions",
      "labelingPercentage",
    ]),
  },
  computed: {
    progressValue() {
      return this.labelingPercentage() * 100;
    },
  },
};
</script>
