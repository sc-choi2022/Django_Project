<template>
  <div>
    <div class="container">
      <h1>Signup</h1>
      <form @submit.prevent="signup(credentials)">
        <div class="signup-form">
          <input v-model="credentials.username" type="text" id="username" class="signup-username" autofocus="true" required="true" placeholder="Write Username" />
          <input v-model="credentials.password1" type="password" id="password1" class="signup-password" required="true" placeholder="Write Password" />
          <input v-model="credentials.password2" type="password" id="password2" class="signup-password" required="true" placeholder="Write Password Again" />
          <input type="submit" name="signup" value="signup" class="signup-submit" />
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
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
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
  .signup-form {
    background: lightgray;
    min-height: 10rem;
    margin: auto;
    max-width: 50%;
    padding: .5rem;
  }

  .signup-username, .signup-password {
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
  .signup-submit {
    border: 1px solid white;
    background: transparent;
    display: block;
    margin: 1rem auto;
    min-width: 1px;
    padding: .25rem;
    transition: 250ms;
  }
</style>