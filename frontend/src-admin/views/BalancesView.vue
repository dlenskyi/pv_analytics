<template>
  <div>
    <b-container class="wide">
      <div class="mb-1 d-flex justify-content-between align-items-center">
        <head-block :title="$t('table.balances.title')" />
        <b-button
          @click="showFilter = !showFilter"
          variant="primary">
          <b-icon icon="filter" scale="1.3"></b-icon>
          {{ $t('table.general.button_filters') }}
        </b-button>
      </div>
      <div v-if="showFilter">
        <balances-filter
          @filter-applied="applyFilters"
        />
      </div>
      <div class="text-center" v-if="balances.length">
        <b-form-group
          id="chart-type-group"
          :label="$t('charts.balances.checkbox_title')"
          label-for="chart-type"
        >
          <b-form-checkbox-group
            id="chart-type"
            switches
            :options="checkboxOptions"
            v-model="chartType"
          >
          </b-form-checkbox-group>
        </b-form-group>
      </div>
      <balance-chart
        v-if="balances.length && filters &&
          filters.date_start && filters.date_end && chartType.length"
        :balances="getFormattedChartsData"
        :range-min="filters.date_start"
        :range-max="filters.date_end"/>
      <span
        v-if="filters && !filters.site"
        class="no-table-data"
      >
        {{ $t('charts.general.no_chart_sites') }}
      </span>
      <span
        v-else-if="filters && !filters.date_start && !filters.date_end"
        class="no-table-data"
      >
        {{ $t('charts.general.no_chart_dates') }}
      </span>
      <span
        v-else-if="!loader.isActive && !balances.length"
        class="no-table-data"
      >
        {{ $t('charts.general.no_chart_data') }}
      </span>
    </b-container>
  </div>
</template>

<script>
  import Formatting from '@base/mixins/Formatting.vue'
  import HeadBlock from '@base/components/HeadBlock.vue'
  import BalancesFilter from '@admin/components/BalancesFilter'
  import BalanceChart from '@admin/components/BalanceChart'
  import { mapState, mapGetters } from 'vuex'


  export default {
    name: 'BalancesView',

    components: {
      BalanceChart,
      HeadBlock,
      BalancesFilter
    },

    mixins: [ Formatting ],

    data () {
      return {
        loader: { isActive: true },
        fields: [
          {
            key: 'id',
            label: this.$t('form.balances.id'),
            class: 'text-center',
          },
          {
            key: 'site',
            label: this.$t('form.balances.site'),
            class: 'text-center',
          },
          {
            key: 'time_indexes_utc',
            label: this.$t('form.balances.time_indexes_utc'),
            class: 'text-center',
          },
          {
            key: 'energy',
            label: this.$t('form.balances.energy'),
            class: 'text-center',
          },
          {
            key: 'date',
            label: this.$t('form.balances.date'),
            class: 'text-center',
          },
          {
            key: 'version',
            label: this.$t('form.balances.version'),
            class: 'text-center',
          },
        ],
        templates: [
          { name: 'date', field: 'date' },
        ],
        showFilter: true,
        filters: null,
        chartType: ['energy'],
      }
    },

    computed: {
      ...mapState(['balances', 'sites',]),
      ...mapGetters(['getFormattedChartsData']),

      checkboxOptions () {
        return [
          {
            text: this.$t('charts.balances.energy'),
            value: 'energy',
            disabled: this.chartType.join('') !== 'energy' && this.chartType.length
          },
          {
            text: this.$t('charts.balances.energy_installed_capacity_ac'),
            value: 'energy_installed_capacity_ac',
            disabled: this.chartType.join('') !== 'energy_installed_capacity_ac' && this.chartType.length
          },
          {
            text: this.$t('charts.balances.energy_installed_capacity_dc'),
            value: 'energy_installed_capacity_dc',
            uncheckedValue: 'energy',
            disabled: this.chartType.join('') !== 'energy_installed_capacity_dc' && this.chartType.length
          },
        ]
      }
    },

    watch: {
      chartType () {
        this.$store.commit(this.$_mutationTypes.SET_CHART_TYPE, this.chartType.join(''))
      }
    },

    methods: {

      clickPaginationCallback (pageNum) {
        this.$store.commit(this.$_mutationTypes.SET_BALANCES_PAGE, pageNum)
        this.getBalances()
      },

      getSites () {
        return new Promise((resolve) => {
          if (this.loading)
            return
          this.loading = true
          this.loader = this.$loading.show(this.$_loaderOptions)
          this.$store.dispatch(this.$_actionTypes.GET_SITES)
            .catch((error) => {
              this.$_notifyError(error, this)
            })
            .finally(() => {
              this.loader.hide()
              this.loading = false
              resolve()
            })
        })
      },

      getBalances () {
        return new Promise((resolve) => {
          if (this.loading)
            return
          this.loading = true
          this.loader = this.$loading.show(this.$_loaderOptions)
          this.$store.dispatch(this.$_actionTypes.GET_BALANCES)
            .then((res) => {
              this.$store.commit(this.$_mutationTypes.SET_BALANCES_PAGES_COUNT, res.total_pages)
            })
            .catch((error) => {
              this.$_notifyError(error, this)
            })
            .finally(() => {
              this.loader.hide()
              this.loading = false
              resolve()
            })
        })
      },

      applyFilters (filters) {
        this.filters = filters
        this.$store.commit(this.$_mutationTypes.SET_BALANCES_FILTERS, filters)
        if (!this.sites.length) {
          this.getSites()
            .then(this.getBalances)
        } else {
          this.getBalances()
        }
      },
    }
  }
</script>

<style>

</style>
