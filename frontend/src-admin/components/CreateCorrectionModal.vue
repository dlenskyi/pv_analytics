<template>
  <div>
    <b-modal
      :title="$t('modal.meter_data.title_edit', {
        id: selectedObject.item.id
      })"
      :id="modalId"
      :ok-title="$t('modal.general.ok_button')"
      :cancel-title="$t('modal.general.cancel_button')"
      @show="resetForm"
      @ok="verifyForm"
      size="lg">
      <b-form @submit.prevent="verifyForm">
        <b-row
          cols="2"
          cols-sm="3"
          cols-md="3"
          cols-lg="3"
        >
          <b-col
            v-for="(obj, key) in selectedObject.values"
            :key="key"
          >

            <!--VALUE-->
            <b-form-group
              id="value-group"
              :label="$t('form.meter_data.value', { key: obj.key })"
              :invalid-feedback="invalidValue(obj)"
              :state="stateValue(obj)"
              label-for="value"
              :description="$t('form.meter_data.help_text.value')"
            >
              <b-form-input
                @keyup.enter="$event.target.blur()"
                @focus="focusInput(obj)"
                :state="stateValueInput(obj)"
                v-model="obj.value"
                id="value"
                :placeholder="$t('form.meter_data.value', { key: obj.key })"
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col>
            <!--MESSAGE-->
            <b-form-group
              id="message-group"
              :label="$t('form.correction_data.message')"
              :invalid-feedback="invalidMessage"
              :state="stateMessage"
              label-for="message"
              :description="$t('form.correction_data.help_text.message')"
            >
              <b-form-textarea
                id="message"
                v-model="message"
                :placeholder="$t('form.correction_data.message')"
                rows="2"
                :state="stateMessageInput"
                max-rows="5"
              ></b-form-textarea>
            </b-form-group>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <b-button
              block
              variant="info"
              @click="showCorrectionHistory"
            >
              {{ $t('modal.meter_data.show_history') }}
            </b-button>
          </b-col>
        </b-row>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
  import { required, requiredIf, integer } from 'vuelidate/lib/validators'

  export default {
    name: 'CreateCorrectionModal',

    data () {
      return {
        loading: false,
        dataCorrections: [],
        selectedValue: null,
        message: null
      }
    },

    props: {
      modalId: {
        type: String,
        required: true,
      },
      selectedObject: {
        type: Object,
        required: true,
      }
    },

    validations: {
      selectedValue: {
        value: {
          required: requiredIf(function (nestedModel) {
            return nestedModel
          }),
          integer
        }
      },
      message: {
        required
      },
    },

    computed: {

      payloads () {
        return {
          message: this.message,
          values: this.selectedObject.values.map(obj => parseInt(obj.value)),
          meter_data_id: this.selectedObject.item.id
        }
      },

      // VALIDATIONS

      stateMessage () {
        return !this.$v.message.$error
      },
      stateMessageInput () {
        return this.$v.message.$error ? false : null
      },
      invalidMessage () {
        if (this.$v.message.$error) {
          if (!this.$v.message.required)
            return this.$t('validation.required', { field: this.$t('form.correction_data.message') })
        }
        return null
      },
    },

    methods: {

      stateValue (valueObj) {
        return this.$v.selectedValue.$model &&
          valueObj.key === this.$v.selectedValue.$model.key &&
          !this.$v.selectedValue.value.$error
      },
      stateValueInput (valueObj) {
        return (this.$v.selectedValue.$model &&
          valueObj.key === this.$v.selectedValue.$model.key &&
          this.$v.selectedValue.value.$error) ? false : null
      },
      invalidValue (valueObj) {
        if (this.$v.selectedValue.$model &&
          valueObj.key === this.$v.selectedValue.$model.key &&
          this.$v.selectedValue.value.$error) {
          if (!this.$v.selectedValue.value.required)
            return this.$t('validation.required', { field: this.$t('form.meter_data.value', {key: valueObj.key}) })
          else if (!this.$v.selectedValue.value.integer)
            return this.$t('validation.integer', { field: this.$t('form.meter_data.value', {key: valueObj.key}) })
        }
        return null
      },

      focusInput (item) {
        this.$v.selectedValue.$reset()
        this.selectedValue = item
        this.$v.selectedValue.$touch()
        this.inputFocused = true
      },

      setValue (item, key, value) {
        item[key] = value
        this.selectedValue = item
        this.$v.selectedValue.$touch()
      },

      resetForm () {
        this.message = null
        this.$v.$reset()
      },

      verifyForm (bvModalEvt) {
        bvModalEvt.preventDefault()
        this.$v.$touch()
        if (this.$v.$invalid)
          return
        this.applyCorrectedData()
      },
      applyCorrectedData () {
        if (this.loading)
          return
        this.loading = true
        this.loader = this.$loading.show(this.$_loaderOptions)
        this.$store.dispatch(this.$_actionTypes.CREATE_CORRECTED_METER_DATA, this.payloads)
          .then(() => {
            this.$emit('objectUpdated')
            this.$nextTick(() => {
              this.$bvModal.hide(this.modalId)
            })
            this.$notify({
              group: 'app',
              type: 'success',
              title: this.$t('notifications.title.success'),
              text: this.$t('notifications.text.meter_data.success_data_edited')
            })
          })
          .catch((error) => {
            this.$_notifyError(error.response, this)
          })
          .finally(() => {
            this.loader.hide()
            this.loading = false
          })
      },
      showCorrectionHistory () {
        const routeData = this.$router.resolve({
          name: 'corrected-data', params: { meterDataId: this.selectedObject.item.id }
        })
        window.open(routeData.href, '_blank')
      }
    }
  }
</script>

<style>

</style>
