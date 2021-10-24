<template>
  <div>
    <div class="pvp-container">
      <v-card class="card" v-if="gameMode">
        <div class="pvp-mode-form">
          <p>Izaberite način igre:</p>
          <div class="pvp-mode-options">
            <v-btn>DOMAĆIN</v-btn>
            <v-btn>GOST</v-btn>
          </div>
        </div>
      </v-card>

      <v-card class="card" v-if="hostWaiting">
        <p>Vaš kod je:</p>
      </v-card>

      <v-card class="card" v-if="guestEnteringKey">
        <p>Unesite kod za kviz</p>
      </v-card>

      <v-card class="card" v-if="wrongGuestKey">
        <p>Pogrešan kod!</p>
      </v-card>

      <v-card class="card" v-if="gameModeNotSupported">
        <p>Način igre nije još podržan!</p>
      </v-card>
      <PVPForm v-if="!gameModeNotSupported"/>
    </div>
  </div>
</template>


<style scoped>
.card {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 20px;
}
p {
  font-size: 30px;
  text-align: center;
}

.pvp-mode-options {
  display: flex;
  justify-content: space-around;
  justify-items: center;
}
</style>


<script>
import PVPForm from "./PVPForm";

export default {
  name: "PVPSection",
  components: {
    PVPForm,
  },
  props: [],
  data() {
    return {
      gameModeNotSupported: false,
      gameMode: false,
      hostWaiting: false,
      guestEnteringKey: false,
      wrongGuestKey: false,
      gameStarting: false,
    };
  },
  methods: {},
  computed: {},
};
</script>
