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

export const DEFAULT_DATEPICKER_SHORTCUTS = [
  { key: 'thisWeek', label: i18n.t('datepicker.shortcuts.this_week'), value: 'isoWeek' },
  { key: 'lastWeek', label: i18n.t('datepicker.shortcuts.last_week'), value: '-isoWeek' },
  { key: 'last7Days', label: i18n.t('datepicker.shortcuts.last_7_days'), value: 7 },
  { key: 'last30Days', label: i18n.t('datepicker.shortcuts.last_30_days'), value: 30 },
  { key: 'thisMonth', label: i18n.t('datepicker.shortcuts.this_month'), value: 'month' },
  { key: 'lastMonth', label: i18n.t('datepicker.shortcuts.last_month'), value: '-month' },
  { key: 'thisYear', label: i18n.t('datepicker.shortcuts.this_year'), value: 'year' },
  { key: 'lastYear', label: i18n.t('datepicker.shortcuts.last_year'), value: '-year' }
]

export const ADMIN_SECTION_PATH = '/admin_cabinet#/'
export const DJANGO_ADMIN_PATH_NAME = 'admin/'
