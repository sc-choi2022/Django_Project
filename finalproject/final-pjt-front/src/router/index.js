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
  // ????????? ?????? ?????? (Vuex ?????? ???)
  const { isLoggedIn } = store.getters
  store.commit('SET_AUTH_ERROR','')

  // Auth??? ???????????? route??? name
  const noAuthPages = ['login', 'signup', 'movies']

  // ?????? ??????????????? ?????? ???????????? Auth??? ?????????????
  const isAuthRequired = !noAuthPages.includes(to.name)

  // Auth??? ????????????, ??????????????? ?????? ??????????
  if (isAuthRequired && !isLoggedIn) {
    alert('???????????? ????????? ??????????????????.')
    // ????????? ???????????? ??????
    next({ name: 'login' , query : { next: to.path }})
  } else {
    // ?????? ??????????????? ????????? ??????
    next()
  }
})

export default router
