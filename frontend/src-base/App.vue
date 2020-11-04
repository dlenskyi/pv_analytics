<template>
  <div>
    <vue-loading
      :active.sync="$store.state.showLoader"
      :color="loaderOptions.color"
      :background-color="loaderOptions.backgroundColor"
      :opacity="loaderOptions.opacity"
    />
    <notifications
      group="app"
      position="top center"
      :duration="7000"
      :width="`${notificationWidth}px`"
    />
    <router-view/>
  </div>
</template>

<script>
  import Vue from 'vue'
  import VueLoading from 'vue-loading-overlay/src/js/Component'
  import _ from 'lodash'
  import FlagIcon from 'vue-flag-icon'
  import axios from 'axios'

  import { actionTypes, mutationTypes } from '@base/store/store-types'
  import { loaderOptions } from '@base/configs'

  Vue.use(FlagIcon)

  Vue.prototype.$_actionTypes = actionTypes
  Vue.prototype.$_mutationTypes = mutationTypes
  Vue.prototype.$_loaderOptions = loaderOptions
  Vue.prototype.$_ = _
  // eslint-disable-next-line no-undef
  Vue.prototype.$_languageCode = LANGUAGE_CODE

  Vue.prototype.$_notifyError = (error, context) => {
    // eslint-disable-next-line no-console
    console.log(error)
    if (error.status !== 500) {
      if (Array.isArray(error.data) && error.data.length === 1) {
        context.$notify({
          group: 'app',
          type: 'error',
          title: context.$t('notifications.title.error'),
          text: error.data[0]
        })
      }
      else if (!Array.isArray(error.data) && Object.keys(error.data)[0] !== "error") {
        for (const title in error.data) {
          let capitalized = title.charAt(0).toUpperCase() + title.slice(1)
          const notification_title = Object.keys(error.data)[0] !== "non_field_errors" ?
            capitalized.replace('_', ' ') : context.$t('notifications.title.error')

          context.$notify({
            group: 'app',
            type: 'error',
            title: notification_title,
            text: error.data[title][0]
          })
        }
      } else {
        context.$notify({
          group: 'app',
          type: 'error',
          title: context.$t('notifications.title.error'),
          text: Object.values(error.data)[0]
        })
      }
    } else {
      context.$notify({
        group: 'app',
        type: 'error',
        title: error.statusText,
        text: context.$t('error.internal_error'),
      })
    }
  }

  axios.defaults.xsrfCookieName = 'csrftoken'
  axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

  export default {
    name: 'App',
    components: {VueLoading},
    data () {
      return {
        notificationWidth: 500,
        loaderOptions: loaderOptions
      }
    },
    watch: {
      $route () {
        this.$store.commit(this.$_mutationTypes.SET_LOADER, false)
      }
    },

    mounted() {
      this.$moment.locale(this.$i18n.locale)
    },

    created () {
      if (window.innerWidth < 500) {
        this.notificationWidth = 300
      }
    },
    methods: {

    }
  }
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style>

</style>
