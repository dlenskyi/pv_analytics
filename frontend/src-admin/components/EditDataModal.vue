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
      @ok="verifyForm">
      <b-form @submit.prevent="verifyForm">

        <!--VALUE-->
        <b-form-group
          id="value-group"
          :label="$t('form.meter_data.value')"
          :invalid-feedback="invalidValue"
          :state="stateValue"
          label-for="value"
          :description="$t('form.meter_data.help_text.value')"
        >
          <b-form-input
            id="value"
            v-model="selectedObject.cellValue"
            :state="stateValueInput"
            :placeholder="$t('form.meter_data.value')"
          ></b-form-input>
        </b-form-group>

        <!--MESSAGE-->
        <b-form-group
          id="message-group"
          :label="$t('form.meter_data.message')"
          :invalid-feedback="invalidMessage"
          :state="stateMessage"
          label-for="message"
          :description="$t('form.meter_data.help_text.message')"
        >
          <b-form-textarea
            id="message"
            v-model="selectedObject.message"
            :placeholder="$t('form.meter_data.message')"
            rows="2"
            :state="stateValueInput"
            max-rows="5"
          ></b-form-textarea>
        </b-form-group>
        <b-button
          block
          variant="info"
          v-if="selectedObject.item[selectedObject.cellIndex].corrections"
          @click="showCorrectionHistory"
        >
          {{ $t('modal.meter_data.show_history') }}
        </b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
  import { required, integer } from 'vuelidate/lib/validators'

  export default {
    name: 'EditDataModal',

    data () {
      return {
        loading: false,
        dataCorrections: [],
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
      selectedObject: {
        cellValue: {
          required,
          integer,
        },
        message: {
          required
        },
      }
    },

    computed: {

      payloads () {
        return {
          message: this.selectedObject.message,
          value: this.selectedObject.cellValue,
          key: this.selectedObject.cellIndex,
          meter_data_id: this.selectedObject.item.id
        }
      },

      // VALIDATIONS

      stateValue () {
        return !this.$v.selectedObject.cellValue.$error
      },
      stateValueInput () {
        return !this.$v.selectedObject.cellValue ? false : null
      },
      invalidValue () {
        if (this.$v.selectedObject.cellValue.$error) {
          if (!this.$v.selectedObject.cellValue.required)
            return this.$t('validation.required', { field: this.$t('form.meter_data.value') })
          else if (!this.$v.selectedObject.cellValue.integer)
            return this.$t('validation.integer', { field: this.$t('form.meter_data.value') })
        }
        return null
      },

      stateMessage () {
        return !this.$v.selectedObject.message.$error
      },
      stateMessageInput () {
        return !this.$v.selectedObject.message ? false : null
      },
      invalidMessage () {
        if (this.$v.selectedObject.message.$error) {
          if (!this.$v.selectedObject.message.required)
            return this.$t('validation.required', { field: this.$t('form.meter_data.value') })
        }
        return null
      },
    },

    methods: {
      resetForm () {
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
