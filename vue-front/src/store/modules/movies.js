import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

// import _ from 'lodash'
// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    movies: [],
    movie: {},
  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    // isAuthor: (state, getters) => {
    //   return state.article.user?.username === getters.currentUser.username
    // },
    // isArticle: state => !_.isEmpty(state.article),
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    // SET_ARTICLE_COMMENTS: (state, comments) => (state.article.comments = comments),
  },

  actions: {
    fetchMovies({ commit, getters }) {
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
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },

    // fetchArticle({ commit, getters }, articlePk) {
    //   /* 단일 게시글 받아오기
    //   GET: article URL (token)
    //     성공하면
    //       응답으로 받은 게시글들을 state.articles에 저장
    //     실패하면
    //       단순 에러일 때는
    //         에러 메시지 표시
    //       404 에러일 때는
    //         NotFound404 로 이동
    //   */
    //   axios({
    //     url: drf.articles.article(articlePk),
    //     method: 'get',
    //     headers: getters.authHeader,
    //   })
    //     .then(res => commit('SET_ARTICLE', res.data))
    //     .catch(err => {
    //       console.error(err.response)
    //       if (err.response.status === 404) {
    //         router.push({ name: 'NotFound404' })
    //       }
    //     })
    // },

    

    // likeArticle({ commit, getters }, articlePk) {
    //   /* 좋아요
    //   POST: likeArticle URL(token)
    //     성공하면
    //       state.article 갱신
    //     실패하면
    //       에러 메시지 표시
    //   */
    //   axios({
    //     url: drf.articles.likeArticle(articlePk),
    //     method: 'post',
    //     headers: getters.authHeader,
    //   })
    //     .then(res => commit('SET_ARTICLE', res.data))
    //     .catch(err => console.error(err.response))
    // },

		// createComment({ commit, getters }, { articlePk, content }) {
    //   /* 댓글 생성
    //   POST: comments URL(댓글 입력 정보, token)
    //     성공하면
    //       응답으로 state.article의 comments 갱신
    //     실패하면
    //       에러 메시지 표시
    //   */
    //   const comment = { content }

    //   axios({
    //     url: drf.articles.comments(articlePk),
    //     method: 'post',
    //     data: comment,
    //     headers: getters.authHeader,
    //   })
    //     .then(res => {
    //       commit('SET_ARTICLE_COMMENTS', res.data)
    //     })
    //     .catch(err => console.error(err.response))
    // },

    // updateComment({ commit, getters }, { articlePk, commentPk, content }) {
    //   /* 댓글 수정
    //   PUT: comment URL(댓글 입력 정보, token)
    //     성공하면
    //       응답으로 state.article의 comments 갱신
    //     실패하면
    //       에러 메시지 표시
    //   */
    //   const comment = { content }

    //   axios({
    //     url: drf.articles.comment(articlePk, commentPk),
    //     method: 'put',
    //     data: comment,
    //     headers: getters.authHeader,
    //   })
    //     .then(res => {
    //       commit('SET_ARTICLE_COMMENTS', res.data)
    //     })
    //     .catch(err => console.error(err.response))
    // },

    // deleteComment({ commit, getters }, { articlePk, commentPk }) {
    //   /* 댓글 삭제
    //   사용자가 확인을 받고
    //     DELETE: comment URL (token)
    //       성공하면
    //         응답으로 state.article의 comments 갱신
    //       실패하면
    //         에러 메시지 표시
    //   */
    //     if (confirm('정말 삭제하시겠습니까?')) {
    //       axios({
    //         url: drf.articles.comment(articlePk, commentPk),
    //         method: 'delete',
    //         data: {},
    //         headers: getters.authHeader,
    //       })
    //         .then(res => {
    //           commit('SET_ARTICLE_COMMENTS', res.data)
    //         })
    //         .catch(err => console.error(err.response))
    //     }
    //   },
  },
}
