<template>
  <div>
    <div class="container">
      <div class="articledetail">
        <div class="title padding-bottom--24">{{ article.title }}</div>
        <div class="created_at">{{ article.created_at }}</div>
        <div class="updated_at">{{ article.updated_at }}</div>
        <div class="content">{{ article.content }}</div>
        <div class="movie_title">{{ article.movie_title }}</div>
      </div>
      
      <!-- Article Edit/Delete UI -->
      <div v-if="isAuthor">
        <router-link :to="{ name: 'articleEdit', params: { articleId } }">
          <button>Edit</button>
        </router-link>
        |
        <button @click="deleteArticle(articleId)">Delete</button>
      </div>

      <!-- Article Like UI -->
      <div>
        Likeit:
        <button
          @click="likeArticle(articleId)"
        >{{ likeCount }}</button>
      </div>

      <hr />
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
.padding-bottom--24 {
  padding-bottom: 24px;
}

.container {
    padding: 5rem 15rem;
    background: rgba(128, 128, 128, 0.082);
  }
</style>
