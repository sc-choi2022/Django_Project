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
    directormovies: [],
    keywordmovies: [],
  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    ottmovies: state => state.ottmovies,
    directormovies: state => state.directormovies,
    keywordmovies: state => state.keywordmovies,
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_OTTMOVIES: (state, ottmovies) => state.ottmovies = ottmovies,
    SET_DIRECTORMOVIES: (state, directormovies) => state.directormovies = directormovies,
    SET_KEYWORDMOVIES: (state, keywordmovies) => state.keywordmovies = keywordmovies,

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
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    fetchDirectorMovies({ commit, getters }, directorId) {
      axios({
        url: drf.movies.directors(directorId),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_DIRECTORMOVIES', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    fetchKeywordMovies({ commit, getters }, keywordId) {
      axios({
        url: drf.movies.keywords(keywordId),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_KEYWORDMOVIES', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
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
