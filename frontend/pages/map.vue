<template>
  <div class="map">
    <router-view />
    <Navigation></Navigation>
    <div class="container">
      <l-map ref="map" id="mapid" :zoom="7" :center="[51.163375, 10.447683]">
        <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png" />
        <l-marker
          v-for="restaurant in restaurants"
          :lat-lng="[restaurant.location.lat, restaurant.location.lng]"
        >
          <l-popup
            >{{ restaurant.name }} <a :href="restaurant.link">Link</a></l-popup
          >
        </l-marker>
      </l-map>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import L from 'leaflet'
import Navigation from '../components/Navigation.vue'
import Logo from '~/components/Logo.vue'

export default Vue.extend({
  data() {
    return {
      restaurants: [
        {
          link: 'http://google.de',
          location: { lat: 48.04, lng: 9.5 },
          name: 'abc'
        },
        {
          link: 'http://google.de',
          location: { lat: 49.04, lng: 9.7 },
          name: 'abc'
        }
      ]
    }
  },
  mounted() {
    const map = this.$refs['map'] as any
    map.mapObject.locate({ setView: true, maxZoom: 15 })
  },
  components: {
    Logo,
    Navigation
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
