import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import MovieListView from '@/views/MovieListView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'

import ArticleListView from '@/views/ArticleListView.vue'
import ArticleNewView from '@/views/ArticleNewView'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleEditView from '@/views/ArticleEditView'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'

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
    component: RecommendView
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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  // 로그인 여부 확인 (Vuex 사용 시)
  const { isLoggedIn } = store.getters

  // Auth가 필요없는 route의 name
  const noAuthPages = ['login', 'signup', 'movies', 'articles']

  // 현재 이동하고자 하는 페이지가 Auth가 필요한가?
  const isAuthRequired = !noAuthPages.includes(to.name)

  // Auth가 필요한데, 로그인되어 있지 않다면?
  if (isAuthRequired && !isLoggedIn) {
    alert('Require Login. Redirecting..')
    // 로그인 페이지로 이동
    next({ name: 'login' })
  } else {
    // 원래 이동하려던 곳으로 이동
    next()
  }
  // 저 위에껄 쓰면 리다이렉트 될 때는 원래 이동하려는 곳으로 가는데 그냥 login시 Home이 아닌 community로 간다 왜지?
  // if (!isAuthRequired && isLoggedIn) {
  //   next({ name: 'movies' })
  // }
})

export default router
