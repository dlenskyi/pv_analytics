<template>
  <div id="app">
    <nav-bar />
    <div class="not-found-section">
      <div class="not-found-content">
        <h1>{{ $t('page_not_found.header') }}</h1>
        <span>{{ $t('page_not_found.text') }}</span>
        <p class="mt-2">
          <b-button @click="$router.push({ name: 'base' })">
            {{ $t('page_not_found.text_button') }}
          </b-button>
        </p>
      </div>
      <b-img fluid :src="require('@base/assets/images/svg/page-not-found.svg')"></b-img>
    </div>
    <router-view />
    <custom-footer />
  </div>
</template>

<script>

  import NavBar from "@base/components/NavBar.vue"
  import CustomFooter from "@base/components/CustomFooter.vue"

  export default {
    name: 'NotFound',

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
      console.log(this.$router)
    }
  }
</script>
