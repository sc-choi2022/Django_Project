<template>
  <div>
    <div class="container">
      <h1>Keyword RECOMMEND</h1>
    </div>
    <div class="container">
      <h2 class="keyword" v-if="keywordId === 9882">Space</h2>
      <h2 class="keyword" v-if="keywordId === 470">Spy</h2>
      <h2 class="keyword" v-if="keywordId === 9840">Romance</h2>
      <h2 class="keyword" v-if="keywordId === 6054">Friendship</h2>
      <h2 class="keyword" v-if="keywordId === 180547">MCU</h2>
      <h2 class="keyword" v-if="keywordId === 4379">Time Travel</h2>
    </div>
    <div class="container container1" v-if="keywordmovies.length">
      <router-link 
        :to="{ name: 'movie', params: {movieId: keywordmovies[0].id} }"><img :src="cardUrl + keywordmovies[0].poster_path" alt="movie_poster">
      </router-link>
      <router-link 
        :to="{ name: 'movie', params: {movieId: keywordmovies[1].id} }"><img :src="cardUrl + keywordmovies[1].poster_path" alt="movie_poster">
      </router-link>
      <router-link 
        :to="{ name: 'movie', params: {movieId: keywordmovies[2].id} }"><img :src="cardUrl + keywordmovies[2].poster_path" alt="movie_poster">
      </router-link>
      <router-link 
        :to="{ name: 'movie', params: {movieId: keywordmovies[3].id} }"><img :src="cardUrl + keywordmovies[3].poster_path" alt="movie_poster">
      </router-link>
      <router-link 
        :to="{ name: 'movie', params: {movieId: keywordmovies[4].id} }"><img :src="cardUrl + keywordmovies[4].poster_path" alt="movie_poster">
      </router-link>
    </div>
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