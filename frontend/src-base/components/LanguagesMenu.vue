<template>
  <div class="languages-menu">
    <ul>
      <li @click="changeLocale('uk')"
          class="cursor-pointer"
          :class="{selected_lang: selectedLanguage('uk')}">
        <div class="d-inline" style="font-size:25px">
          <flag iso="ua" />
        </div>
      </li>
      <li @click="changeLocale('ru')"
          class="cursor-pointer"
          :class="{selected_lang: selectedLanguage('en')}">
        <div class="d-inline" style="font-size:25px">
          <flag iso="ru" />
        </div>
      </li>
    </ul>
  </div>
</template>

<script>

  export default {
    name: 'LanguagesMenu',

    data () {
      return  {
      }
    },

    methods: {
      selectedLanguage(language) {
        return language === this.$i18n.locale
      },

      changeLocale(language) {
        this.$store.dispatch(this.$_actionTypes.CHANGE_LANGUAGE, { language: language })
          .catch((error) => {
            this.$_notifyError(error, this)
          })
      },
    }
  }
</script>

<style scoped>

</style>
