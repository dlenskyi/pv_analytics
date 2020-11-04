import Vue from 'vue'
import VueRouter from 'vue-router'
import {
  DJANGO_ADMIN_PATH_NAME,
  ADMIN_SECTION_PATH,
} from '@base/configs'
import { getToken } from '@base/store'

import NotFoundPage from '@base/components/NotFoundPage.vue'
import BasePage from '@anonymous/views/BasePage.vue'
import Home from '@anonymous/components/Home.vue'

// Redirect user to cabinet if local storage token exists
const checkTokenStorage = (next) => {
  const token = getToken()
  if (token && token.is_admin)
    window.location.replace(ADMIN_SECTION_PATH)
  else
    next()
}

const routes = [
  {
    path: '/404',
    name: 'not-found',
    component: NotFoundPage,
  },
  {
    path: '/',
    component: BasePage,
    redirect: '/login',
    children: [
      {
        path: 'login',
        beforeEnter: (to, from, next) => {
          checkTokenStorage(next)
        },
        name: 'base',
        component: Home,
      },
      {
        path: DJANGO_ADMIN_PATH_NAME,
        beforeEnter:() => {
          location.replace('/' + DJANGO_ADMIN_PATH_NAME)
        }
      },
    ]
  },
  {
    path: '*',
    redirect: { name: 'not-found' }
  }
]

const router = new VueRouter({ mode: 'history', routes })

Vue.use(VueRouter)

export default router
