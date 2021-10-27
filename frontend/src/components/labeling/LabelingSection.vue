<template>
  <div class="labeling-container">
    <LabelingStats />
    <LabelingQuestion
      v-if="isQuestionPresent"
      :question="question"
    >
    </LabelingQuestion>
  </div>
</template>

<style scoped>

.labeling-container {
  max-width: 1276px;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

</style>

<script>
import { mapGetters } from 'vuex'
import LabelingQuestion from "./LabelingQuestion"
import LabelingStats from "./LabelingStats"

export default {
  name: "LabelingSection",
  components: {
    LabelingQuestion,
    LabelingStats,
  },
  data: () => ({}),
  mounted() {
    this.$store.dispatch("loadQuestion")
  },
  computed: {
    ...mapGetters(["question"]),
    isQuestionPresent() {
      return this.$store.getters.question !== undefined
    },
  },
};
</script>
