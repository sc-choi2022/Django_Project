import Vue from 'vue'
import VueRouter from 'vue-router'

import MovieListView from '@/views/MovieListView.vue'

import ArticleListView from '@/views/ArticleListView.vue'
import ArticleNewView from '@/views/ArticleNewView'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
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

export default router
