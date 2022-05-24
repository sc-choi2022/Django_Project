import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store'

import MovieListView from '@/views/MovieListView.vue'

import ArticleListView from '@/views/ArticleListView.vue'
import ArticleNewView from '@/views/ArticleNewView'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'

Vue.use(VueRouter)

const routes = [
  // 인증 필요 없음
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/',  // Home
    name: 'movies',
    component: MovieListView
  },
  {
    path: '/community',  // Home
    name: 'articles',
    component: ArticleListView
  },
  // 인증 필요함
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/community/articles/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  // {
  //   path: '/articles/:articlePk',
  //   name: 'article',
  //   component: ArticleDetailView
  // },
  // {
  //   path: '/articles/:articlePk/edit',
  //   name: 'articleEdit',
  //   component: ArticleEditView
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {
//   // 로그인 여부 확인 (Vuex 사용 시)
//   const { isLoggedIn } = store.getters

//   // Auth가 필요한 route의 name
//   const noAuthPages = ['articleNew']

//   // 현재 이동하고자 하는 페이지가 Auth가 필요한가?
//   const isAuthRequired = !noAuthPages.includes(to.name)

//   // Auth가 필요한데, 로그인되어 있지 않다면?
//   if (isAuthRequired && !isLoggedIn) {
//     alert('Require Login. Redirecting..')
//     // 로그인 페이지로 이동
//     next({ name: 'login' })
//   } else {
//     // 원래 이동하려던 곳으로 이동
//     next()
//   }
// })

export default router
