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
  .color
  {
      background: rgb(4, 23, 59);
  }
  html, body
  {
      margin: 0px;
  }

  div.container
  {
    font-family: Raleway;
    margin: 0 auto;
    padding: 2em;
    text-align: center;
  }

  div.container a
  {
      color: #FFF;
      text-decoration: none;
      font: 20px Raleway;
      margin: 0px 10px;
      padding: 10px 10px;
      position: relative;
      z-index: 0;
      cursor: pointer;
  }
</style>
