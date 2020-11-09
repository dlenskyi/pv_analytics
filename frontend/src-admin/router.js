import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@admin/store'
import VueRouterMiddleware, { createMiddleware, middleware } from 'vue-router-middleware'

import { actionTypes } from '@base/store/store-types'
import { getToken } from '@base/store'
import NotFoundPage from '@base/components/NotFoundPage.vue'
import SettingsView from '@base/views/SettingsView.vue'
import BasePage from '@admin/views/BasePage.vue'
import MeterDataView from '@admin/views/MeterDataView.vue'
import CorrectionDataView from '@admin/views/CorrectionDataView.vue'

createMiddleware('require-auth', (args, to, from, next) => {
  if (!store.state.user.isAuthenticated) {
    store.dispatch(actionTypes.INIT_USER)
      .then(() => {
        if (!store.state.user.isAuthenticated) {
          store.dispatch(actionTypes.LOGOUT)
        } else {
          const token = getToken()
          if (!token) {
            store.dispatch(actionTypes.LOGOUT)
            return
          }
          next()
        }
      })
      .catch((error) => {
        if (error.response.status === 401 ||
                    !store.state.user.isAuthenticated) {
          store.dispatch(actionTypes.LOGOUT)
        } else {
          next()
        }
      })
  } else {
    next()
  }
})

const routes = [
  ...middleware('require-auth', [{
    path: '/',
    name: 'base',
    redirect: 'meter_data',
    component: BasePage,
    children: [
      {
        path: 'meter_data',
        name: 'meter-data',
        component: MeterDataView,
      },
      {
        path: 'corrected_data/:meterDataId',
        name: 'corrected-data',
        component: CorrectionDataView,
      },
      {
        path: 'settings',
        name: 'settings',
        component: SettingsView,
      },
    ]
  },
  ]),
  {
    path: '/404',
    name: 'not-found',
    component: NotFoundPage,
  },
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({ routes })


Vue.use(VueRouter)
Vue.use(VueRouterMiddleware, { router })

export default router
