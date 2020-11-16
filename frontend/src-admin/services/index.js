import axios from 'axios'
import { adminApiConfig } from '@base/configs'


export const initialMeterData = axios.create({
  baseURL: `${adminApiConfig.baseURL}/meter_p30_data/`,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  params: {
    page: null
  }
})


export const correctedMeterData = axios.create({
  baseURL: `${adminApiConfig.baseURL}/corrected_meter_data/`,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
})

export const correctedDataByMeter = axios.create({
  baseURL: `${adminApiConfig.baseURL}/corrected_data_by_meter/`,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
})

export const balances = axios.create({
  baseURL: `${adminApiConfig.baseURL}/balances/`,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  params: {
    page: null
  }
})


export const sites = axios.create({
  baseURL: `${adminApiConfig.baseURL}/sites/`,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
})
