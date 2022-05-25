<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar },
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>

<style>
  @import 'https://fonts.googleapis.com/css?family=Raleway';
  div.container
  {
    font-family: Raleway;
    margin: 0 auto;
    padding: 2em;
    text-align: center;
  }
</style>