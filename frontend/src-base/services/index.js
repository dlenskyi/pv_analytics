import axios from 'axios'
import { webConfig, baseApiConfig } from '@base/configs'

// Language

export const changeLanguage = axios.create({
  method: 'post',
  baseURL: `${webConfig.baseURL}/i18n/setlang/`,
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
  },
})

export const logoutUser = axios.create({
  method: 'post',
  baseURL: `${baseApiConfig.baseURL}/logout/`,
  headers: { 'Accept': 'application/json' },
})

export const changePassword = axios.create({
  method: 'post',
  baseURL: `${baseApiConfig.baseURL}/password/change/`,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
})


export const getUser = axios.create({
  method: 'get',
  baseURL: `${baseApiConfig.baseURL}/user/`,
  headers: { 'Accept': 'application/json' },
})

export const updateUser = axios.create({
  method: 'patch',
  baseURL: `${baseApiConfig.baseURL}/user/`,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
})
