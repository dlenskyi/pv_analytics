<template>
  <div>
    <b-container class="wide">
      <head-block :title="$t('table.correction_data.title')" />
      <content-table
        :fields="fields"
        :templates="templates"
        :items="correctedDataByMeter"
        :slots="templates"
      >
        <template
          slot="date"
          slot-scope="data"
        >{{ formatDate(data.tbl.item.date) }}</template>
        <template slot="actions" slot-scope="data">
          <div class="d-flex justify-content-center">
            <b-button
              size="sm"
              v-b-tooltip.hover
              :title="$t('table.general.button_delete')"
              variant="danger"
              @click="deleteObject(data.tbl.item)">
              <b-icon icon="trash"></b-icon>
            </b-button>
          </div>
        </template>
      </content-table>
      <span v-if="!loader.isActive && !correctedDataByMeter.length" class="no-table-data">
        {{ $t('table.general.no_data') }}
      </span>
      <confirm-item-modal
        modalId="delete-item"
        :okButtonTitle="$t('modal.general.ok_button')"
        :cancelButtonTitle="$t('modal.general.cancel_button')"
        :title="$t('modal.correction_data.title_delete')"
        :text="$t('modal.correction_data.text_delete')"
        @onConfirm="deleteCorrectionData"/>
    </b-container>
  </div>
</template>

<script>
  import ContentTable from '@base/components/ContentTable'
  import Formatting from '@base/mixins/Formatting.vue'
  import Deletion from '@base/mixins/Deletion.vue'
  import ConfirmItemModal from '@base/components/ConfirmItemModal.vue'
  import HeadBlock from '@base/components/HeadBlock.vue'
  import { mapState } from 'vuex'


  export default {
    name: 'CorrectionDataView',

    components: {
      ContentTable,
      ConfirmItemModal,
      HeadBlock
    },

    mixins: [ Formatting, Deletion ],

    data () {
      return {
        loader: { isActive: true },
        fields: [
          {
            key: 'meter_data_id',
            label: this.$t('form.correction_data.meter_data_id'),
            class: 'text-center',
          },
          {
            key: 'values',
            label: this.$t('form.correction_data.value'),
            class: 'text-center',
          },
          {
            key: 'message',
            label: this.$t('form.correction_data.message'),
            class: 'text-center',
          },
          {
            key: 'date',
            label: this.$t('form.correction_data.date'),
            class: 'text-center',
          },
          {
            key: 'actions',
            label: this.$t('form.general.actions'),
            class: 'text-center',
          }
        ],
        templates: [
          { name: 'date', field: 'date' },
          { name: 'actions', field: 'actions' },
        ]
      }
    },

    created () {
      this.getCorrectedDataByMeter()
    },

    computed: {
      ...mapState(['correctedDataByMeter'])
    },

    methods: {
      deleteCorrectionData () {
        this.confirmDeleteObject(
          this.$_actionTypes.DELETE_CORRECTED_METER_DATA,
          'id',
          this.$t('notifications.text.correction_data.success_correction_data_deleted'),
        )
      },

      getCorrectedDataByMeter () {
        if (this.loading)
          return
        this.loading = true
        this.loader = this.$loading.show(this.$_loaderOptions)
        this.$store.dispatch(this.$_actionTypes.GET_CORRECTED_DATA_BY_METER, this.$route.params.meterDataId)
          .catch((error) => {
            this.$_notifyError(error, this)
          })
          .finally(() => {
            this.loader.hide()
            this.loading = false
          })
      },
    }
  }
</script>

<style>

</style>
