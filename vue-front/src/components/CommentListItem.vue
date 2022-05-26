<template>
  <div class="comment-list-item">
<<<<<<< HEAD
    <div class="board">
      <div class ='first'>
        <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
          {{ comment.user.username }}
        </router-link>
      </div>
      <div class ='second'>
        <span v-if="!isEditing">{{ payload.content }}</span>
      </div>
      <div class ='third'>
        <span v-if="!isEditing">댓글 작성일: {{ payload.created_at }}</span>
      </div>
      <div class ='fourth'>
        <span v-if="!isEditing">댓글 수정일: {{ payload.updated_at }}</span>
      </div>
    </div>
=======
    <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
      {{ comment.user.username }}
    </router-link>: 
    
    <span v-if="!isEditing">{{ payload.content }}</span>
    <br>
    <span v-if="!isEditing">댓글 작성일: {{ payload.created_at }}</span> |  
    <span v-if="!isEditing">댓글 수정일: {{ payload.updated_at }}</span>
>>>>>>> 5a084e16b0aa12eeab8551a7119b3f908c6196eb

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteComment(payload)">Delete</button>
    </span>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articleId: this.comment.article,
        commentId: this.comment.id,
        content: this.comment.content,
        created_at: this.comment.created_at,
        updated_at: this.comment.updated_at,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.parent{
    width: 90%;
    margin: 10px auto;
}

.first {
    border: 1px;
    float: left;
    width:30%;
    box-sizing: border-box;
}

.second{
    border: 1px;
    float: left;
    margin-left: 5%;
    width:30%;
    box-sizing: border-box;
}

.third{
    border: 1px;
    float: right;
    width:30%;
    box-sizing: border-box;
}

.fourth{
    border: 1px;
    float: right;
    width:30%;
    box-sizing: border-box;
}
</style>