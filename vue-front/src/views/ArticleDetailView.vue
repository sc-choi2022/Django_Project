<template>
  <div>
    <div class="container">
      <h1>{{ article.title }}</h1>

      <p>
        content: {{ article.content }}
      </p>
      <p>
        movie_title: {{ article.movie_title }}
      </p>
      <p>기사 작성일: {{ article.created_at }}</p>
      <p>기사 수정일: {{ article.updated_at }}</p>
      
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

</style>
