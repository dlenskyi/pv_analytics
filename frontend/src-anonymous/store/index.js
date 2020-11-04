import Vue from 'vue'
import Vuex from 'vuex'

import {
  authUser,
} from '@anonymous/services'

import {
  baseActions,
  baseGetters,
  baseMutations,
  baseState,
  anonRequestInterceptor,
  setToken,
} from '@base/store'

import { actionTypes } from '@base/store/store-types'

Vue.use(Vuex)

const axiosInstances = [
  authUser,
]

for (const instance of axiosInstances) {
  instance.interceptors.request.use(anonRequestInterceptor)
}

const initialState = {
  ...baseState,

}

document.initialState = initialState      // Need in each section stores for base logout user behavior

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


    // eslint-disable-next-line no-unused-vars
    [actionTypes.LOGIN_USER]({ commit }, payloads) {
      return new Promise((resolve, reject) => {
        authUser({
          data: payloads
        })
          .then(response => {
            setToken(response.data)
            resolve(response.data)
          })
          .catch(error => {
            reject(error.response)
          })
      })
    },
  }
})
