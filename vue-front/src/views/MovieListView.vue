<template>
  <div>
    <!-- <div><h1>Home</h1></div><hr> -->
    <div class="container">
      <div class="gallery" v-if="movies.length">       
        <figure class="gallery_item item0"><router-link 
          :to="{ name: 'movie', params: {movieId: movies[0].id} }"><img :src="cardUrl + movies[0].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item1"><router-link 
          :to="{ name: 'movie', params: {movieId: movies[1].id} }"><img :src="cardUrl + movies[1].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item2"><router-link 
          :to="{ name: 'movie', params: {movieId: movies[2].id} }"><img :src="cardUrl + movies[2].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item3"><router-link 
          :to="{ name: 'movie', params: {movieId: movies[3].id} }"><img :src="cardUrl + movies[3].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item4"><router-link 
          :to="{ name: 'movie', params: {movieId: movies[4].id} }"><img :src="cardUrl + movies[4].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item5"><router-link 
          :to="{ name: 'movie', params: {movieId: movies[5].id} }"><img :src="cardUrl + movies[5].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item6"><router-link 
          :to="{ name: 'movie', params: {movieId: movies[6].id} }"><img :src="cardUrl + movies[6].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item7"><router-link 
          :to="{ name: 'movie', params: {movieId: movies[7].id} }"><img :src="cardUrl + movies[7].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item8"><router-link 
          :to="{ name: 'movie', params: {movieId: movies[8].id} }"><img :src="cardUrl + movies[8].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item9"><router-link 
          :to="{ name: 'movie', params: {movieId: movies[9].id} }"><img :src="cardUrl + movies[9].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  export default {
    name: 'MovieList',
    computed: {
      ...mapGetters(['movies']),
      cardUrl(){
        return "https://image.tmdb.org/t/p/w400"
      },     
    },
    methods: {
      ...mapActions(['fetchMovies'])
    },
    created() {
      this.fetchMovies()
      console.log(this.movies)
    },
  }
</script>

<style>
.gallery {
    display: grid;
    grid-template-columns: repeat(9, 1fr);
    grid-template-rows: repeat(7, 5vw);
    grid-gap: 15px;
}
.posterimg {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
#app > div:nth-child(2) > div > div > figure.gallery_item > a {
  margin-left: 0;
  padding-left: 0;
}
.item0 {
    grid-column-start: 1;
    grid-column-end: 3;
    grid-row-start: 1;
    grid-row-end: 8;
}
.item1 {
    grid-column-start: 3;
    grid-column-end: 5;
    grid-row-start: 1;
    grid-row-end: 5;
}
.item2 {
    grid-column-start: 3;
    grid-column-end: 5;
    grid-row-start: 5;
    grid-row-end: 8;
}
.item3 {
    grid-column-start: 5;
    grid-column-end: 6;
    grid-row-start: 1;
    grid-row-end: 4;
}
.item4 {
    grid-column-start: 5;
    grid-column-end: 7;
    grid-row-start: 4;
    grid-row-end: 8;
}
.item5 {
    grid-column-start: 6;
    grid-column-end: 8;
    grid-row-start: 1;
    grid-row-end: 4;
}
.item6 {
    grid-column-start: 7;
    grid-column-end: 8;
    grid-row-start: 4;
    grid-row-end: 8;
}
.item7 {
    grid-column-start: 8;
    grid-column-end: 10;
    grid-row-start: 1;
    grid-row-end: 3;
}
.item8 {
    grid-column-start: 8;
    grid-column-end: 10;
    grid-row-start: 3;
    grid-row-end: 6;
}
.item9 {
    grid-column-start: 8;
    grid-column-end: 10;
    grid-row-start: 6;
    grid-row-end: 8;
}
</style>