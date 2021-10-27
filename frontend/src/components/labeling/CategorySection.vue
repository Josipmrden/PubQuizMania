<template>
  <div class="category-section">
    <v-checkbox
      v-for="(category, idx) in questionCategories"
      :key="idx"
      v-model="category.active"
      :label="category.name"
    ></v-checkbox>
  </div>
</template>

<style scoped>
.category-section {
  display: grid;
  grid-template-columns: auto auto auto auto;
  padding-bottom: 30px;
}
.category-section >>> .v-slide-group__content {
  justify-content: center;
}

.category-section >>> .v-messages {
  min-height: 0px;
}
</style>

<script>
export default {
  name: "CategorySection",
  props: ["questionCategories"],
};
</script>
