<template>
  <div>
    <div class="container">
      <p class="username">{{ profile.username }}</p>
      <div class="gallery" v-if="profile.movies_mymovie.length">
        <p class="movietype title1">My Movie</p>
        <figure class="gallery_item item0"><router-link 
          :to="{ name: 'movie', params: {movieId: profile.movies_mymovie[0].id} }"><img :src="cardUrl + profile.movies_mymovie[0].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item1"><router-link 
          :to="{ name: 'movie', params: {movieId: profile.movies_mymovie[1].id} }"><img :src="cardUrl + profile.movies_mymovie[1].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item2"><router-link 
          :to="{ name: 'movie', params: {movieId: profile.movies_mymovie[2].id} }"><img :src="cardUrl + profile.movies_mymovie[2].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <p class="movietype title2">Wish Movie</p>
        <figure class="gallery_item item3"><router-link 
          :to="{ name: 'movie', params: {movieId: profile.movies_wish[0].id} }"><img :src="cardUrl + profile.movies_wish[0].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item4"><router-link 
          :to="{ name: 'movie', params: {movieId: profile.movies_wish[1].id} }"><img :src="cardUrl + profile.movies_wish[1].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <figure class="gallery_item item5"><router-link 
          :to="{ name: 'movie', params: {movieId: profile.movies_wish[2].id} }"><img :src="cardUrl + profile.movies_wish[2].poster_path" alt="movie_poster" class="posterimg">
          </router-link>
        </figure>
        <div>
        </div>
      </div>
      <br><br><br>
      <div class="articlediv">
        <p align="left" class="movietype title3">Liked Article</p>
        <p align="left" v-if="profile.like_articles.length">{{ profile.like_articles[profile.like_articles.length-1].title }}</p>
        <p align="left" v-if="profile.like_articles.length >= 2">{{ profile.like_articles[profile.like_articles.length-2].title }}</p>
        <p align="left" v-if="profile.like_articles.length >= 3">{{ profile.like_articles[profile.like_articles.length-3].title }}</p> 
      </div> 
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile']),
    cardUrl(){
      return "https://image.tmdb.org/t/p/w400"
    }, 
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>
<style scoped>
  .container{
    background-image: url("@/assets/Profile_background.png");
    color: rgb(0, 0, 0);
    height: 40rem;
  }
  .container .username {
    font-weight: 800;
    font-size: 100px;
    text-align: left;
    text-decoration: underline overline;
    margin: 0;
    text-shadow: 4px 4px 0px #bdbdbd;
  }
  .container .movietype {
    font-weight: 800;
    font-size: 50px;
    margin: 0;
    /* text-shadow: -1px 0 #bdbdbd, 0 1px #bdbdbd, 1px 0 #bdbdbd, 0 -1px #bdbdbd; */
  }
  .gallery {
    display: grid;
    grid-template-columns: repeat(17, 1fr);
    grid-template-rows: repeat(3, 5vw);
    grid-gap: 15px;
  }
  .title1 {
    grid-column-start: 2;
    grid-column-end: 6;
    grid-row-start: 1;
    grid-row-end: 1;
  }
  .item0 {
    grid-column-start: 2;
    grid-column-end: 4;
    grid-row-start: 2;
    grid-row-end: 5;
  }
  .item1 {
    grid-column-start: 4;
    grid-column-end: 6;
    grid-row-start: 2;
    grid-row-end: 5;
  }
  .item2 {
    grid-column-start: 6;
    grid-column-end: 8;
    grid-row-start: 2;
    grid-row-end: 5;
  }
  .title2 {
    grid-column-start: 9;
    grid-column-end: 14;
    grid-row-start: 1;
    grid-row-end: 1;
  }
  .item3 {
    grid-column-start: 9;
    grid-column-end: 11;
    grid-row-start: 2;
    grid-row-end: 5;
  }
  .item4 {
    grid-column-start: 11;
    grid-column-end: 13;
    grid-row-start: 2;
    grid-row-end: 5;
  }
  .item5 {
    grid-column-start: 13;
    grid-column-end: 15;
    grid-row-start: 2;
    grid-row-end: 5;
  }
  .title3 {
    grid-column-start: 2;
    grid-column-end: 10;
    grid-row-start: 1;
    grid-row-end: 1;
  }
  .article {
    align: "left";
  }
</style>