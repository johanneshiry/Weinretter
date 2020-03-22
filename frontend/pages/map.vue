<template>
  <div class="map">
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
        <l-tile-layer url="https://{s}.tile.osm.org/{z}/{x}/{y}.png" />
        <v-geosearch :options="geosearchOptions"/>
        <v-marker-cluster>
          <l-marker
            v-for="restaurant in restaurants"
            :icon="icon"
            :lat-lng="[restaurant.location.lat, restaurant.location.lng]"
            :key="'' + restaurant.location.lat + restaurant.location.lng"
          >
            <l-popup>
              <b>{{ restaurant.name }}</b>
              <br>
              <p v-if="restaurant.description">{{restaurant.description}}</p>
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
              <p v-if="restaurant.address"><i>Adresse: </i>
                <br>
                <template v-if="typeof restaurant.address === 'string'">
                  {{restaurant.address}}
                </template>
                <template v-else>
                  {{restaurant.address.street}} {{restaurant.address.housenumber}} <br>
                  {{restaurant.address.city}} {{restaurant.address.plz}}
                </template>
              </p>
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
  import L from 'leaflet';

  export default Vue.extend({
  data() {
    return {
      geosearchOptions: {
        provider: new OpenStreetMapProvider(),
        showMarker: false,
        showPopup: false,
        style: 'bar'
      },
      zoom: 7,
      icon: L.icon({
        iconUrl: require('../assets/marker.png'),
        iconSize: [24, 74],
        iconAnchor: [16, 37]
      })
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
    this.$refs['map'].mapObject
      .locate({ setView: true, maxZoom: 15 })
      .setView([51.163375, 10.447683], 7);
  },
  components: {
    VGeosearch,
    Navigation,
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
  max-height: 83vh;
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

p {
  margin: 5px 0;
}

.zoom-notice {
  margin: 10px;
}
</style>

<style>
  .leaflet-popup-content-wrapper {
    border-radius: 6px !important;
  }

  .leaflet-control-geosearch.bar {
    margin: 10px 50px 0 !important;
  }
</style>
