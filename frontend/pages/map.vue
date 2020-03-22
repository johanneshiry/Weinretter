<template>
  <div class="map">
    <Navigation />
    <div class="container">
      <div v-if="zoomInRequired" class="zoom-notice">
        Um dein <span class="highlight"><b>Lieblingsrestaurant</b></span> zu finden, zoome in die Karte
      </div>
      <l-map
        ref="map"
        id="mapid"
        :min-zoom=5
        :zoom.sync="zoom"
        @update:bounds="fetchRestaurants"
      >
        <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png" />
        <v-geosearch :options="geosearchOptions"/>
        <v-marker-cluster>
          <l-marker
            v-for="restaurant in restaurants"
            :lat-lng="[restaurant.location.lat, restaurant.location.lng]"
            :key="'' + restaurant.location.lat + restaurant.location.lng"
          >
            <l-popup>
              <b>{{ restaurant.name }}</b>
              <br>
              <p v-if="restaurant.tags && restaurant.tags.length > 0"><i>Angebot: </i>
                <b-form-tag
                  v-for="tag in restaurant.tags"
                  :key="tag"
                  :title="tag"
                  variant="dark"
                  disabled
                  class="mr-1 tag">
                  {{ tag }}
                </b-form-tag>
              </p>
              <br>
              <a :href="restaurant.link" target="_blank">Angebot ansehen &#8594;</a>
            </l-popup>
          </l-marker>
        </v-marker-cluster>
      </l-map>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import Navigation from '../components/Navigation.vue'
import VGeosearch from 'vue2-leaflet-geosearch'
import { OpenStreetMapProvider } from 'leaflet-geosearch'
import 'leaflet-geosearch/assets/css/leaflet.css'
import 'leaflet.markercluster/dist/MarkerCluster.css'
import 'leaflet.markercluster/dist/MarkerCluster.Default.css'

export default Vue.extend({
  data() {
    return {
      geosearchOptions: {
        provider: new OpenStreetMapProvider(),
        showMarker: false,
        showPopup: false
      },
      zoom: 7
    }
  },

  computed: {
    restaurants() {
      return this.$store.state.fetchedRestaurants
    },

    zoomInRequired() {
      // For the wow effect at the hackathon, show all restaurants always.
      // When we actually have a lot of data, remove the `false` from here.
      return false && this.zoom < 9;
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
    this.$refs['map'].mapObject.locate({ setView: true, maxZoom: 15 }).setView([51.163375, 10.447683], 7);
  },
  components: {
    VGeosearch,
    Navigation
  },

  head() {
    return {
      title: 'Finde Restaurants - WeinRetter'
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
