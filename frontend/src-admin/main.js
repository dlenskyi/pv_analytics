import Vue from 'vue'
import App from '@base/App.vue'

// local modules
import i18n from '@base/i18n'
import store from '@admin/store'
import router from '@admin/router'

// library modules
import Loading from 'vue-loading-overlay'
import vueMoment from 'vue-moment'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import Vuelidate from 'vuelidate'
import moment from 'moment'
import 'moment/locale/uk'
import 'moment/locale/ru'
import Notifications from 'vue-notification'
import Paginate from 'vuejs-paginate'
import Multiselect from 'vue-multiselect'

// CSS
import 'vue-loading-overlay/dist/vue-loading.css'
import '@base/styles/ourStyles.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


Vue.use(Notifications)
Vue.use(Loading)
Vue.use(Vuelidate)
Vue.use(vueMoment, {moment})
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.component('paginate', Paginate)
Vue.component('multiselect', Multiselect)

Vue.config.devtools = process.env.VUE_APP_DEVTOOLS || false

new Vue({
  i18n,
  store,
  router,
  render: h => h(App)
}).$mount('#app')
