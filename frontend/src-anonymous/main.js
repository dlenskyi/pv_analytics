import Vue from 'vue'
import App from '@base/App.vue'

// local modules
import i18n from '@base/i18n'
import store from '@anonymous/store'
import router from '@anonymous/router'

// library modules
import Loading from 'vue-loading-overlay'
import vueMoment from 'vue-moment'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import Notifications from 'vue-notification'
import Vuelidate from 'vuelidate'
import moment from 'moment'
import 'moment/locale/uk'
import 'moment/locale/ru'

// CSS
import 'vue-loading-overlay/dist/vue-loading.css'
import '@base/styles/ourStyles.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(Notifications)
Vue.use(Loading)
Vue.use(Vuelidate)
Vue.use(vueMoment, { moment })
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.config.devtools = process.env.VUE_APP_DEVTOOLS || false

new Vue({
  i18n,
  store,
  router,
  render: h => h(App)
}).$mount('#app')
