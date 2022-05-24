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
    <p>users_mymovie: {{ movie.users_mymovie }}</p>
    <p>users_wish: {{ movie.users_wish }}</p>
    
    <!-- Article Edit/Delete UI -->
    <!-- <div v-if="isAuthor"> -->
      <!-- {{ movie.}} -->
      <!-- <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteArticle(articlePk)">Delete</button> -->
    <!-- </div> -->

    <!-- Article Like UI -->
    <!-- <div>
      Likeit:
      <button
        @click="likeArticle(articlePk)"
      >{{ likeCount }}</button>
    </div> -->

    <!-- <hr /> -->
    <!-- Comment UI
    <comment-list :comments="article.comments"></comment-list> -->

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
      ...mapGetters(['movie']),
      // 'isAuthor', 다시 써주기
      // likeCount() {
      //   return this.article.like_users?.length
      // }
    },
    methods: {
      ...mapActions([
        'fetchMovie',
        // 'likeArticle',
      ])
    },
    created() {
      this.fetchMovie(this.movieId)
    },
  }
</script>

<style></style>
