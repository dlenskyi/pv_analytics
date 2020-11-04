import Cookies from 'js-cookie'

import { webConfig } from '@base/configs'
import {
  changeLanguage,
  logoutUser,
  changePassword,
  getUser,
  updateUser,
} from '@base/services'
import { mutationTypes, actionTypes } from '@base/store/store-types'
import adminStore from '@admin/store'
import { encodedObjectUrl } from '@base/utils'

const setCsrfToken = (config) => {
  const csrfToken = Cookies.get('csrftoken')
  if (csrfToken)
    config.headers.common['X-CSRFTOKEN'] = csrfToken
}

export const setToken = (token) => {
  localStorage.setItem('Token', JSON.stringify(token))
}

export const getToken = () => {
  return JSON.parse(localStorage.getItem('Token')) || null
}

export const cleanStorages = () => {
  localStorage.removeItem('Token')
}

export const baseRequestInterceptor = (config) => {
  setCsrfToken(config)
  return config
}

export const baseResponseFulfilledInterceptor = (response) => {
  return response
}

export const baseResponseRejectedInterceptor = error => {
  if (error.response.status === 401 || error.response.status === 403)
    adminStore.dispatch(actionTypes.LOGOUT)
  return Promise.reject(error)
}

export const adminRequestInterceptor = (config) => {
  setCsrfToken(config)
  return config
}

export const anonRequestInterceptor = (config) => {
  setCsrfToken(config)
  return config
}

export const adminResponseFulfilledInterceptor = (response) => {
  return response
}

export const adminResponseRejectedInterceptor = error => {
  if (error.response.status === 401 || error.response.status === 403)
    adminStore.dispatch(actionTypes.LOGOUT)
  return Promise.reject(error)
}

const axiosInstances = [
  changeLanguage,
  logoutUser,
  changePassword,
  getUser,
  updateUser,
]

for (const instance of axiosInstances) {
  instance.interceptors.request.use(baseRequestInterceptor)
  instance.interceptors.response.use(
    baseResponseFulfilledInterceptor,
    baseResponseRejectedInterceptor
  )
}

export const baseState = {
  showLoader: true,
  user: {
    isAuthenticated: false,
    name: null,
    email: null,
    isSuperuser: null,
  },
}

export const baseGetters = {

}

export const baseMutations = {
  [mutationTypes.SET_LOADER](state, loader) {
    state.showLoader = loader
  },
  [mutationTypes.SET_AUTH](state) {
    state.user.isAuthenticated = true
  },
  [mutationTypes.SET_USER](state, data) {
    state.user.name = data.username
    state.user.email = data.email
    state.user.isSuperuser = data.is_superuser
  },
  // eslint-disable-next-line no-unused-vars
  [mutationTypes.LOGOUT](state) {
    state = document.initialState
    cleanStorages()
    document.location = webConfig.baseURL
  },
}

export const baseActions = {
  [actionTypes.INIT_USER]({ commit, state }) {
    const token = getToken()
    try {
      if (token && !state.user.isAuthenticated) {
        commit(mutationTypes.SET_USER, token)
        commit(mutationTypes.SET_AUTH)
      } else {
        document.location = webConfig.baseURL
        return Promise.reject({
          message: 'No token',
          status: 401,
        })
      }
    } catch (e) {
      document.location = webConfig.baseURL
      return Promise.reject({
        message: 'Invalid token',
        status: 401,
      })
    }
  },

  // eslint-disable-next-line no-unused-vars
  [actionTypes.CHANGE_PASSWORD] ({ commit }, payloads) {
    return new Promise((resolve, reject) => {
      changePassword({
        data: payloads
      })
        .then((response) => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error)
        })
    })
  },

  // eslint-disable-next-line no-unused-vars
  [actionTypes.CHANGE_LANGUAGE]({ commit }, language) {
    // Encode lang data
    const encodedData = encodedObjectUrl(language)
    return new Promise((resolve, reject) => {
      changeLanguage({
        data: encodedData
      })
        .then(response => {
          window.location.reload()
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },

  [actionTypes.LOGOUT]({ commit }) {
    return new Promise((resolve, reject) => {
      logoutUser()
        .then(response => {
          commit(mutationTypes.LOGOUT)
          resolve(response)
        })
        .catch(error => {
          commit(mutationTypes.LOGOUT)
          reject(error)
        })
    })
  },

  [actionTypes.GET_USER]({ commit }) {
    return new Promise((resolve, reject) => {
      getUser()
        .then((response) => {
          commit(mutationTypes.SET_USER, response.data)
          resolve(response.data)
        })
        .catch(error => {
          reject(error)
        })
    })
  },

  [actionTypes.CHANGE_USER] ({commit}, payloads) {
    return new Promise((resolve, reject) => {
      updateUser({
        data: payloads
      })
        .then((response) => {
          commit(mutationTypes.SET_USER, response.data)
          resolve(response.data)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
}
