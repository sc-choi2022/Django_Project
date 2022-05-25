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
      <div class="container">
      <!-- Director -->
        <router-link 
            :to="{ name: 'recommendDirector', params: {directorId: 21684} }"><img src="@/assets/item1.png" alt="Bong Joon Ho" height="200" width="250">
            </router-link>
        <router-link 
            :to="{ name: 'recommendKeyword', params: {keywordId: 9840} }"><img src="@/assets/item2.png" alt="romance" height="200" width="250">
            </router-link>
        <router-link 
            :to="{ name: 'recommendKeyword', params: {keywordId: 6054} }"><img src="@/assets/item3.png" alt="friendship" height="200" width="250">
            </router-link>
        <router-link 
            :to="{ name: 'recommendKeyword', params: {keywordId: 470} }"><img src="@/assets/item4.png" alt="spy" height="200" width="250">
            </router-link>
      </div>
        <router-link 
            :to="{ name: 'recommendKeyword', params: {keywordId: 4379} }"><img src="@/assets/item5.png" alt="timetravel" height="200" width="250">
            </router-link>
        <router-link 
            :to="{ name: 'recommendKeyword', params: {keywordId: 180547} }"><img src="@/assets/item6.png" alt="mcu" height="200" width="250">
            </router-link>
        <router-link 
            :to="{ name: 'recommendDirector', params: {directorId: 525} }"><img src="@/assets/item7.png" alt="Christopher Edward Nolan" height="200" width="250">
            </router-link>
        <router-link 
            :to="{ name: 'recommendKeyword', params: {keywordId: 9882} }"><img src="@/assets/item8.png" alt="space" height="200" width="250">
            </router-link>
      <div class="container">
      </div>
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