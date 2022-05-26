<template>
  <div>
    <div class="container">
      <div>
        <h1>Community</h1>
        <router-link :to="{ name: 'articleNew' }" v-if="isLoggedIn">
          <button v-if="currentUser.email">New</button>
        </router-link>
      </div>
      <div class="articles" v-for="article in articles" :key="article.id">
        [{{ article.movie_title }}]
        {{ currentUser }}
        <!-- username: {{ article.user.username }}  <br> -->
        <router-link 
          :to="{ name: 'article', params: {articleId: article.id} }">
          {{ article.title }}
        </router-link>
        <font-awesome-icon icon="fa-solid fa-heart" color="#ff78ae" />{{ article.like_count }}
        <font-awesome-icon icon="fa-solid fa-feather" color="#808080" />{{ article.comment_count }} <hr>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles', 'isLoggedIn', 'currentUser'])
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style scoped>
  .container {
    padding: 5rem 20rem;
  }
  .articles {
    text-align: left;
  }
  a {
    text-decoration:none;
    color: black;
    font-weight: 800;
  }
</style>
