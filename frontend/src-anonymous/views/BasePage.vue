<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view/>
    <custom-footer />
  </div>
</template>

<script>
  import NavBar from "@base/components/NavBar.vue"
  import CustomFooter from "@base/components/CustomFooter.vue"

  export default {
    name: 'Base',

    components: {
      NavBar,
      CustomFooter
    },

    data () {
      return {
      }
    },

    created () {
      this.$store.commit(this.$_mutationTypes.SET_LOADER, false)
    },
  }
</script>

<style>

</style>
