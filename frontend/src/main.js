import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { store } from './store/store.js'
import { router } from './router.js'

Vue.config.productionTip = false

/* if (process.env.NODE_ENV === 'development') {
  const { worker } = require('./mocks/browser')
  worker.start()
}
 */

new Vue({
  vuetify,
  store,
  router,
  render: h => h(App)
}).$mount('#app');