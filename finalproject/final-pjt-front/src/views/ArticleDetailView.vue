<template>
  <div>
    <div class="container">
      <h1>{{ article.title }}</h1>
      <h2> Movie Title: {{ article.movie_title }} </h2>
      <p class="righttext">기사 작성일: {{ article.created_at.substr(0,10) }} 기사 수정일: {{ article.updated_at.substr(0,10) }}</p>

      <p> {{ article.content }} </p>
      
      <!-- Article Edit/Delete UI -->
      <div class="righttext" v-if="isAuthor">
        <router-link :to="{ name: 'articleEdit', params: { articleId } }">
          <button>Edit</button>
        </router-link>
        |
        <button @click="deleteArticle(articleId)">Delete</button>
      </div>

      <!-- Article Like UI -->
      <div>
        Like it<font-awesome-icon icon="fa-solid fa-heart" color="#ff78ae" />:
        <button @click="likeArticle(articleId)">
          {{ likeCount }}
        </button>
      </div>

      <!-- Comment UI -->
      <comment-list :comments="article.comments"></comment-list>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articleId: this.$route.params.articleId,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articleId)
    },
  }
</script>

<style>
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
  .righttext {
    text-align: right;
  }
</style>
