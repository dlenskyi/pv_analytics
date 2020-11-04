<template>
  <div>
    <div class="card-header mb-3">{{ $t('title.general.user_settings.change_password') }}</div>
    <b-form @submit.prevent="updatePassword">

      <!--OLD PASSWORD-->
      <b-form-group
        id="old-pass-group"
        :label="$t('form.user_settings.old_password')"
        :invalid-feedback="invalidOldPassword"
        :state="stateOldPassword"
        label-for="old-pass"
      >
        <b-form-input
          id="old-pass"
          type="password"
          v-model="passwords.oldPassword"
          :state="($v.passwords.oldPassword.$error) ? false : null"
          :placeholder="$t('form.user_settings.placeholder_password')"
        ></b-form-input>
      </b-form-group>

      <!--NEW PASSWORD1-->
      <b-form-group
        id="new-pass1-group"
        :label="$t('form.user_settings.new_password1')"
        :invalid-feedback="invalidNewPassword1"
        :state="stateNewPassword1"
        label-for="new-pass1"
      >
        <b-form-input
          id="new-pass1"
          type="password"
          v-model="passwords.newPassword1"
          :state="($v.passwords.newPassword1.$error) ? false : null"
          :placeholder="$t('form.user_settings.placeholder_password')"
        ></b-form-input>
      </b-form-group>

      <!--NEW PASSWORD2-->
      <b-form-group
        id="new-pass2-group"
        :label="$t('form.user_settings.new_password2')"
        :invalid-feedback="invalidNewPassword2"
        :state="stateNewPassword2"
        label-for="new-pass2"
      >
        <b-form-input
          id="new-pass2"
          type="password"
          v-model="passwords.newPassword2"
          :state="($v.passwords.newPassword2.$error) ? false : null"
          :placeholder="$t('form.user_settings.placeholder_password')"
        ></b-form-input>
      </b-form-group>
      <b-button
        type="submit"
        :disabled="loading"
        variant="success">
        <b-icon icon="check"></b-icon>
        {{ $t('form.user_settings.button_apply') }}
      </b-button>
    </b-form>

  </div>
</template>

<script>
  import { required, sameAs } from "vuelidate/lib/validators"

  export const defaultPasswords = {
    oldPassword: '',
    newPassword1: '',
    newPassword2: ''
  }

  export default {
    name: 'ChangePassword',

    data () {
      return {
        passwords: { ...defaultPasswords },
        loading: false
      }
    },

    computed: {

      payloads () {
        return {
          old_password: this.passwords.oldPassword,
          new_password1: this.passwords.newPassword1,
          new_password2: this.passwords.newPassword2
        }
      },

      // VALIDATIONS
      stateOldPassword () {
        return (!this.$v.passwords.oldPassword.$error)
      },
      invalidOldPassword () {
        if (this.$v.passwords.oldPassword.$error) {
          if (!this.$v.passwords.oldPassword.required)
            return this.$t('validation.required', { field: this.$t('form.user_settings.old_password') })
        }
        return null
      },
      stateNewPassword1 () {
        return (!this.$v.passwords.newPassword1.$error)
      },
      invalidNewPassword1 () {
        if (this.$v.passwords.newPassword1.$error) {
          if (!this.$v.passwords.newPassword1.required)
            return this.$t('validation.required', { field: this.$t('form.user_settings.new_password1') })
        }
        return null
      },
      stateNewPassword2 () {
        return (!this.$v.passwords.newPassword2.$error)
      },
      invalidNewPassword2 () {
        if (this.$v.passwords.newPassword2.$error) {
          if (!this.$v.passwords.newPassword2.required)
            return this.$t('validation.required', { field: this.$t('form.user_settings.new_password1')})
          else if (!this.$v.passwords.newPassword2.sameAs)
            return this.$t('validation.same_as', { field: this.$t('form.user_settings.new_password1') })
        }
        return null
      },
    },

    validations: {
      passwords: {
        oldPassword: {
          required
        },
        newPassword1: {
          required,
        },
        newPassword2: {
          required,
          sameAs: sameAs('newPassword1')
        }
      }
    },

    methods: {
      updatePassword () {
        this.$v.$touch()
        if (this.passwords.oldPassword === this.passwords.newPassword1) {
          this.$notify({
            group: 'app',
            type: 'warn',
            title: this.$t('notifications.title.warning'),
            text: this.$t('notifications.text.user_settings.warning_passwords_identical')
          })
          return
        }
        if (this.$v.$invalid) {
          return
        }
        this.loading = true
        this.loader = this.$loading.show(this.$_loaderOptions)
        this.$store.dispatch(this.$_actionTypes.CHANGE_PASSWORD, this.payloads)
          .then((res) => {
            if (res.detail) {
              this.$notify({
                group: 'app',
                type: 'success',
                title: this.$t('notifications.title.success'),
                text: res.detail
              })
              this.$v.$reset()
              this.passwords = { ...defaultPasswords }
            } else {
              this.$notify({
                group: 'app',
                type: 'error',
                title: this.$t('notifications.title.error'),
                text: this.$t('error.internal_error')
              })
            }
          })
          .catch((error) => {
            this.$_notifyError(error.response, this)
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
