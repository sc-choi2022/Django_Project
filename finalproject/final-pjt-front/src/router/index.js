import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import MovieListView from '@/views/MovieListView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import RecommendListView from '@/views/RecommendListView.vue'
import RecommendOttView from '@/views/RecommendOttView.vue'
import RecommendDirectorView from '@/views/RecommendDirectorView.vue'
import RecommendKeywordView from '@/views/RecommendKeywordView.vue'

import ArticleListView from '@/views/ArticleListView.vue'
import ArticleNewView from '@/views/ArticleNewView'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleEditView from '@/views/ArticleEditView'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import NotFound404 from '@/views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  // accounts
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
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
  },
  
  // movies
  {
    path: '/',  // Home
    name: 'movies',
    component: MovieListView
  },
  {
    path: '/movie/:movieId',
    name: 'movie',
    component: MovieDetailView
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: RecommendListView
  },
  {
    path: '/recommend/ott/:ottId',
    name: 'recommendOtt',
    component: RecommendOttView
  },
  {
    path: '/recommend/director/:directorId',
    name: 'recommendDirector',
    component: RecommendDirectorView
  },
  {
    path: '/recommend/keyword/:keywordId',
    name: 'recommendKeyword',
    component: RecommendKeywordView
  },
  
  // community
  {
    path: '/community',
    name: 'articles',
    component: ArticleListView
  },
  {
    path: '/community/articles/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/community/articles/:articleId',
    name: 'article',
    component: ArticleDetailView
  },
  {
    path: '/community/articles/:articleId/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  // 로그인 여부 확인 (Vuex 사용 시)
  const { isLoggedIn } = store.getters
  store.commit('SET_AUTH_ERROR','')

  // Auth가 필요없는 route의 name
  const noAuthPages = ['login', 'signup', 'movies']

  // 현재 이동하고자 하는 페이지가 Auth가 필요한가?
  const isAuthRequired = !noAuthPages.includes(to.name)

  // Auth가 필요한데, 로그인되어 있지 않다면?
  if (isAuthRequired && !isLoggedIn) {
    alert('로그인이 필요한 페이지입니다.')
    // 로그인 페이지로 이동
    next({ name: 'login' , query : { next: to.path }})
  } else {
    // 원래 이동하려던 곳으로 이동
    next()
  }
})

export default router
