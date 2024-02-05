import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

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
      
    } catch (error) {
      
    }
  }else{
    next()
  }
})

export default router
