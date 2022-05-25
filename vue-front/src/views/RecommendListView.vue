<template>
  <div>
    <div class="container">
      <!-- OTT -->
      <router-link 
          :to="{ name: 'recommendOtt', params: {ottId: 8} }"><img src="https://img.khan.co.kr/news/2022/04/20/2022042001002421400214721.jpg" alt="netflix" height="200" width="300">
          </router-link>
      <router-link 
          :to="{ name: 'recommendOtt', params: {ottId: 97} }"><img src="https://image.edaily.co.kr/images/Photo/files/NP/S/2021/07/PS21070900209.jpg" alt="watcha" height="200" width="300">
          </router-link>
      <router-link 
          :to="{ name: 'recommendOtt', params: {ottId: 337} }"><img src="https://img.wowtv.co.kr/wowtv_news/dnrs/20211112/B20211112084626560.jpg" alt="disney plus" height="200" width="300">
          </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecommendList'
}
</script>

<style>

</style>