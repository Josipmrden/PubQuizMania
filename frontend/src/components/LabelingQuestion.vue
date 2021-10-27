<template>
  <div>
    <v-card rounded>
      <div class="card-container">
        <div class="title-section">
          <div class="question-title-holder">
            <v-img
              alt="PQM Logo"
              class="shrink mr-2"
              src="@/assets/toast.png"
            />
            <h1 class="title-question">Pitanje #{{ question.number }}</h1>
            <v-img
              alt="PQM Logo"
              class="shrink mr-2"
              src="@/assets/toast.png"
            />
          </div>
        </div>

        <v-text-field
          class="text-field-question"
          v-model="question.question"
        ></v-text-field>
        <v-text-field v-model="question.answer"></v-text-field>
        <CategorySection :questionCategories="question.categories" />
        <div class="accept-question-section">
          <v-btn
            class="accept-labeled-question-btn"
            color="primary"
            block
            @click="acceptLabeledQuestion(question)"
          >
            PRIHVATI PITANJE
          </v-btn>
        </div>
      </div>
    </v-card>
    <v-snackbar v-model="snackbar">
      {{ errorMessage }}
      <template v-slot:action="{ attrs }">
        <v-btn color="primary" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>


<style scoped>
.card-container {
  margin: 10px;
  padding: 10px;
}
.title-question {
  display: inline-block;
  height: 64px;
  line-height: 80px;
  text-align: center;
  vertical-align: middle;
  padding-right: 10px;
}
.labeled-questions-navigation {
  position: absolute;
  top: 10px;
  right: 20px;
}
.question-title-holder {
  display: inline-flex;
}
.question-title {
  display: flex;
  justify-content: space-around;
}
.accept-question-section {
  display: flex;
  justify-content: flex-end;
}
</style>


<script>
import CategorySection from "./CategorySection"

export default {
  name: "LabelingQuestion",
  props: ["question"],
  components: { CategorySection },
  data() {
    return {
      snackbar: false,
      errorMessage: "",
    };
  },
  methods: {
    acceptLabeledQuestion(question) {
      this.$store.dispatch("acceptLabeledQuestion", question).catch((err) => {
        this.errorMessage =
          err.response !== undefined && "data" in err.response
            ? err.response.data
            : "Unexpected error happened!";

        this.snackbar = true;
      });
    }
  },
};
</script>