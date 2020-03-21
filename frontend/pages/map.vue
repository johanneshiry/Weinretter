<template>
  <div class="container">
    <link
      rel="stylesheet"
      href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
      integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
      crossorigin=""
    />
    <div id="mapid"></div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import L from 'leaflet'

export default Vue.extend({
  components: {},
  mounted() {
    let recaptchaScript = document.createElement('script')
    recaptchaScript.setAttribute(
      'src',
      'https://unpkg.com/leaflet@1.6.0/dist/leaflet.js'
    )
    document.head.appendChild(recaptchaScript)
    const mymap = L.map('mapid').setView([51.505, -0.09], 13)
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
