<template>
  <v-stepper v-model="e1" vertical>
    <v-stepper-step :complete="e1 > 1" step="1">
      Odaberite vrstu igre
    </v-stepper-step>

    <v-stepper-content step="1">
      <v-card color="grey lighten-1" class="mb-12 pvp-form-card" height="100px">
        <div class="game-mode">
          <v-btn class="game-mode-btn" @click="hostModePressed">DOMAĆIN</v-btn>
          <v-btn class="game-mode-btn" @click="guestModePressed">GOST</v-btn>
        </div>
      </v-card>
    </v-stepper-content>

    <div v-if="pickedMode">
      <div v-if="hostMode">
        <v-stepper-step :complete="e1 > 2" step="2">
          Odaberite kategorije
        </v-stepper-step>

        <v-stepper-content step="2">
          <v-card
            color="grey lighten-1"
            class="mb-12 pvp-form-card"
            height="100px"
          >
            <p>kurac</p>
          </v-card>
        </v-stepper-content>
      </div>
      <div v-else>
        <p>kurac</p>
      </div>
    </div>
  </v-stepper>
</template>


<style scoped>
.pvp-form-card {
  display: inline-block;
}

v-stepper-content >>> .v-stepper__wrapper {
  height: 100px !important;
}

.v-stepper__wrapper {
  height: 100px !important;
}

.game-mode {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  height: 100%;
}

.game-mode-btn {
  margin: 20px;
}
</style>


<script>
export default {
  name: "PVPForm",
  props: [],
  data: () => {
    return {
      e1: 1,
      pickedMode: false,
      hostMode: true,
    };
  },
  methods: {
    hostModePressed() {
      this.hostMode = true;
      this.pickedMode = true;
      this.gameModePressed();
    },
    guestModePressed() {
      this.hostMode = false;
      this.pickedMode = true;
      this.gameModePressed();
    },
    gameModePressed() {
      this.e1 = 2;
    },
  },
};
</script>
