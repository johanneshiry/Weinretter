<template>
  <div class="imp">
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
              <a :href="restaurant.link" target="_blank">Angebot ansehen &#8594;</a>
            </l-popup>
          </l-marker>
        </v-marker-cluster>
      </l-map>
    </div>
  </div>
</template>
