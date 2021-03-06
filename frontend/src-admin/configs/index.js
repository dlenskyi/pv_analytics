import { apiConfig } from '@base/configs'
import i18n from "@base/i18n"

export const customerApiUrl = `${apiConfig.baseURL}/customer`

export const NAV_ITEMS = [
  {
    href: { name: 'meter-data' },
    text: i18n.t('navigation.admin.meter_data')
  },
  {
    href: { name: 'balances' },
    text: i18n.t('navigation.admin.balances')
  },
  {
    href: { name: 'settings' },
    text: i18n.t('navigation.general.settings')
  },
  {
    href: '#',
    text: i18n.t('navigation.general.logout')
  }
]
