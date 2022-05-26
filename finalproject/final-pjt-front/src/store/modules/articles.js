import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    articles: [],
    article: {},
  },

  getters: {
    articles: state => state.articles,
    article: state => state.article,
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username
    },
    isArticle: state => !_.isEmpty(state.article),
  },

  mutations: {
    SET_ARTICLES: (state, articles) => state.articles = articles,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS: (state, comments) => (state.article.comments = comments),
  },

  actions: {
    fetchArticles({ commit }) {
      axios({
        url: drf.articles.articles(),
        method: 'get',
      })
        .then(res => commit('SET_ARTICLES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchArticle({ commit, getters }, articleId) {
      axios({
        url: drf.articles.article(articleId),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ARTICLE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    createArticle({ commit, getters }, article) {     
      axios({
        url: drf.articles.articles(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'article',
            params: { articleId: getters.article.id }
          })
        })
        .catch(() => {
          alert('글을 쓸 수 있는 권한이 없습니다.')
          router.push({ name: 'community' })
        })
    },

    updateArticle({ commit, getters }, { id, title, content, movie_title, }) {
      axios({
        url: drf.articles.article(id),
        method: 'put',
        data: { title, content, movie_title, },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'article',
            params: { articleId: getters.article.id }
          })
        })
    },

    deleteArticle({ commit, getters }, articleId) {      
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.article(articleId),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_ARTICLE', {})
            router.push({ name: 'articles' })
          })
          .catch(err => console.error(err.response))
      }
    },

    likeArticle({ commit, getters }, articleId) {
      axios({
        url: drf.articles.likeArticle(articleId),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ARTICLE', res.data))
        .catch(err => console.error(err.response))
    },

		createComment({ commit, getters }, { articleId, content }) {
      const comment = { content }

      axios({
        url: drf.articles.comments(articleId),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateComment({ commit, getters }, { articleId, commentId, content }) {
      const comment = { content }

      axios({
        url: drf.articles.comment(articleId, commentId),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteComment({ commit, getters }, { articleId, commentId }) {
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.articles.comment(articleId, commentId),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_ARTICLE_COMMENTS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },
  },
}
