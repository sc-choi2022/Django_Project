<template>
  <div>
    <div class="container">
      <div class="board">
        <div>
          <h1>Community</h1>
          <router-link :to="{ name: 'articleNew' }" v-if="isLoggedIn">
            <button v-if="currentUser.email">New</button>
          </router-link>
        </div>
        <br>
        <div class="articles">
          <div class="article" v-for="article in articles" :key="article.id">
            [{{ article.movie_title }}]
            <router-link 
              :to="{ name: 'article', params: {articleId: article.id} }">
              {{ article.title }}
            </router-link>
            <font-awesome-icon icon="fa-solid fa-heart" color="#ff78ae" />{{ article.like_count }}
            <font-awesome-icon icon="fa-solid fa-feather" color="#808080" />{{ article.comment_count }} <br><br>
          </div>
        </div>
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
    padding: 5rem 15rem;
    background: rgba(128, 128, 128, 0.082);
  }
  .article {
    text-align: left;
  }
  .board {
    background: white;
        padding: 10px;
  }
  a {
    text-decoration:none;
    color: black;
    font-weight: 800;
  }
  hr {
    border: 0;
  }
  button {
    border: 0;
    outline: 0;
  }
</style>
