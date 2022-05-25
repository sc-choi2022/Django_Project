<template>
  <div>
    <div class="container">
      <div class="gallery1">
        <figure class="gallery_item item1"><router-link 
          :to="{ name: 'recommendOtt', params: {ottId: 8} }"><img src="https://img.khan.co.kr/news/2022/04/20/2022042001002421400214721.jpg" alt="netflix" height="200" width="300">
          </router-link>
        </figure>
        <figure class="gallery_item item2"><router-link 
          :to="{ name: 'recommendOtt', params: {ottId: 97} }"><img src="https://image.edaily.co.kr/images/Photo/files/NP/S/2021/07/PS21070900209.jpg" alt="watcha" height="200" width="300">
          </router-link>
        </figure>
        <figure class="gallery_item item3"><router-link 
          :to="{ name: 'recommendOtt', params: {ottId: 337} }"><img src="https://img.wowtv.co.kr/wowtv_news/dnrs/20211112/B20211112084626560.jpg" alt="disney plus" height="200" width="300">
          </router-link>
        </figure>
      </div>
    </div>
    <br><br><br><br>
    <div class="container">
      <div class="gallery2">
        <figure class="gallery_item item01"><router-link 
          :to="{ name: 'recommendDirector', params: {directorId: 21684} }"><img src="@/assets/item1.png" alt="Bong Joon Ho" class="logoimg">
          </router-link>
        </figure>
        <figure class="gallery_item item02"><router-link 
          :to="{ name: 'recommendKeyword', params: {keywordId: 9840} }"><img src="@/assets/item2.png" alt="romance" class="logoimg">
          </router-link>
        </figure>
        <figure class="gallery_item item03"><router-link 
          :to="{ name: 'recommendKeyword', params: {keywordId: 6054} }"><img src="@/assets/item3.png" alt="friendship" class="logoimg">
          </router-link>
        </figure>
        <figure class="gallery_item item04"><router-link 
          :to="{ name: 'recommendKeyword', params: {keywordId: 470} }"><img src="@/assets/item4.png" alt="spy" class="logoimg">
          </router-link>
        </figure>
        <figure class="gallery_item item05"><router-link 
          :to="{ name: 'recommendKeyword', params: {keywordId: 4379} }"><img src="@/assets/item5.png" alt="timetravel" class="logoimg">
          </router-link>
        </figure>
        <figure class="gallery_item item06"><router-link 
          :to="{ name: 'recommendKeyword', params: {keywordId: 180547} }"><img src="@/assets/item6.png" alt="mcu" class="logoimg">
          </router-link>
        </figure>
        <figure class="gallery_item item07"><router-link 
          :to="{ name: 'recommendDirector', params: {directorId: 525} }"><img src="@/assets/item7.png" alt="Christopher Edward Nolan" class="logoimg">
          </router-link>
        </figure>
        <figure class="gallery_item item08"><router-link 
          :to="{ name: 'recommendKeyword', params: {keywordId: 9882} }"><img src="@/assets/item8.png" alt="space" class="logoimg">
          </router-link>
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecommendList'
}
</script>

<style scoped>
.gallery1 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(1, 5vw);
    grid-gap: 15px;
}
.gallery2 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(4, 5vw);
    grid-gap: 15px;
}
.logoimg {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
#app > div:nth-child(2) > div:nth-child(1) > div > figure.gallery_item {
  margin-left: 0;
  padding-left: 0;
}
.item1 {
  grid-column-start: 1;
  grid-column-end: 2;
  grid-row-start: 1;
  grid-row-end: 2;
}
.item2 {
  grid-column-start: 2;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 2;
}
.item3 {
  grid-column-start: 3;
  grid-column-end: 4;
  grid-row-start: 1;
  grid-row-end: 2;
}
.item01 {
  grid-column-start: 1;
  grid-column-end: 2;
  grid-row-start: 1;
  grid-row-end: 3;
}
.item02 {
  grid-column-start: 2;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 3;
}
.item03 {
  grid-column-start: 3;
  grid-column-end: 4;
  grid-row-start: 1;
  grid-row-end: 3;
}
.item04 {
  grid-column-start: 4;
  grid-column-end: 5;
  grid-row-start: 1;
  grid-row-end: 3;
}
.item05 {
  grid-column-start: 1;
  grid-column-end: 2;
  grid-row-start: 3;
  grid-row-end: 5;
}
.item06 {
  grid-column-start: 2;
  grid-column-end: 3;
  grid-row-start: 3;
  grid-row-end: 5;
}
.item07 {
  grid-column-start: 3;
  grid-column-end: 4;
  grid-row-start: 3;
  grid-row-end: 5;
}
.item08 {
  grid-column-start: 4;
  grid-column-end: 5;
  grid-row-start: 3;
  grid-row-end: 5;
}
</style>