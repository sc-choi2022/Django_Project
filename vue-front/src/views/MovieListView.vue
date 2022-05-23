<template>
  <div>
    <h1>Home</h1>
    <ul>
      <li v-for="movie in movies" :key="movie.pk">
        {{ movie }}
        <hr>
        {{ movie.title }}
        {{ movie.poster_path }}
        {{ movie.video }}
        <hr>

        <!-- 글 이동 링크 (제목)
        <router-link 
          :to="{ name: 'article', params: {articlePk: article.pk} }">
          {{ article.title }}
        </router-link> -->
      </li>
    </ul>
   
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'MovieList',
    computed: {
      ...mapGetters(['movies'])
    },
    methods: {
      ...mapActions(['fetchMovies'])
    },
    created() {
      this.fetchMovies()
    },
  }
</script>

<style></style>
