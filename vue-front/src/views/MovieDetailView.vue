<template>
  <div>
    <div class="container">
      <div class="moviedetail">
        <div class="movieposter">
          <img :src="cardUrl + movie.poster_path" alt="movie_poster">
        </div>
        <div class="movietext1">
          <h1>{{ movie.title }}</h1>
          <p>{{ movie.runtime }} min 개봉일 {{ movie.release_date }} </p>
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
        <div class="movietext3">
          {{ movie.overview }}
        </div>
        <div class="otts" v-if="movie.otts.length === 1">
          <span v-if="movie.otts[0]['id'] === 8">
            <a href="https://www.netflix.com/kr/">
            <img class="thumnail" src="https://w.namu.la/s/08cf9640d5b9e25e2901375f21e3794c9f79e0c4930c5f697cacca22ec454184e410ad955dd997cccaf7e15ad0d7ee8d8976fe767505159c90513b78764543bec07bc8a4b9cf87217ebcb1db11d0ba81db10fe022311d293ed443336b28508c4" alt=""></a>
          </span>
          <span v-if="movie.otts[0]['id'] === 97">
            <a href="https://watcha.com/">
            <img class="thumnail" src="https://w.namu.la/s/806795f01bfdb99ee07ef5ed4d26c7a76ce99bddf229f51418d040f4387944e4e06d19bcbd84da2a179de6273e3ca30f084aabc97154fb91a2f167ee349cec6d6e3c4db1abb00949ce2523d61074442a389fffadb69a3030b85c5168be94f968" alt=""></a>
          </span>
          <span v-if="movie.otts[0]['id'] === 337">
            <a href="https://www.disneyplus.com/ko-kr/welcome/stream-now">
            <img class="thumnail" src="https://w.namu.la/s/e53fcef546cc1b3f510694f331690215c764c0672c35dd34d207f29ed51c38de36e9f57e5bdd2ee05df77b4c1731d4ce840d3990860b959d27dc073339f94f0705d5bb2a4295a17b8911c5f6d31384752c47dedbd5d7f51bfec4db459a7e6f4b" alt=""></a>
          </span>
        </div>
        <div class="otts" v-if="movie.otts.length === 2">
          <span v-if="movie.otts[0]['id'] === 8">
            <a href="https://www.netflix.com/kr/">
            <img class="thumnail" src="https://w.namu.la/s/08cf9640d5b9e25e2901375f21e3794c9f79e0c4930c5f697cacca22ec454184e410ad955dd997cccaf7e15ad0d7ee8d8976fe767505159c90513b78764543bec07bc8a4b9cf87217ebcb1db11d0ba81db10fe022311d293ed443336b28508c4" alt=""></a>
          </span>
          <span v-if="movie.otts[0]['id'] === 97">
            <a href="https://watcha.com/">
            <img class="thumnail" src="https://w.namu.la/s/806795f01bfdb99ee07ef5ed4d26c7a76ce99bddf229f51418d040f4387944e4e06d19bcbd84da2a179de6273e3ca30f084aabc97154fb91a2f167ee349cec6d6e3c4db1abb00949ce2523d61074442a389fffadb69a3030b85c5168be94f968" alt=""></a>
          </span>
          <span v-if="movie.otts[0]['id'] === 337">
            <a href="https://www.disneyplus.com/ko-kr/welcome/stream-now">
            <img class="thumnail" src="https://w.namu.la/s/e53fcef546cc1b3f510694f331690215c764c0672c35dd34d207f29ed51c38de36e9f57e5bdd2ee05df77b4c1731d4ce840d3990860b959d27dc073339f94f0705d5bb2a4295a17b8911c5f6d31384752c47dedbd5d7f51bfec4db459a7e6f4b" alt=""></a>
          </span>
          <span v-if="movie.otts[1]['id'] === 8">
            <a href="https://www.netflix.com/kr/">
            <img class="thumnail" src="https://w.namu.la/s/08cf9640d5b9e25e2901375f21e3794c9f79e0c4930c5f697cacca22ec454184e410ad955dd997cccaf7e15ad0d7ee8d8976fe767505159c90513b78764543bec07bc8a4b9cf87217ebcb1db11d0ba81db10fe022311d293ed443336b28508c4" alt=""></a>
          </span>
          <span v-if="movie.otts[1]['id'] === 97">
            <a href="https://watcha.com/">
            <img class="thumnail" src="https://w.namu.la/s/806795f01bfdb99ee07ef5ed4d26c7a76ce99bddf229f51418d040f4387944e4e06d19bcbd84da2a179de6273e3ca30f084aabc97154fb91a2f167ee349cec6d6e3c4db1abb00949ce2523d61074442a389fffadb69a3030b85c5168be94f968" alt=""></a>
          </span>
          <span v-if="movie.otts[1]['id'] === 337">
            <a href="https://www.disneyplus.com/ko-kr/welcome/stream-now">
            <img class="thumnail" src="https://w.namu.la/s/e53fcef546cc1b3f510694f331690215c764c0672c35dd34d207f29ed51c38de36e9f57e5bdd2ee05df77b4c1731d4ce840d3990860b959d27dc073339f94f0705d5bb2a4295a17b8911c5f6d31384752c47dedbd5d7f51bfec4db459a7e6f4b" alt=""></a>
          </span>
        </div>
        <div class="otts" v-if="movie.otts.length === 3">
          <span>
            <a href="https://www.netflix.com/kr/">
            <img class="thumnail" src="https://w.namu.la/s/08cf9640d5b9e25e2901375f21e3794c9f79e0c4930c5f697cacca22ec454184e410ad955dd997cccaf7e15ad0d7ee8d8976fe767505159c90513b78764543bec07bc8a4b9cf87217ebcb1db11d0ba81db10fe022311d293ed443336b28508c4" alt=""></a>
          </span>
          <span>
            <a href="https://watcha.com/">
            <img class="thumnail" src="https://w.namu.la/s/806795f01bfdb99ee07ef5ed4d26c7a76ce99bddf229f51418d040f4387944e4e06d19bcbd84da2a179de6273e3ca30f084aabc97154fb91a2f167ee349cec6d6e3c4db1abb00949ce2523d61074442a389fffadb69a3030b85c5168be94f968" alt=""></a>
          </span>
          <span>
            <a href="https://www.disneyplus.com/ko-kr/welcome/stream-now">
            <img class="thumnail" src="https://w.namu.la/s/e53fcef546cc1b3f510694f331690215c764c0672c35dd34d207f29ed51c38de36e9f57e5bdd2ee05df77b4c1731d4ce840d3990860b959d27dc073339f94f0705d5bb2a4295a17b8911c5f6d31384752c47dedbd5d7f51bfec4db459a7e6f4b" alt=""></a>
          </span>
        </div>
        <div class="personalmovie">
          <h4>이 영화를 관람한 사람 {{ movie.users_mymovie.length }}</h4>
          <h4>이 영화를 표시한 사람 {{ movie.users_wish.length }}</h4>
        </div>
        <div class="personalicon">
          <h3 @click="myMovie(movieId)"><font-awesome-icon icon="fa-solid fa-person" /></h3>
          <h3 @click="wish(movieId)"><font-awesome-icon icon="fa-solid fa-face-grin-stars" /></h3>
        </div>
        <div class="comments">
          <movie-comment-list :reviews="movie.reviews"></movie-comment-list>
        </div>
      </div>
        
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
  .movietext3{
    text-align: left;
    grid-column-start: 5;
    grid-column-end: 13;
    grid-row-start: 8;
    grid-row-end: 9;     
  }
  .thumnail {
    border-radius: 4px;  /* Rounded border */
    padding: 5px; /* Some padding */
    height: 5rem;
  }
  .otts{
    text-align: right;
    grid-column-start: 5;
    grid-column-end: 12;
    grid-row-start: 10;
    grid-row-end: 13;   
  }
  .personalmovie{
    text-align: left;
    grid-column-start: 5;
    grid-column-end: 10;
    grid-row-start: 7;
    grid-row-end: 8;    
  }
  .personalicon{
    color: #ffcc00;
    text-align: left;
    grid-column-start: 8;
    grid-column-end: 10;
    grid-row-start: 7;
    grid-row-end: 8;    
  }
  .comments{
    text-align: left;
    grid-column-start: 1;
    grid-column-end: 4;
    grid-row-start: 9;
    grid-row-end: 11;    
  }
</style>