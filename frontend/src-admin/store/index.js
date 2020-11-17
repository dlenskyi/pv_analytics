import Vue from 'vue'
import Vuex from 'vuex'
import _ from 'lodash'
import qs from 'qs'

import {
  baseState, baseGetters, baseMutations, baseActions,
  adminRequestInterceptor,
  adminResponseFulfilledInterceptor,
  adminResponseRejectedInterceptor,
} from '@base/store'
import { actionTypes, mutationTypes } from '@base/store/store-types'

import {
  initialMeterData,
  correctedMeterData,
  correctedDataByMeter,
  balances,
  sites,
} from '@admin/services'

Vue.use(Vuex)

const initialState = {
  ...baseState,
  initialMeterData: [],
  initialMeterDataArg: {
    page: 1,
    pagesCount: 0,
    filters: null
  },
  correctedMeterData: [],
  correctedDataByMeter: [],
  balances: [],
  balancesArg: {
    page: 1,
    pagesCount: 0,
    filters: null
  },
  // There are three chart types: energy,
  // energy_installed_capacity_ac and energy_installed_capacity_dc
  chartType: 'energy',
  sites: [],
}

const axiosInstances = [
  initialMeterData,
  correctedMeterData,
  correctedDataByMeter,
  balances,
  sites,
]

for (const instance of axiosInstances) {
  instance.interceptors.request.use(adminRequestInterceptor)
  instance.interceptors.response.use(
    adminResponseFulfilledInterceptor,
    adminResponseRejectedInterceptor
  )
}

document.initialState = initialState      // Need in each section, stores for base logout user behavior

