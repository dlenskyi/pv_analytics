import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)

function loadLocaleMessages () {
  const locales = require.context('./locale', true, /[A-Za-z0-9-_,\s]+\.json$/i)
  const messages = {}
  locales.keys().forEach(key => {
    const matched = key.match(/([a-z0-9]+)\./i)
    if (matched && matched.length > 1) {
      const locale = matched[1]
      messages[locale] = locales(key)
    }
  })
  return messages
}

export default new VueI18n({
  // eslint-disable-next-line no-undef
  locale: LANGUAGE_CODE,
  // eslint-disable-next-line no-undef
  fallbackLocale: LANGUAGE_CODE,
  messages: loadLocaleMessages(),
  silentTranslationWarn: true
})
