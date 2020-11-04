import axios from 'axios'
import { baseApiConfig } from '@base/configs'

export const authUser = axios.create({
  method: 'post',
  baseURL: `${baseApiConfig.baseURL}/auth/`,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
})
