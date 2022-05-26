<template>
  <div>
    <div class="container">
      <div class="moviedetail">
        <div class="movieposter">
          <img :src="cardUrl + movie.poster_path" alt="movie_poster">
        </div>
        <div class="movietext1">
          <h1>{{ movie.title }} 
            <span v-if="movie.certifications[0]['name']='ALL'" style="color:green">{{ movie.certifications[0]['name'] }}
            </span>
          </h1>
          <p>{{ movie.runtime }} min 개봉일 {{ movie.release_date.slice(0,10) }} </p>
          <p>감독 {{ movie.directors[0]['name'] }}</p>
          <p> 
            <span>{{ movie.genres[0].name }} </span> 
            <span v-if="movie.genres.length >= 2">{{ movie.genres[1].name }} </span> 
            <span v-if="movie.genres.length >= 3">{{ movie.genres[2].name }}</span>
          </p>
          <p class="vote">
            <span v-if="1<=movie.vote_average && movie.vote_average<2"><font-awesome-icon icon="fa-solid fa-star-half" /></span>
            <span v-if="2<=movie.vote_average && movie.vote_average<3"><font-awesome-icon icon="fa-solid fa-star" /></span>
            <span v-if="3<=movie.vote_average && movie.vote_average<4"><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star-half" /></span>
            <span v-if="4<=movie.vote_average && movie.vote_average<5"><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /></span>
            <span v-if="5<=movie.vote_average && movie.vote_average<6"><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star-half" /></span>
            <span v-if="6<=movie.vote_average && movie.vote_average<7"><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /></span>
            <span v-if="7<=movie.vote_average && movie.vote_average<8"><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star-half" /></span>
            <span v-if="8<=movie.vote_average && movie.vote_average<9"><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /></span>
            <span v-if="9<=movie.vote_average && movie.vote_average<10"><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star-half" /></span>
          </p>
        </div>
        <div class="video">
          <iframe width="640" height="360" :src="videoUrl+movie.video" frameborder="0"></iframe>
        </div>
        <div class="movietext2">
          <h2>Cast</h2>
        </div>
        <div class="actor0">
          <img :src="cardUrl1 + movie.actors[0].profile_path" alt="actors">
        </div>
        <div class="actor1">
          <img :src="cardUrl1 + movie.actors[1].profile_path" alt="actors">
        </div>
        <div class="actor2">
          <img :src="cardUrl1 + movie.actors[2].profile_path" alt="actors">
        </div>
      </div>

      <!-- MTM field
      <p>certifications: {{ movie.certifications }}</p>
      <p></p>

      user_id 출력된다
      <p>users_mymovie: {{ movie.users_mymovie }}</p>
      <p>users_wish: {{ movie.users_wish }}</p>


      Article Like UI
      <div>
        Mymovie:
        <button
          @click="myMovie(movieId)"
        >myMovie</button>
      </div>

      <div>
        wish:
        <button
          @click="wish(movieId)"
        >wish</button>
      </div> -->

      <movie-comment-list :reviews="movie.reviews"></movie-comment-list>
    </div>  
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import MovieCommentList from '@/components/MovieCommentList.vue'

  export default {
    name: 'MovieDetail',
    components: { MovieCommentList },
    data() {
      return {
        movieId: this.$route.params.movieId,
      }
    },
    computed: {
      ...mapGetters(['movie']),
      cardUrl(){
        return "https://image.tmdb.org/t/p/w400"
      }, 
      cardUrl1(){
        return "https://image.tmdb.org/t/p/w200"
      }, 
      videoUrl(){
        return "https://www.youtube.com/embed/"
      },
    },
    methods: {
      ...mapActions([
        'fetchMovie',
        'myMovie',
        'wish',
      ])
    },
    created() {
      this.fetchMovie(this.movieId)
    },
  }
</script>

<style scoped>
  * { box-sizing: border-box;}
  img {
    object-fit: cover;
  }
  p, h1, h2 {
    font-weight: 800;
  }
  .moviedetail {
    display: grid;
    grid-template-columns: repeat(13, 1fr);
    grid-template-rows: repeat(13, 5vw);
    grid-gap: 10px;
  }
  .movieposter { 
    grid-column-start: 1;
    grid-column-end: 3;
    grid-row-start: 1;
    grid-row-end: 7;
  }
  .movietext1 {
    grid-column-start: 4;
    grid-column-end: 13;
    grid-row-start: 1;
    grid-row-end: 7;    
   }
  .video {
    grid-column-start: 5;
    grid-column-end: 8;
    grid-row-start: 3;
    grid-row-end: 7;  
  }
  .movietext2 {
    grid-column-start: 2;
    grid-column-end: 3;
    grid-row-start: 7;
    grid-row-end: 8;  
  }
  .actor0 {
    grid-column-start: 1;
    grid-column-end: 2;
    grid-row-start: 8;
    grid-row-end: 9;   
  }
  .actor1 {
    grid-column-start: 2.5;
    grid-column-end: 3.5;
    grid-row-start: 8;
    grid-row-end: 9;   
  }
  .actor2 {
    grid-column-start: 3;
    grid-column-end: 4;
    grid-row-start: 8;
    grid-row-end: 9;   
  }
  .actor0 img, .actor1 img, .actor2 img {
    width: 8rem;
    height: 10rem;
    object-fit: cover;
  }
  .vote {
    color: #ffcc00;
  }
</style>