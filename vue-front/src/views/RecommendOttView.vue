<template>
  <div>
    <p>Ott</p>
    <li v-for="movie in ottmovies" :key="movie.id">
      <img :src="cardUrl + movie.poster_path" alt="image">
    </li>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  export default {
    name: 'RecommendOtt',
    data() {
      return {
        ottId: this.$route.params.ottId,
      }
    },
    computed: {
      ...mapGetters([ 'ottmovies']),
      cardUrl(){
        return "https://image.tmdb.org/t/p/w400"
      },     
    },
    methods: {
      ...mapActions(['fetchOttMovies'])
    },
    created() {
      this.fetchOttMovies(this.ottId)
    },
  }
</script>

<style>

</style>