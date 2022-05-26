<template>
  <div class="movie-comment-list-item">
    <span v-if="!isEditing">{{ payload.content }} 
      <span v-if="payload.rank === 2"><font-awesome-icon icon="fa-solid fa-star" /></span>
      <span v-if="payload.rank === 4"><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /></span>
      <span v-if="payload.rank === 6"><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /></span>
      <span v-if="payload.rank === 8"><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /></span>
      <span v-if="payload.rank === 10"><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /><font-awesome-icon icon="fa-solid fa-star" /></span>
      {{ payload.updated_at.substr(0,10) }}</span>
    <br>  
    <span v-if="!isEditing"></span>

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
  </div>
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