import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export default {
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
    SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.reviews = reviews),
  },

  actions: {
    fetchMovies({ commit }) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
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

    createReview({ commit, getters }, { movieId, content, rank }) {
      
      const comment = { content, rank }

      axios({
        url: drf.movies.reviews(movieId),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateReview({ commit, getters }, { movieId, reviewId, content, rank }) {
      
      const comment = { content, rank }

      axios({
        url: drf.movies.review(movieId, reviewId),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteReview({ commit, getters }, { movieId, reviewId }) {

        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.movies.review(movieId, reviewId),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_MOVIE_REVIEWS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },

		
  },
}
