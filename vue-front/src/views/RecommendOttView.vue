<template>
  <div>
    <div class="container">
      <h1>OTT RECOMMEND</h1>
      <h2 class="logo" v-if="ottId === 8">Netflix</h2>
      <h2 class="logo" v-if="ottId === 97">Watcha</h2>
      <h2 class="logo" v-if="ottId === 337">Disney Plus</h2>
    </div>
    <div class="container">
      <img :src="cardUrl + ottmovies[0].poster_path" alt="movie_poster" class="poster-1">
      <img :src="cardUrl + ottmovies[1].poster_path" alt="movie_poster" class="poster-1">
      <img :src="cardUrl + ottmovies[2].poster_path" alt="movie_poster" class="poster-2">
      <img :src="cardUrl + ottmovies[3].poster_path" alt="movie_poster" class="poster-3">
      <img :src="cardUrl + ottmovies[4].poster_path" alt="movie_poster" class="poster-4">
    </div>
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
      }     
    },
    methods: {
      ...mapActions(['fetchOttMovies'])
    },
    created() {
      this.fetchOttMovies(this.ottId)
    },
  }
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing:border-box;
}
body {
  width: 100%;
  height: 100vh;
  background-color:#000;
  
  display:grid;
  place-items:center;
}
img {
  width: 40%;
  height: 100%;
  object-fit:cover;
  
  -webkit-box-reflect:below 2px linear-gradient(transparent, transparent, #0004);
  
  transform-origin:center;
  transform:perspective(800px) rotateY(25deg);
  transition:0.5s;
}
.container {
  max-width:600px;
  max-height:350px;
  
  
  
  display:flex;
  justify-content:center;
  align-items:center;
  gap:20px;
  
}
.container:hover img {
  opacity:0.3;
}
.container img:hover {
  transform:perspective(800px)       rotateY(0deg);
  opacity:1;
}
</style>