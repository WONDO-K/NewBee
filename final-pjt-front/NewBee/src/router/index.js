import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignupView from '@/views/SignupView.vue'
import LoginView from '@/views/LoginView.vue'
import MyPageView from '@/views/MyPageView.vue'
import BankSearchView from '@/views/BankSearchView.vue'
import FreeBoardView from '@/views/FreeBoardView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/mypage',
      name: 'mypage',
      component: MyPageView,
    },
    {
      path: '/banksearch',
      name: 'banksearch',
      component: BankSearchView,
    },
    {
      path: '/freeboard',
      name: 'freeboard',
      component: FreeBoardView,
    },
    {
      path: '/createarticle',
      name: 'createarticle',
      component: ArticleCreateView,
    }
  ]
})

export default router
