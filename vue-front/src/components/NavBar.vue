<template>
  <div>
    <div class="container color borderXwidth">
      <router-link :to="{ name: 'movies' }">HOME</router-link>
      <router-link :to="{ name: 'articles' }">COMMUNITY</router-link>
      <router-link :to="{ name: 'recommend' }">RECOMMEND</router-link> 
      <router-link v-if="!isLoggedIn" :to="{ name: 'login' }">LOGIN</router-link>
      <router-link v-if="!isLoggedIn" :to="{ name: 'signup' }">SIGNUP</router-link>
      <router-link v-if="isLoggedIn" :to="{ name: 'logout' }">LOGOUT</router-link>
      <router-link v-if="isLoggedIn" :to="{ name: 'profile' ,params: { username } }">PROFILE</router-link>
    </div>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style>
  @import 'https://fonts.googleapis.com/css?family=Raleway';
  .color
  {
      background: linear-gradient(#141E30, #243B55);
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

/* Border X get width  */
div.borderXwidth a:before, div.borderXwidth a:after
{
    position: absolute;
    opacity: 0;
    width: 0%;
    height: 2px;
    content: '';
    background: #FFF;
    transition: all 0.3s;
}

div.borderXwidth a:before
{
    left: 0px;
    top: 0px;
}

div.borderXwidth a:after
{
    right: 0px;
    bottom: 0px;
}

div.borderXwidth a:hover:before, div.borderXwidth a:hover:after
{
    opacity: 1;
    width: 100%;
}

</style>