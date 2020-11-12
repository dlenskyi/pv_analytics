import Vue from 'vue'
import Vuex from 'vuex'

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
  correctedDataByMeter
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
}

const axiosInstances = [
  initialMeterData,
  correctedMeterData,
  correctedDataByMeter,
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

  },

  actions: {
    ...baseActions,

    [actionTypes.GET_INITIAL_METER_DATA]({ state, commit }) {
      initialMeterData.defaults.params.page = state.initialMeterDataArg.page
      return new Promise((resolve, reject) => {
        initialMeterData({
          params: state.initialMeterDataArg.filters
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

  }
})
