<template>
  <div>
    <b-container class="wide">
      <div class="mb-1 d-flex justify-content-between align-items-center">
        <head-block :title="$t('title.admin.meter_data')" />
        <b-button
          @click="showFilter = !showFilter"
          variant="primary">
          <b-icon icon="filter" scale="1.3"></b-icon>
          {{ $t('table.general.button_filters') }}
        </b-button>
      </div>
      <div v-if="showFilter">
        <meter-data-filter
          @filter-applied="applyFilters"
        />
      </div>

      <content-table
        :fields="fields"
        :templates="templates"
        :items="items"
        @row-clicked="onRowClicked"
        :slots="templates"
      >
        <template
          slot="dayTotal"
          slot-scope="data"
        >{{ getDayTotal(data.tbl.item) }}</template>
        <!--Skip first templates-->
        <template
          :slot="templateObj.name"
          slot-scope="data"
          v-for="templateObj in templates.slice(1, templates.length)"
        >{{ data.tbl.item[templateObj.field].value }}</template>
      </content-table>
      <span v-if="!loader.isActive && !initialMeterData.length" class="no-table-data">
        {{ $t('table.general.no_data') }}
      </span>
      <div
        v-if="pagesCount > 1"
        class="pagination_div">
        <paginate
          :value="page"
          :page-count="pagesCount"
          container-class="pagination-container"
          page-class="page-item"
          prev-class="btn btn-primary"
          next-class="btn btn-primary"
          active-class="active-class"
          :click-handler="clickPaginationCallback" />
      </div>
      <edit-data-modal
        @objectUpdated="setData"
        modalId="edit-data"
        v-if="selectedObject"
        :selectedObject="selectedObject"/>
    </b-container>
  </div>
</template>

