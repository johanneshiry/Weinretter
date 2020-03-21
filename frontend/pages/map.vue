<template>
  <div class="map">
    <Navigation/>
    <div class="container">
      <l-map ref="map" id="mapid" :zoom.sync="zoom" :center="[51.163375, 10.447683]" @update:bounds="fetchRestaurants" >
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

<script>
import Vue from 'vue'
import Navigation from '../components/Navigation.vue'
import Logo from '~/components/Logo.vue'

  export default Vue.extend({
    data() {
      return {
        zoom: 7
      }
    },

    computed: {
      restaurants() {
        return this.$store.state.fetchedRestaurants
      },

      zoomInRequired() {
        return this.zoom < 9;
      }
    },

    methods: {
      fetchRestaurants(bounds) {
        if(!this.zoomInRequired) {
          this.$store.dispatch('fetchRestaurants', {leftLng: bounds.getWest(), rightLng: bounds.getEast(), bottomLat: bounds.getSouth(), topLat: bounds.getNorth()})
        }
      }
    },

    mounted() {
      this.$refs["map"].mapObject.locate({setView: true, maxZoom: 15})
    },
    components: {
      Logo,
      Navigation
    },

    head() {
      return {
        title: "Finde Restaurants - WeinRetter",
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
