<template>
  <section>
    <GChart
      type="LineChart"
      :settings="{
        packages: ['corechart', 'table', 'map'],
        language: $_languageCode,
      }"
      :data="balances"
      :options="chartOptions"/>
  </section>
</template>

<script>

  export default {
    name: 'BalanceChart',

    data () {
      return {
        chartData: [],
      }
    },

    props: {
      balances: {
        type: Array,
        required: true
      },
      rangeMin: {
        type: String,
        required: true
      },
      rangeMax: {
        type: String,
        required: true
      },
    },

    computed: {
      formattedChartTitle () {
        return this.$t('charts.balances.title', {
          startDate: this.rangeMin,
          endDate: this.rangeMax,
        })
      },

      chartOptions () {
        return {
          title: this.formattedChartTitle,
          bar: { groupWidth: '75%' },
          legend: { position: 'top' },
          height: 300,
          theme: 'material',
          backgroundColor: 'none',
          explorer: {
            actions: ['dragToZoom', 'rightClickToReset'],
            axis: 'horizontal',
            keepInBounds: true,
            maxZoomIn: 150.0
          },
          hAxis: {
            textStyle:{ color: 'grey', opacity: 0.8 },
            gridlines: { color: 'grey', opacity: 0.6},
            viewWindowMode: 'pretty',
            viewWindow: {
              min: this.minDay,
              max: this.maxDay
            }
          },
          vAxis: {
            textStyle:{ color: 'grey', opacity: 0.8},
            gridlines: { color: 'grey', opacity: 0.6},
            baselineColor: { color: 'grey', opacity: 0.6},
            viewWindowMode: 'pretty',
          },
          'language': this.$_languageCode
        }
      },

      minDay () {
        return new Date(this.rangeMin)
      },
      maxDay () {
        return new Date(this.rangeMax)
      }
    },

    methods: {
    }
  }
</script>

<style>

</style>
