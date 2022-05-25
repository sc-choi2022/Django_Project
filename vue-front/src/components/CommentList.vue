<template>
  <div class="comment-list">
    <div class="container">
      <ul>
        <comment-list-item 
          v-for="comment in comments" 
          :comment="comment" 
          :key="comment.id">
        </comment-list-item>        
      </ul>
      <comment-list-form></comment-list-form>
    </div>
  </div>
</template>

<script>
import CommentListForm from '@/components/CommentListForm.vue'
import CommentListItem from '@/components/CommentListItem.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentListItem, CommentListForm },
  props: { comments: Array },
}
</script>

<style>

</style>