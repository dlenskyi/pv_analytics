import i18n from '@base/i18n'

export const host = process.env.NODE_ENV === 'production' ? process.env.VUE_APP_DOMAIN : 'localhost:8000'

export const webConfig = {
  baseURL: process.env.NODE_ENV === 'production' ? `https://${host}` : `http://${host}`,
}

export const apiConfig = {
  baseURL: `${webConfig.baseURL}/api/v1`
}

export const adminApiConfig = {
  baseURL: `${apiConfig.baseURL}/admin`
}

export const baseApiConfig = {
  baseURL: `${apiConfig.baseURL}/base`
}

export const loaderOptions = {
  color: '#4b8bff',
  backgroundColor: '#000',
  opacity: 0.1
}

// Field length settings
export const MIN_NAME_FIELD_LENGTH = 4
export const MAX_NAME_FIELD_LENGTH = 20
export const MIN_USERNAME_LENGTH = 4
export const MAX_USERNAME_LENGTH = 20
export const MIN_PASSWORD_LENGTH = 8

export const METER_QUANTITY = 50

export const BOOLEAN_OPTIONS = [
  { value: true, name: i18n.t('multiselect.single_label.boolean.true') },
  { value: false, name: i18n.t('multiselect.single_label.boolean.false') }
]

export const DATE_FORMAT = 'DD-MM-YYYY'

export const ADMIN_SECTION_PATH = '/admin_cabinet#/'
export const DJANGO_ADMIN_PATH_NAME = 'admin/'
