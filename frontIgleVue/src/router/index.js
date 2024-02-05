import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import axios from 'axios'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      meta: { requireAuth: true },
      component: () => import('../views/DashBoardView.vue')
    }
  ]
})

router.beforeEach(async (to, from, next) => {
  const requireAuth = to.matched.some(url => url.meta.requireAuth)
  if (requireAuth){
    try {
      const token = localStorage.getItem('Token')
      const url = "http://localhost:8000/refresh-token/"
      const {data} = await axios.get(url, {
        headers:{
          Authorization: 'Token' + ' ' + token
        }
      })

      localStorage.setItem('Token', data.token)
      next()
      
    } catch (error) {
      console.log(error.response.data.error)
      next({name: 'login'})
    }
  }else{
    next()
  }
})

export default router
