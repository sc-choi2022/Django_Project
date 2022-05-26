<template>
  <div class="movie-comment-list">
    <div class="container">
      <ul>
        <movie-comment-list-item 
          v-for="review in reviews"
          :review="review" 
          :key="review.id">
        </movie-comment-list-item>        
      </ul>
      <movie-comment-form></movie-comment-form>
    </div>
  </div>
</template>

<script>
import MovieCommentListItem from '@/components/MovieCommentListItem.vue'
import MovieCommentForm from '@/components/MovieCommentForm.vue'

export default {
  name: 'MovieCommentList',
  components: { MovieCommentListItem, MovieCommentForm },
  props: { reviews: Array },
}
</script>

<style>

</style>