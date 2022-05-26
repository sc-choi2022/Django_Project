<template>
  <div class="container">
    <form @submit.prevent="onSubmit" class="movie-comment-form">
      <label for="review">감상평과 별점을 남겨주세요 :)</label>
      <div><input type="text" id="review" v-model="content" required></div>
      <div class="rating"> 
        <input type="radio" name="rating" value="10" id="5" v-model="rank">
        <label for="5">☆</label> 
        <input type="radio" name="rating" value="8" id="4" v-model="rank">
        <label for="4">☆</label> 
        <input type="radio" name="rating" value="6" id="3" v-model="rank">
        <label for="3">☆</label> 
        <input type="radio" name="rating" value="4" id="2" v-model="rank">
        <label for="2">☆</label> 
        <input type="radio" name="rating" value="2" id="1" v-model="rank">
        <label for="1">☆</label> 
      </div>
      <button>review</button>
    </form>
  </div>
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
  .rating {
  display: flex;
  justify-content: center;
  flex-direction: row-reverse;
  }
  .rating>input {
  display: none
  }
  .rating>label {
  position: relative;
  width: 19px;
  font-size: 25px;
  color: #ff0000;
  cursor: pointer
  }
  .rating>label::before {
  content: "\2605";
  position: absolute;
  opacity: 0
  }
  .rating>label:hover:before,
  .rating>label:hover~label:before {
  opacity: 1 !important
  }
  .rating>input:checked~label:before {
  opacity: 1
  }
  .rating:hover>input:checked~label:before {
  opacity: 0.4
  }
</style>