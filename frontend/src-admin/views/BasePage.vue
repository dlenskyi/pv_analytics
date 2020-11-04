<template>
  <div id="app">
    <nav-bar :navItems="navItems"
             @itemClicked="onItemClick" />
    <router-view/>
    <custom-footer />
  </div>
</template>

<script>
  import NavBar from "@base/components/NavBar.vue"
  import CustomFooter from "@base/components/CustomFooter.vue"
  import { NAV_ITEMS } from "@admin/configs"

  export default {
    name: 'Base',

    components: {
      NavBar,
      CustomFooter
    },

    data () {
      return {
        navItems: NAV_ITEMS,
      }
    },

    created () {
      this.loader = this.$loading.show(this.$_loaderOptions)
      this.$store.dispatch(this.$_actionTypes.GET_USER)
        .catch((error) => {
          this.$_notifyError(error, this)
        })
        .finally(() => {
          this.loader.hide()
        })
    },

    methods: {
      onItemClick (navItem) {
        if (navItem.text === this.$t('navigation.general.logout'))
          this.$store.dispatch(this.$_actionTypes.LOGOUT)
      }
    }

  }
</script>

<style>

</style>
