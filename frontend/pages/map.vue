<template>
  <div class="container">
    <l-map id="mapid" :zoom=6 :center="[52, 10]">
      <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
      <l-marker v-for="restaurant in restaurants" :lat-lng="[restaurant.location.lat, restaurant.location.lng]"></l-marker>
    </l-map>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import L from 'leaflet'

export default Vue.extend({
 data() {
   return {
     restaurants: [{"link":"http://google.de","location":{"lat":48.04,"lng":9.5},"name":"abc"}, {"link":"http://google.de","location":{"lat":49.04,"lng":9.7},"name":"abc"}]

   }
 }
})
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

#mapid {
  height: 100vh;
  width: 100vw;
}
</style>
