<template>
  <div>
    <b-container>
      <b-row class="justify-content-center mt-5"><h2 class="text-center">{{ $t('pages.login.admin.welcome') }}</h2></b-row>
      <b-row class="justify-content-center">
        <b-form @submit.prevent="authAdminUser" class="w-50">
          <b-form-group
            id="username-group"
            :label="$t('auth.login')"
            label-for="username"
            :invalid-feedback="invalidCredentials"
            :state="stateUsername"
          >
            <b-form-input
              id="username"
              v-model="username"
              type="text"
              :state="stateUsernameInput"
              :placeholder="$t('auth.field.username')"
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id="password-group"
            :label="$t('auth.password')"
            label-for="password"
            :invalid-feedback="invalidPassword"
            :state="statePassword"
          >
            <b-form-input
              id="password"
              v-model="password"
              type="password"
              @blur="invalidCredentials = null"
              :state="statePasswordInput"
              :placeholder="$t('auth.placeholder_password')"
            ></b-form-input>
          </b-form-group>
          <div class="form-actions">
            <b-button
              type="submit"
              :disabled="loading"
              variant="primary">
              {{ $t('auth.login_button') }}
            </b-button>
          </div>
        </b-form>
      </b-row>
    </b-container>

  </div>
</template>

<script>
  import { ADMIN_SECTION_PATH } from '@base/configs'
  import { required } from "vuelidate/lib/validators"

  export default {
    name: 'AdminLogin',

    data () {
      return {
        username: null,
        password: null,
        invalidCredentials: null,
        loading: false,
      }
    },

    watch: {
      username () {
        this.invalidCredentials = null
      },
      password () {
        this.invalidCredentials = null
      },
    },

    computed: {
      payloads () {
        return {
          username: this.username,
          password: this.password,
        }
      },
      stateUsernameInput () {
        return this.invalidCredentials !== null ? false : null
      },
      stateUsername () {
        return this.invalidCredentials === null
      },
      statePasswordInput () {
        return (this.$v.password.$error || this.invalidCredentials !== null) ? false : null
      },
      statePassword () {
        return !this.$v.password.$error || this.invalidCredentials !== null
      },
      invalidPassword () {
        if (this.$v.password.$error) {
          if (!this.$v.password.required)
            return this.$t('validation.required', { field: this.$t('auth.field.password') })
        }
        return null
      },
    },

    validations: {
      username: {
        required,
      },
      password: {
        required
      },
    },

    methods: {

      authAdminUser () {
        this.$v.$touch()
        if (this.$v.$invalid)
          return
        this.authUser()
      },

      authUser () {
        this.$v.$reset()
        this.invalidCredentials = null
        this.loading = true
        this.loader = this.$loading.show(this.$_loaderOptions)
        this.$store.dispatch(this.$_actionTypes.LOGIN_USER, this.payloads)
          .then((response) => {
            if (response.is_admin) {
              window.location.replace(ADMIN_SECTION_PATH)
            } else {
              this.$notify({
                group: 'app',
                type: 'warn',
                title: this.$t('notifications.title.warning'),
                text: this.$t('error.permission_denied')
              })
            }
          })
          .catch((error) => {
            this.invalidCredentials = error.data.error
            this.$notify({
              group: 'app',
              type: 'error',
              title: this.$t('notifications.title.error'),
              text: error.data.error
            })
          })
          .finally(() => {
            this.loading = false
            this.loader.hide()
          })
      }
    }
  }
</script>

<style>

</style>
