<template>
  <li class="nav-item">
    <router-link :to="linkTo" class="nav-link">
      <p class="nav-text">
        <slot></slot>
      </p>
    </router-link>
  </li>
</template>


<style scoped>
.nav-item {
  display: inline-block;
  height: 64px;
  line-height: 64px;
  text-align: center;
  vertical-align: middle;
  padding-left: 30px;
  padding-right: 30px;
}

.nav-item:hover {
  transition: 0.3s;
  background-color: #eee;
}

.nav-link {
  text-decoration: none;
  color: var(--v-blue-base);
}

.nav-text {
  font-size: 22px;
  font-weight: 500;
}
</style>


<script>
export default {
  name: "NavigationItem",
  props: ["linkTo"],
  data: () => {
    return {};
  },
};
</script>
