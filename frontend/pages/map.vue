<template>
  <div class="map">
    <Navigation/>
    <div class="container">
      <div v-if="zoomInRequired" class="zoom-notice">Um die Restaurants zu sehen, zoome in die Karte</div>
      <l-map ref="map" id="mapid" :zoom.sync="zoom" :center="[51.163375, 10.447683]" @update:bounds="fetchRestaurants">
        <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"/>
        <v-geosearch :options="geosearchOptions" ></v-geosearch>
        <l-marker
          v-for="restaurant in restaurants"
          :lat-lng="[restaurant.location.lat, restaurant.location.lng]"
        >
          <l-popup>{{ restaurant.name }} <a :href="restaurant.link">Link</a></l-popup>
        </l-marker>
      </l-map>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  import Navigation from '../components/Navigation.vue'
  import VGeosearch from 'vue2-leaflet-geosearch';
  import { OpenStreetMapProvider } from 'leaflet-geosearch';
  import 'leaflet-geosearch/assets/css/leaflet.css'

  export default Vue.extend({
    data() {
      return {
        geosearchOptions: {
          provider: new OpenStreetMapProvider(),
          showMarker: false,
          showPopup: false,
        },
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
        if (!this.zoomInRequired) {
          this.$store.dispatch('fetchRestaurants', {
            leftLng: bounds.getWest(),
            rightLng: bounds.getEast(),
            bottomLat: bounds.getSouth(),
            topLat: bounds.getNorth()
          })
        }
      }
    },

    mounted() {
      this.$refs["map"].mapObject.locate({setView: true, maxZoom: 15})
    },
    components: {
      VGeosearch,
      Navigation
    },

    head() {
      return {
        title: "Finde Restaurants - WeinRetter",
      }
    }
  })
</script>

<style scoped>
  .container {
    margin: 0 auto;
    min-height: 92vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    flex-direction: column;
  }

  #mapid {
    height: 92vh;
    width: 100vw;
  }

  .zoom-notice {
    margin: 10px;
  }
</style>
