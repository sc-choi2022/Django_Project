<template>
  <div>
    <div class="container">
      <h1>Community</h1>
          <router-link :to="{ name: 'articleNew' }" v-if="isLoggedIn">
            <button>New</button>
          </router-link>
      <ul>
        <li v-for="article in articles" :key="article.id">
          <!-- 작성자 -->
          username: {{ article.user.username }}  |
          title: {{ article.title }}  |
          movie_title: {{ article.movie_title }} 

          <!-- 글 이동 링크 (제목) -->
          <router-link 
            :to="{ name: 'article', params: {articleId: article.id} }">
            {{ article.title }}
          </router-link>

          <!-- 댓글 개수/좋아요 개수 -->
          =>
          댓글 개수: {{ article.comment_count }} | 좋아요 개수: {{ article.like_count }}

        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles', 'isLoggedIn'])
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style></style>
