<template>
  <v-app>
    <v-app-bar app light class="app-bar">
      <div class="d-flex align-center toast-logo">
        <v-img
          alt="PQM Logo"
          class="shrink mr-2"
          src="@/assets/toast.png"
          width="40"
        />
        <div class="nav-item-logo">
          <p class="nav-text-logo">Pub Quiz Mania</p>
        </div>
      </div>

      <v-spacer></v-spacer>

      <ul class="nav-options">
        <NavigationItem linkTo='/labeling'>OZNAČI PITANJA</NavigationItem>
        <NavigationItem linkTo='/quiz'> KVIZ</NavigationItem>
        <NavigationItem linkTo='/pvp'>DVOBOJ</NavigationItem>
      </ul>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap");
.application {
  font-family: "Roboto", Arial;
  background-color: white;
}

.v-toolbar__content {
  height: 64px !important;
  padding: 0px !important;
}

.nav-text-logo {
  font-size: 30px;
  font-weight: 500;
}

.toast-logo {
  padding-left: 10px;
}

.nav-options {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.nav-item-logo {
  display: inline-block;
  height: 64px;
  line-height: 64px;
  text-align: center;
  vertical-align: middle;
  padding-left: 10px;
  padding-right: 10px;
}

.nav-link {
  text-decoration: none;
  color: black !important;
}
</style>

<script>
import NavigationItem from "./components/navigation/NavigationItem";

export default {
  name: "App",

  components: {
    NavigationItem
  },

  data: () => ({}),
};
</script>
