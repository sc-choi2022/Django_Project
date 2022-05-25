<template>
  <div>
    <p>Director</p>
    <li v-for="movie in directormovies" :key="movie.id">
      <img :src="cardUrl + movie.poster_path" alt="image">
    </li>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  export default {
    name: 'RecommendDirector',
    data() {
      return {
        directorId: this.$route.params.directorId,
      }
    },
    computed: {
      ...mapGetters([ 'directormovies']),
      cardUrl(){
        return "https://image.tmdb.org/t/p/w400"
      },     
    },
    methods: {
      ...mapActions(['fetchDirectorMovies'])
    },
    created() {
      this.fetchDirectorMovies(this.directorId)
    },
  }
</script>

<style>

</style>