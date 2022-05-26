<template>
  <div class="account-error-list">
    {{ authError['username'] }}
    {{ authError['password1'] }}
    {{ authError['non_field_errors'] }}
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
  }
</script>

<style>
  .account-error-list {
    color: red;
  }
</style>
