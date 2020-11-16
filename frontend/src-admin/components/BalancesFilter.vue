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
          <multiselect
            id="site"
            :select-label="$t('multiselect.select_label')"
            :deselect-label="$t('multiselect.deselect_label')"
            :selected-label="$t('multiselect.selected_label')"
            v-model="filterModels.sites"
            :placeholder="$t('multiselect.placeholder', {
              field: $t('form.meter_data.site_name_multiselect').toLowerCase()
            })"
            :searchable="true"
            :multiple="true"
            :close-on-select="false"
            :options="sites">
          </multiselect>
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
  import { mapState } from 'vuex'

  const defaultFilterModels = {
    dateRange: {
      start: null,
      end: null,
    },
    sites: [],
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
      ...mapState(['sites']),

      filterArgs () {
        return {
          date_start: this.filterModels.dateRange.start ? this.filterModels.dateRange.start : undefined,
          date_end: this.filterModels.dateRange.end ? this.filterModels.dateRange.end : undefined,
          site: this.filterModels.sites.length ? this.filterModels.sites : null
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
