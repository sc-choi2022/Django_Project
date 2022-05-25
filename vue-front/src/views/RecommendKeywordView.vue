<template>
  <div>
    <p>Keyword</p>
    <li v-for="movie in keywordmovies" :key="movie.id">
      <img :src="cardUrl + movie.poster_path" alt="image">
    </li>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  export default {
    name: 'RecommendKeyword',
    data() {
      return {
        keywordId: this.$route.params.keywordId,
      }
    },
    computed: {
      ...mapGetters([ 'keywordmovies']),
      cardUrl(){
        return "https://image.tmdb.org/t/p/w400"
      },     
    },
    methods: {
      ...mapActions(['fetchKeywordMovies'])
    },
    created() {
      this.fetchKeywordMovies(this.keywordId)
    },
  }
</script>

<style>

</style>