<template>
  <div class="container">
    <b-form @submit="submit">
      <b-form-group
        id="input-group-1"
        label="Name deines Restaurant:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="name"
          type="email"
          required
          placeholder="La Pizza"
        />
      </b-form-group>

      <b-form-group id="input-group-2" label="Website zu deinem Restaurant:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="link"
          required
          placeholder="http://lapizza.de"
        />
      </b-form-group>

      <l-map ref="map" id="mapid" :zoom=7 :center="[51.163375, 10.447683]">
        <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"/>
      </l-map>
      <b-button type="submit" variant="primary">Registrieren</b-button>
    </b-form>
  </div>
</template>

<script>
  import Vue from 'vue'

  export default Vue.extend({
    data() {
      return {
        name: '',
        link: ''
      }
    },
    methods: {
      submit() {
      }
    },
    mounted() {
      const map = this.$refs["map"].mapObject;
      map.on('click', function (e) {
        var popLocation = e.latlng;
        var popup = L.popup()
          .setLatLng(popLocation)
          .setContent('<p>Hello world!<br />This is a nice popup.</p>')
          .openOn(map);
      });
    },
    head() {
      return {
        title: "Registriere dein Restaurant - WeinRetter",
      }
    },
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
    height: 30vh;
    width: 50vw;
  }
</style>