export default new Vuex.Store({
  state: initialState,
  getters: {
    ...baseGetters,

    getInitialMeterDataPage: state => state.initialMeterDataArg.page,
    getInitialMeterDataPagesCount: state => state.initialMeterDataArg.pagesCount,

    getBalacesPage: state => state.balancesArg.page,
    getBalacesPagesCount: state => state.balancesArg.pagesCount,

    getBalancesBySiteName: (state) => (siteName) => {
      const balanceArray = []
      // Filter balance records by site name, and zip dates
      // and values for that dates
      state.balances.filter(balance => {
        return balance.site === siteName
      }).map(obj => {
        balanceArray.push(..._.zip(obj.time_indexes_utc, obj[state.chartType]))
      })
      // Parse all dates and values for that Site, and return its
      const dates = balanceArray.map(elem => {
        return [new Date(elem[0])]
      })
      const values = balanceArray.map(elem => {
        return elem[1]
      })
      return [dates, values]
    },

    getFormattedChartsData: (state, getters) => {
      // Init formatted array, which we will return, and array for balance
      // values and corresponding site names
      let formattedChartsData = []
      let allBalanceValues = {
        siteNames: [],
        values: []
      }
      state.sites.forEach(function (siteName) {
        const [dates, values] = getters.getBalancesBySiteName(siteName)
        // As each balance object has the same date values (1 hour frequency),
        // we set for our formatted array maximum date range for all charts
        if (dates.length > formattedChartsData.length)
          formattedChartsData = dates
        // If Site has values, then we push values and siteName to our
        // total balance values array
        if (values.length) {
          allBalanceValues.values.push(values)
          allBalanceValues.siteNames.push(siteName)
        }
      })
      // Now we have array of arrays of values (allBalanceValues)
      // Also we have our formatted array with array of arrays of dates
      // Now we need to iterate through all arrays of balance values,
      // inside it go through all dates, and append each new value to
      // corresponding date
      allBalanceValues.values.forEach(valueArray => {
        formattedChartsData.map((elem, index) => {
          elem.push(valueArray[index])
        })
      })
      // Set columns for charts, first goes Date, then site names
      // (we get it from array with values)
      formattedChartsData.unshift(['Date', ...allBalanceValues.siteNames])
      // Return formatted array
      return formattedChartsData
    },

  },

  mutations: {
    ...baseMutations,

    [mutationTypes.SET_INITIAL_METER_DATA](state, data) {
      state.initialMeterData = data
    },
    [mutationTypes.SET_INITIAL_METER_DATA_PAGE] (state, page) {
      state.initialMeterDataArg.page = page
    },
    [mutationTypes.SET_INITIAL_METER_DATA_PAGES_COUNT] (state, count) {
      state.initialMeterDataArg.pagesCount = count
    },
    [mutationTypes.SET_INITIAL_METER_DATA_FILTERS] (state, filters) {
      state.initialMeterDataArg.filters = filters
    },

    [mutationTypes.SET_CORRECTED_METER_DATA](state, data) {
      state.correctedMeterData = data
    },
    [mutationTypes.APPEND_CORRECTED_METER_DATA](state, data) {
      state.correctedMeterData.unshift(data)
    },
    [mutationTypes.REMOVE_CORRECTED_DATA_BY_METER](state, id) {
      const oldDataIndex = state.correctedDataByMeter.findIndex(obj => obj.id === id)
      if (oldDataIndex >= 0) {
        state.correctedDataByMeter.splice(oldDataIndex, 1)
      }
    },

    [mutationTypes.SET_CORRECTED_DATA_BY_METER](state, data) {
      state.correctedDataByMeter = data
    },

    [mutationTypes.SET_BALANCES](state, data) {
      state.balances = data
    },
    [mutationTypes.SET_BALANCES_PAGE] (state, page) {
      state.balancesArg.page = page
    },
    [mutationTypes.SET_BALANCES_PAGES_COUNT] (state, count) {
      state.balancesArg.pagesCount = count
    },
    [mutationTypes.SET_BALANCES_FILTERS] (state, filters) {
      state.balancesArg.filters = filters
    },

    [mutationTypes.SET_SITES](state, data) {
      state.sites = data
    },
    [mutationTypes.SET_CHART_TYPE](state, type) {
      state.chartType = type
    },

  },

  actions: {
    ...baseActions,

    [actionTypes.GET_INITIAL_METER_DATA]({ state, commit }) {
      initialMeterData.defaults.params.page = state.initialMeterDataArg.page
      return new Promise((resolve, reject) => {
        initialMeterData({
          params: state.initialMeterDataArg.filters,
          // for filtering by multiple site names
          paramsSerializer: function(params) {
            return qs.stringify(params, { indices: false })
          }
        })
          .then(response => {
            commit(mutationTypes.SET_INITIAL_METER_DATA, response.data.results)
            resolve(response.data)
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

    [actionTypes.GET_CORRECTED_METER_DATA]({ commit }) {
      return new Promise((resolve, reject) => {
        correctedMeterData()
          .then(response => {
            commit(mutationTypes.SET_CORRECTED_METER_DATA, response.data)
            resolve(response.data)
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

    [actionTypes.CREATE_CORRECTED_METER_DATA]({ commit }, payloads) {
      return new Promise((resolve, reject) => {
        correctedMeterData({
          method: 'post',
          data: payloads
        })
          .then(response => {
            commit(mutationTypes.APPEND_CORRECTED_METER_DATA, response.data)
            resolve(response.data)
          })
          .catch((error) => {
            reject(error)
          })
      })
    },
    [actionTypes.DELETE_CORRECTED_METER_DATA]({ commit }, id) {
      return new Promise((resolve, reject) => {
        correctedMeterData({
          url: `${id}/`,
          method: 'delete'
        })
          .then(response => {
            commit(mutationTypes.REMOVE_CORRECTED_DATA_BY_METER, id)
            resolve(response.data)
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

    [actionTypes.GET_CORRECTED_DATA_BY_METER]({ commit }, meterId) {
      return new Promise((resolve, reject) => {
        correctedDataByMeter({
          url: `${meterId}/`
        })
          .then(response => {
            commit(mutationTypes.SET_CORRECTED_DATA_BY_METER, response.data)
            resolve(response.data)
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

    [actionTypes.GET_BALANCES]({ state, commit }) {
      balances.defaults.params.page = state.balancesArg.page
      return new Promise((resolve, reject) => {
        balances({
          params: state.balancesArg.filters,
          // for filtering by multiple site names
          paramsSerializer: function(params) {
            return qs.stringify(params, { indices: false })
          }
        })
          .then(response => {
            commit(mutationTypes.SET_BALANCES, response.data)
            resolve(response.data)
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

    [actionTypes.GET_SITES]({ commit }) {
      return new Promise((resolve, reject) => {
        sites()
          .then(response => {
            commit(mutationTypes.SET_SITES, response.data)
            resolve(response.data)
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

  }
})
