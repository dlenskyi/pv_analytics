<template>
  <section id="head">
    <b-navbar toggleable="lg" type="light" variant="light" fixed="top">
      <b-navbar-brand :to="brandHref">
        <span>{{ brandName }}</span>
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav @click="itemClicked(navItem)" v-for="(navItem, key) in navItems" :key="key">
          <b-nav-item :to="navItem.href">{{ navItem.text }}</b-nav-item>
        </b-navbar-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <languages-menu />
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </section>
</template>

<script>

  import LanguagesMenu from "@base/components/LanguagesMenu.vue"
  import i18n from '@base/i18n'

  export default {
    name: 'NavBar',

    components: {
      LanguagesMenu
    },

    props: {
      brandName: {
        type: String,
        default: () => i18n.t('title.home.company')
      },
      brandHref: {
        default () {
          return { name: 'base' }
        }
      },
      navItems: {
        type: Array,
        required: false
      }
    },

    data () {
      return  {
      }
    },

    methods: {
      itemClicked (navItem) {
        this.$emit('itemClicked', navItem)
      }
    }
  }
</script>

<style scoped>

</style>
