<template>
  <div>
    <h2>{{ $t('filter.title') }}</h2>

    <b-form @submit.prevent="sendFilteredQuery">

      <div class="d-flex">
        <!--DATE RANGE-->
        <b-form-group
          id="date-group"
          class="mr-4 w-100 mh-100"
          :label="$t('filter.by.meter_data.date')"
          :invalid-feedback="invalidDateRange"
          :state="stateDateRange"
          label-for="date"
        >
          <VueCtkDateTimePicker
            id="date"
            :custom-shortcuts="defaultDatepickerShortcuts"
            v-model="filterModels.dateRange"
            @input="datePickerInput"
            @is-hidden="applyDateRange"
            :autoClose="true"
            :hint="$t('pages.meter_data.date_hint')"
            :locale="$_languageCode"
            :format="dateFormat"
            :formatted="dateFormat"
            outputFormat="YYYY-MM-DD"
            :range="true"
          >
          </VueCtkDateTimePicker>
        </b-form-group>

        <!--SITE-->
        <b-form-group
          id="site-group"
          class="w-100 mh-100"
          :label="$t('filter.by.meter_data.site')"
          label-for="site"
        >
          <b-form-input
            id="site"
            style="height: 42px;"
            v-model="filterModels.site"
            :placeholder="$t('form.meter_data.site_name')"
          ></b-form-input>
        </b-form-group>
      </div>

      <div class="d-flex justify-content-end">
        <b-button
          class="mb-2"
          @click="clearAllFilters"
          variant="primary">
          <b-icon icon="arrow-repeat"></b-icon>
          {{ $t('filter.reset_button') }}
        </b-button>
        <b-button
          class="mb-2 ml-3"
          type="submit"
          variant="success">
          <b-icon icon="check"></b-icon>
          {{ $t('filter.apply_button') }}
        </b-button>
      </div>

    </b-form>
  </div>
</template>

<script>

  import { DATE_FORMAT, DEFAULT_DATEPICKER_SHORTCUTS } from '@base/configs'
  import moment from 'moment'

  const defaultFilterModels = {
    dateRange: {
      start: null,
      end: null,
    },
    site: '',
  }

  export default {
    name: 'BalancesFilter',

    data () {
      return {
        filterModels: {
          ...defaultFilterModels,
          dateRange: {
            // Start of last week
            start: moment().subtract(1, 'weeks').startOf('week').format('YYYY-MM-DD'),
            // Current day
            end: moment().format('YYYY-MM-DD'),
          },
        },
        defaultDatepickerShortcuts: DEFAULT_DATEPICKER_SHORTCUTS,
        dateFormat: DATE_FORMAT,
        invalidDateRange: null,
      }
    },

    watch: {
      'filterModels.dateRange' () {
        this.invalidDateRange = null
      }
    },

    created () {
      this.sendFilteredQuery()
    },

    computed: {

      filterArgs () {
        return {
          date_start: this.filterModels.dateRange.start ? this.filterModels.dateRange.start : undefined,
          date_end: this.filterModels.dateRange.end ? this.filterModels.dateRange.end : undefined,
          site: this.filterModels.site ? this.filterModels.site : null
        }
      },

      isDateRangeValid () {
        if (!this.filterModels.dateRange)
          return false
        if (!this.filterModels.dateRange.start && !this.filterModels.dateRange.end)
          return true
        return this.filterModels.dateRange.start && this.filterModels.dateRange.end
      },
      stateDateRange () {
        return (this.invalidDateRange === null)
      },
    },

    methods: {
      clearAllFilters () {
        this.filterModels = {...defaultFilterModels}
        this.$emit('filter-applied', this.filterArgs)
      },
      sendFilteredQuery () {
        if (!this.isDateRangeValid) {
          this.invalidDateRange = this.$t('validation.date_range')
          return
        }
        this.$emit('filter-applied', this.filterArgs)
      },

      applyDateRange () {
        this.$nextTick(this.sendFilteredQuery)
      },

      datePickerInput (value) {
        if (!value)
          this.clearAllFilters()
      },

    }
  }
</script>

<style scoped>

</style>
