<template>
  <div>
    <div class="container">
      <h1>Director RECOMMEND</h1>
    </div>
    <div class="container">
      <h2 class="keyword" v-if="directorId === 525">Christopher Nolan</h2>
      <h2 class="keyword" v-if="directorId === 21684">Bong Joon-ho</h2>
    </div>
    <div class="container container1" v-if="directormovies.length">
      <router-link 
        :to="{ name: 'movie', params: {movieId: directormovies[0].id} }"><img :src="cardUrl + directormovies[0].poster_path" alt="movie_poster">
      </router-link>
      <router-link 
        :to="{ name: 'movie', params: {movieId: directormovies[1].id} }"><img :src="cardUrl + directormovies[1].poster_path" alt="movie_poster">
      </router-link>
      <router-link 
        :to="{ name: 'movie', params: {movieId: directormovies[2].id} }"><img :src="cardUrl + directormovies[2].poster_path" alt="movie_poster">
      </router-link>
      <router-link 
        :to="{ name: 'movie', params: {movieId: directormovies[3].id} }"><img :src="cardUrl + directormovies[3].poster_path" alt="movie_poster">
      </router-link>
      <router-link 
        :to="{ name: 'movie', params: {movieId: directormovies[4].id} }"><img :src="cardUrl + directormovies[4].poster_path" alt="movie_poster">
      </router-link>
    </div>
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

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing:border-box;
}
body {
  width: 150%;
  height: 100vh;
  background-color:#000;
  
  display:grid;
  place-items:center;
}
img {
  width: 120%;
  height: 100%;
  object-fit:cover;
  
  -webkit-box-reflect:below 2px linear-gradient(transparent, transparent, #0004);
  
  transform-origin:center;
  transform:perspective(800px) rotateY(25deg);
  transition:0.5s;
}
.container1 {
  width: 100%;
  display:flex;
  justify-content:center;
  align-items:center;
  gap:1%;
  
}

.container1:hover img {
  opacity:0.3;
}

.container img:hover {
  transform:perspective(800px) rotateY(0deg);
  opacity:1;
}
</style>