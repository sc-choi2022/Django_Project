<template>
  <div>
    <div class="container">
      <h1>haha</h1>
      <h1>{{ profile.username }}</h1>
      <h2>My Movie</h2>
      <ul>
        <li v-for="movie in profile.movies_mymovie" :key="movie.id">
          movie_id: {{ movie.id }}  |
          movie_title: {{ movie.title }}
        </li>
      </ul>
      <h2>Wish</h2>
      <ul>
        <li v-for="movie in profile.movies_wish" :key="movie.id">
          movie_id: {{ movie.id }}  |
          movie_title: {{ movie.title }}
        </li>
      </ul>

      <h2>좋아요 한 글</h2>
      <ul>
        <li v-for="article in profile.like_articles" :key="article.id">
          <router-link :to="{ name: 'article', params: { articleId: article.id } }">
            {{ article.title }}
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile'])
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
