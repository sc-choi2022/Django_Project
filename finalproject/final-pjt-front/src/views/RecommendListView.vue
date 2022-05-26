<template>
  <div>
    <div class="container">
      <div class="gallery1">
        <figure class="gallery_item item1"><router-link 
          :to="{ name: 'recommendOtt', params: {ottId: 8} }"><img src="https://w.namu.la/s/984a3a524c3a76ef69967a3538f0b655d9e4a9b948314bd8d57f34a1502753104f1613f356c08d4352cdfad86bbea9cd56b2133ea5c9c7a57f1c065b1048cb5b99a3d5c985c3e5dcc9771079d20c1e9243522e2675093317ec2656221a51fa59" alt="netflix" height="200" width="300">
          </router-link>
        </figure>
        <figure class="gallery_item item2"><router-link 
          :to="{ name: 'recommendOtt', params: {ottId: 97} }"><img src="https://w.namu.la/s/806795f01bfdb99ee07ef5ed4d26c7a76ce99bddf229f51418d040f4387944e4e06d19bcbd84da2a179de6273e3ca30f084aabc97154fb91a2f167ee349cec6d6e3c4db1abb00949ce2523d61074442a389fffadb69a3030b85c5168be94f968" alt="watcha" height="200" width="300">
          </router-link>
        </figure>
        <figure class="gallery_item item3"><router-link 
          :to="{ name: 'recommendOtt', params: {ottId: 337} }"><img src="https://w.namu.la/s/e53fcef546cc1b3f510694f331690215c764c0672c35dd34d207f29ed51c38de36e9f57e5bdd2ee05df77b4c1731d4ce840d3990860b959d27dc073339f94f0705d5bb2a4295a17b8911c5f6d31384752c47dedbd5d7f51bfec4db459a7e6f4b" alt="disney plus" height="200" width="300">
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