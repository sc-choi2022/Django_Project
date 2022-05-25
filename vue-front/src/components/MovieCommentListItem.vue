<template>
  <li class="movie-comment-list-item">
    <!-- <router-link :to="{ name: 'profile', params: { username: review.user.username } }">
    </router-link>:  -->
      {{ review.user.username }}
    
    <span v-if="!isEditing">{{ payload.content }}</span>
    <span v-if="!isEditing">{{ payload.rank }}</span>
    <br>
    <span v-if="!isEditing">댓글 작성일: {{ payload.created_at }}</span> |  
    <span v-if="!isEditing">댓글 수정일: {{ payload.updated_at }}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <input type="number" v-model="payload.rank">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.username === review.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteReview(payload)">Delete</button>
    </span>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieCommentListItem',
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        movieId: this.review.movie,
        reviewId: this.review.id,
        content: this.review.content,
        created_at: this.review.created_at,
        updated_at: this.review.updated_at,
        rank: this.review.rank,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>

</style>