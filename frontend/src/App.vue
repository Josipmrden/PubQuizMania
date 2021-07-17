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
        <li class="nav-item">
          <router-link to="/labeling" class="nav-link">
            <p class="nav-text">OZNAČI PITANJA</p>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/quiz" class="nav-link">
            <p class="nav-text">KVIZ</p>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/pvp" class="nav-link">
            <p class="nav-text">DVOBOJ</p>
          </router-link>
        </li>
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

.nav-item {
  display: inline-block;
  height: 64px;
  line-height: 64px;
  text-align: center;
  vertical-align: middle;
  padding-left: 30px;
  padding-right: 30px;
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

.nav-item:hover {
  transition: 0.3s;
  background-color: #eee;
}

.nav-link {
  text-decoration: none;
  color: black !important;
}

.nav-text {
  font-size: 22px;
  font-weight: 500;
}
</style>

<script>

export default {
  name: "App",

  components: {
  },

  data: () => ({}),
};
</script>
