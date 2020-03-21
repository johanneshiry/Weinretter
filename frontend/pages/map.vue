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
    const map = L.map('mapid').setView([51.163375, 10.447683], 5)
    const tileLayer = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, " +
        "<a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, ",
    });

    tileLayer.addTo(map)
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
