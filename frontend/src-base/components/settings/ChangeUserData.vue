<template>
  <div>
    <div class="card-header mb-3">{{ $t('title.general.user_settings.change_data') }}</div>
    <b-form @submit.prevent="updateUserData">

      <!--EMAIL-->
      <b-form-group
        id="email-group"
        :label="$t('form.user_settings.email')"
        :invalid-feedback="invalidEmail"
        :state="stateEmail"
        label-for="email"
      >
        <b-form-input
          id="email"
          v-model="email"
          :state="($v.email.$error) ? false : null"
          :placeholder="$t('form.user_settings.placeholder_email')"
        ></b-form-input>
      </b-form-group>

      <!--USERNAME-->
      <b-form-group
        id="username-group"
        :label="$t('form.user_settings.username')"
        label-for="username"
        :invalid-feedback="invalidUsername"
        :state="stateUsername"
      >
        <b-form-input
          id="username"
          v-model="username"
          type="text"
          required
          :state="($v.username.$error) ? false : null"
          :placeholder="$t('form.user_settings.placeholder_username')"
        ></b-form-input>
      </b-form-group>
      <b-button
        type="submit"
        class="mr-4"
        :disabled="loading"
        variant="success">
        <b-icon icon="check"></b-icon>
        {{ $t('form.user_settings.button_apply') }}
      </b-button>
      <b-button
        @click="getUserData"
        variant="primary">
        <b-icon icon="arrow-repeat"></b-icon>
        {{ $t('form.user_settings.button_reset') }}
      </b-button>
    </b-form>

  </div>
</template>

<script>
  import { MIN_USERNAME_LENGTH, MAX_USERNAME_LENGTH } from "@base/configs"
  import { email, required, minLength, maxLength } from "vuelidate/lib/validators"
  import { mapState } from 'vuex'

  export default {
    name: 'ChangeUserData',

    data () {
      return {
        username: '',
        email: '',
        loading: false
      }
    },

    created () {
      this.getUserData()
    },

    computed: {
      ...mapState(['user']),

      payloads () {
        return {
          username: this.username,
          email: this.email
        }
      },
      stateUsername () {
        return (!this.$v.username.$error)
      },
      invalidUsername () {
        if (this.$v.username.$error) {
          if (!this.$v.username.required)
            return this.$t('validation.required', { field: this.$t('form.user_settings.username') })
          else if (!this.$v.username.minLength || !this.$v.username.maxLength)
            return this.$t('validation.length_min_max', {
              minLength: this.$v.username.$params.minLength.min,
              maxLength: this.$v.username.$params.maxLength.max,
              field: this.$t('form.user_settings.username')
            })
        }
        return null
      },
      stateEmail () {
        return (!this.$v.email.$error)
      },
      invalidEmail () {
        if (this.$v.email.$error) {
          if (!this.$v.email.email)
            return this.$t('validation.email')
        }
        return null
      },
    },

    validations: {
      username: {
        required,
        minLength: minLength(MIN_USERNAME_LENGTH),
        maxLength: maxLength(MAX_USERNAME_LENGTH),
      },
      email: {
        email
      }
    },

    methods: {
      updateUserData () {
        const oldEmail = this.user.email
        const oldUsername = this.user.name
        this.$v.$touch()
        if (oldEmail === this.email && oldUsername === this.username) {
          this.$notify({
            group: 'app',
            type: 'warn',
            title: this.$t('notifications.title.warning'),
            text: this.$t('notifications.text.user_settings.warning_user_data_identical')
          })
          return
        }
        if (this.$v.$invalid)
          return
        this.loading = true
        this.loader = this.$loading.show(this.$_loaderOptions)
        this.$store.dispatch(this.$_actionTypes.CHANGE_USER, this.payloads)
          .then(() => {
            this.$notify({
              group: 'app',
              type: 'success',
              title: this.$t('notifications.title.success'),
              text: this.$t('notifications.text.user_settings.success_user_updated')
            })
            this.updateUserConstants()
          })
          .catch((error) => {
            this.$_notifyError(error.response, this)
          })
          .finally(() => {
            this.loading = false
            this.loader.hide()
          })
      },

      getUserData () {
        this.loading = true
        this.loader = this.$loading.show(this.$_loaderOptions)
        this.$store.dispatch(this.$_actionTypes.GET_USER)
          .then(() => {
            this.updateUserConstants()
          })
          .catch((error) => {
            this.$_notifyError(error.response, this)
          })
          .finally(() => {
            this.loading = false
            this.loader.hide()
          })
      },

      updateUserConstants () {
        this.username = this.user.name
        this.email = this.user.email
      }
    }
  }
</script>

<style>

</style>
