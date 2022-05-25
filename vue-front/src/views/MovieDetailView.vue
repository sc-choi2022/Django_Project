<template>
  <div>
    <h1>{{ movie.title }}</h1>

    <p>overview: {{ movie.overview }}</p>
    <p>runtime: {{ movie.runtime }}</p>
    <p>release_date: {{ movie.release_date }}</p>
    <p>poster_path: {{ movie.poster_path }}</p>
    <p>video: {{ movie.video }}</p>

    <!-- MTM field -->
    <p>genres: {{ movie.genres }}</p>
    <p>certifications: {{ movie.certifications }}</p>
    <p>directors: {{ movie.directors }}</p>
    <p>actors: {{ movie.actors }}</p>
    <p>otts: {{ movie.otts }}</p>

    <p>vote_count: {{ movie.vote_count }}</p>
    <p>vote_average: {{ movie.vote_average }}</p>

    <!-- user_id 출력된다 -->
    <p>users_mymovie: {{ movie.users_mymovie }}</p>
    <p>users_wish: {{ movie.users_wish }}</p>


    <!-- Article Like UI -->
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
    </div>


  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'MovieDetail',
    data() {
      return {
        movieId: this.$route.params.movieId,
      }
    },
    computed: {
      // 'isAuthor', 
      ...mapGetters(['movie']),
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

<style></style>
