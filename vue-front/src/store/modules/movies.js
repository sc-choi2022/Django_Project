import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

// import _ from 'lodash'
// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    movies: [],
    movie: {},
    ottmovies: [],
  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    ottmovies: state => state.ottmovies,
    // isAuthor: (state, getters) => {
    //   return state.movie.user?.username === getters.currentUser.username
    // },
    // isArticle: state => !_.isEmpty(state.article),
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_OTTMOVIES: (state, ottmovies) => state.ottmovies = ottmovies,
  },

  actions: {
    fetchMovies({ commit }) {
      /* 게시글 목록 받아오기
      GET: articles URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.movies(),
        method: 'get',
        // headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchMovie({ commit, getters }, movieId) {
      
      axios({
        url: drf.movies.movie(movieId),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    fetchOttMovies({ commit, getters }, ottId) {
      axios({
        url: drf.movies.otts(ottId),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_OTTMOVIES', res.data))
        .catch(err => console.error(err.response))
    },

    

    myMovie({ commit, getters }, movieId) {
      axios({
        url: drf.movies.myMovie(movieId),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },


    wish({ commit, getters }, movieId) {
      /* 좋아요
      POST: likeArticle URL(token)
        성공하면
          state.article 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.wish(movieId),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },

		
  },
}
