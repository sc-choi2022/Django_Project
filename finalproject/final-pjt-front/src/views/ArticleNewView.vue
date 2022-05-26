<template>
  <div class="container">
    <h1></h1>
    <article-form :article="article" action="create"></article-form>
  </div>
</template>

<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'AritcleNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          id: null,
          title: '',
          content: '',
          movie_title: '',
        }
      }
    },
  }
</script>

<style></style>
