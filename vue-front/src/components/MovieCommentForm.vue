<template>
  <form @submit.prevent="onSubmit" class="movie-comment-form">
    <label for="review">review: </label>
    <input type="text" id="review" v-model="content" required>
    <input type="number" id="rank" v-model="rank" required>
    <button>review</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieCommentForm',
  data() {
    return {
      content: '',
      rank: 10,
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ movieId: this.movie.id, content: this.content, rank: this.rank })
      this.content = ''
      this.rank = 0
    }
  }
}
</script>

<style>
/* .comment-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
} */
</style>