<script>

  import { mapState, mapGetters } from 'vuex'
  import ContentTable from '@base/components/ContentTable'
  import EditDataModal from '@admin/components/EditDataModal.vue'
  import MeterDataFilter from '@admin/components/MeterDataFilter.vue'
  import { METER_QUANTITY } from '@base/configs'
  import HeadBlock from '@base/components/HeadBlock.vue'
  import Deletion from '@base/mixins/Deletion.vue'

  export default {
    name: 'MeterDataView',

    components: {
      HeadBlock,
      ContentTable,
      EditDataModal,
      MeterDataFilter,
    },

    mixins: [ Deletion ],

    data () {
      return {
        items: [],
        selectedObject: null,
        loading: false,
        loader: { isActive: true },
        showFilter: false,
      }
    },

    created () {
      // this.getInitialMeterData()
      this.getCorrectedMeterData()
    },

    watch: {
      correctedMeterData () {
        this.setData()
      }
    },

    computed: {
      ...mapState(['initialMeterData', 'correctedMeterData']),
      ...mapGetters({
        page: 'getInitialMeterDataPage',
        pagesCount: 'getInitialMeterDataPagesCount'
      }),

      fields () {
        // Generate fields
        const fields = []
        fields.push({ key: 'id', label: this.$t('form.meter_data.id'), class: 'text-center', tdClass: 'p-0', })
        fields.push({ key: 'device_name', label: this.$t('form.meter_data.device_name'), class: 'text-center', tdClass: 'p-0', })
        fields.push({ key: 'site_name', label: this.$t('form.meter_data.site_name'), class: 'text-center', tdClass: 'p-0', })
        fields.push({ key: 'date', label: this.$t('form.meter_data.date'), class: 'text-center', tdClass: 'p-0', })
        fields.push({ key: 'day_total', label: this.$t('form.meter_data.day_total'), class: 'text-center', tdClass: 'p-0', })
        for (let meter_index = 1; meter_index <= METER_QUANTITY; meter_index++) {
          const fieldObj = {
            key: meter_index.toString(),
            label: meter_index.toString(),
            class: 'text-center',
            tdClass: 'cursor-pointer p-0',
          }
          fields.push(fieldObj)
        }
        return fields
      },

      templates () {
        // Generate templates
        const templates = []
        templates.push({ name: 'dayTotal', field: 'day_total' })
        for (let meter_index = 1; meter_index <= METER_QUANTITY; meter_index++) {
          const templateObj = {
            name: meter_index,
            field: meter_index,
          }
          templates.push(templateObj)
        }
        return templates
      },
    },

    methods: {

      clickPaginationCallback (pageNum) {
        if (this.loading)
          return
        this.loading = true
        this.loader = this.$loading.show(this.$_loaderOptions)

        this.$store.commit(this.$_mutationTypes.SET_INITIAL_METER_DATA_PAGE, pageNum)
        this.$store.dispatch(this.$_actionTypes.GET_INITIAL_METER_DATA)
          .then((res) => {
            this.$store.commit(this.$_mutationTypes.SET_INITIAL_METER_DATA_PAGES_COUNT, res.total_pages)
            this.setData()
          })
          .catch((error) => {
            this.$_notifyError(error, this)
          })
          .finally(() => {
            this.loader.hide()
            this.loading = false
          })
      },

      applyFilters (filters) {
        this.$store.commit(this.$_mutationTypes.SET_INITIAL_METER_DATA_FILTERS, filters)
        this.getInitialMeterData()
      },

      getInitialMeterData () {
        if (this.loading)
          return
        this.loading = true
        this.loader = this.$loading.show(this.$_loaderOptions)
        this.$store.commit(this.$_mutationTypes.SET_INITIAL_METER_DATA_PAGE, 1)
        this.$store.dispatch(this.$_actionTypes.GET_INITIAL_METER_DATA)
          .then((res) => {
            this.$store.commit(this.$_mutationTypes.SET_INITIAL_METER_DATA_PAGES_COUNT, res.total_pages)
            this.setData()
          })
          .catch((error) => {
            this.$_notifyError(error, this)
          })
          .finally(() => {
            this.loader.hide()
            this.loading = false
          })
      },

      getDayTotal (obj) {
        let total = 0
        for (let meter_index = 1; meter_index <= METER_QUANTITY; meter_index++) {
          total += Number(obj[meter_index].value)
        }
        return total
      },

      getCorrectedMeterData () {
        if (this.loading)
          return
        this.loading = true
        this.loader = this.$loading.show(this.$_loaderOptions)
        this.$store.dispatch(this.$_actionTypes.GET_CORRECTED_METER_DATA)
          .catch((error) => {
            this.$_notifyError(error, this)
          })
          .finally(() => {
            this.loader.hide()
            this.loading = false
            this.getInitialMeterData()
          })
      },

      setData () {
        // Reset Meter data list
        this.items = []

        // Iterate through initialMeterData
        for (const obj of this.$_.cloneDeep(this.initialMeterData)) {

          const meterObj = this.$_.cloneDeep(obj)

          meterObj['_cellVariants'] = {}

          const correctionList = this.correctedMeterData.filter(o => o.meter_data_id === parseInt(meterObj.id))
          for (let meter_index = 1; meter_index <= METER_QUANTITY; meter_index++) {
            meterObj[meter_index] = {
              'value': meterObj[meter_index],
            }
          }
          if (correctionList.length) {
            const lastCorrectedData = correctionList[0]
            meterObj[parseInt(lastCorrectedData.key)] = {
              'value': lastCorrectedData.value,
              'corrections': correctionList
            }
            meterObj['_cellVariants'] = Object.assign({[parseInt(lastCorrectedData.key)]: 'primary'}, meterObj['_cellVariants'])
          }
          this.items.push(meterObj)
        }
      },

      onRowClicked (item, e) {
        // If user clicked on fields that don't include data - do nothing
        // Minus 4 because we have first 5 fields (indexing starts with 0) other than data that begins with 1
        const clickedIndex = e.target.cellIndex - 4
        if (Object.keys(item).includes(clickedIndex.toString())) {
          this.selectedObject = {
            cellIndex: clickedIndex,
            cellValue: item[clickedIndex].value,
            item: item,
          }
          this.$nextTick(() => {
            this.$bvModal.show('edit-data')
          })
        }
      },
    }
  }

</script>

<style>

</style>
