<template>
  <div>
    <div class="container">
      <h1>Login</h1>
      <form @submit.prevent="login(credentials)">
        <div class="login-form">
          <input v-model="credentials.username" type="text" id="username" class="login-username" autofocus="true" required="true" placeholder="Username" />
          <input v-model="credentials.password" type="password" id="password" class="login-password" required="true" placeholder="Password" />
          <input type="submit" name="Login" value="Login" class="login-submit" />
        </div>
      </form>
      <account-error-list v-if="authError"></account-error-list>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style scoped>
  div.container
  {
    font-family: Raleway;
    margin: 0 auto;
    padding: 2em;
    text-align: center;
  }
  body, html {
  height: 100%;
  }
  body {
  font-weight: 100;
  display: flex;
  overflow: hidden;
  }
  .login-form {
    background: lightgray;
    min-height: 10rem;
    margin: auto;
    max-width: 50%;
    padding: .5rem;
  }

  .login-username, .login-password {
    background: transparent;
    margin: 40rem;
    border: 0 solid;
    border-bottom: 1px solid rgba(white, .5);
    display: block;
    margin: 1rem;
    padding: .5rem;
    transition: 250ms;
    width: calc(100% - 3rem);
  }
  .login-submit {
    border: 1px solid white;
    background: transparent;
    display: block;
    margin: 1rem auto;
    min-width: 1px;
    padding: .25rem;
    transition: 250ms;
  }
</style>
