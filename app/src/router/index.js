import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/home.vue'
import Project from '@/router/project'
import Sheet from '@/router/sheet'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    meta: { title: '' },
    component: Home
  },
  ...Project,
  ...Sheet
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
