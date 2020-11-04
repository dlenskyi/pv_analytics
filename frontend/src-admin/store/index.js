import Vue from 'vue'
import Vuex from 'vuex'

import {
  baseState, baseGetters, baseMutations, baseActions,
  adminRequestInterceptor,
  adminResponseFulfilledInterceptor,
  adminResponseRejectedInterceptor,
} from '@base/store'

import {

} from '@admin/services'

Vue.use(Vuex)

const initialState = {
  ...baseState,

}

const axiosInstances = [
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

  },

  mutations: {
    ...baseMutations,

  },

  actions: {
    ...baseActions,

  }
})
