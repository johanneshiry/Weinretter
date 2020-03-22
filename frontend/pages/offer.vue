<template>
  <div class="offer">
    <Navigation></Navigation>
    <div class="container">
      <b-form @submit.prevent="submit">
        <b-form-group
          id="input-group-1"
          label="Name deines Restaurant:"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="name"
            required
            placeholder="La Pizza"
          />
        </b-form-group>

        <b-form-group id="input-group-2" label="Website zu deinem Restaurant:" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="link"
            type="url"
            required
            placeholder="http://lapizza.de"
          />
        </b-form-group>

        <l-map ref="map" id="mapid" :zoom=7 :center="[51.163375, 10.447683]">
          <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"/>
          <VGeosearch :options="geosearchOptions"/>
          <l-marker v-if="location" :lat-lng="location"/>
        </l-map>
        <b-button type="submit" variant="primary">Registrieren</b-button>
      </b-form>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
  import Vue from 'vue'
  import Navigation from "../components/Navigation";
  import Footer from "../components/Footer";
  import VGeosearch from 'vue2-leaflet-geosearch';
  import {OpenStreetMapProvider} from 'leaflet-geosearch';
  import 'leaflet-geosearch/assets/css/leaflet.css'

  export default Vue.extend({
    data() {
      return {
        geosearchOptions: {
          showMarker: false,
          provider: new OpenStreetMapProvider(),
        },
        name: '',
        link: '',
        location: null
      }
    },
    methods: {
      async submit() {
        if (!this.location) {
          this.$bvToast.toast('Wähle bitte den Standort deines Restaurant auf der Karte aus', {
            title: 'Fehler',
            autoHideDelay: 5000,
            variant: 'danger'
          });
          return;
        }

        let grecaptcha = await window.recaptcha;
        let captcha = await grecaptcha.execute('6Le3Kp4UAAAAADWlhb5dUD-FSDe7YpSr0p5rdLt_', {action: 'homepage'});
        await this.$store.dispatch('createRestaurant', {name: this.name, link: this.link, location: this.location, captcha});
        this.$bvToast.toast('Deine Restaurant wurde gespeichert', {
          title: 'Vielen Dank',
          autoHideDelay: 5000,
          variant: 'success'
        });
      },
    },
    mounted() {
      this.$refs["map"].mapObject.on('click', (e) => this.location = e.latlng);
      if (!window.recaptcha) {
        let recaptchaScript = document.createElement('script');
        recaptchaScript.setAttribute('src', 'https://www.google.com/recaptcha/api.js?render=6Le3Kp4UAAAAADWlhb5dUD-FSDe7YpSr0p5rdLt_');
        recaptchaScript.async = true;
        window.recaptcha = new Promise((resolve) => {
          recaptchaScript.onload = () => {
            grecaptcha.ready(() => resolve(grecaptcha))
          };
        });
        document.head.appendChild(recaptchaScript);
      }
    },
    head() {
      return {
        title: "Registriere dein Restaurant - WeinRetter",
      }
    },
    components: {
      Navigation,
      Footer,
      VGeosearch
    }
  })
</script>

<style scoped>
  .container {
    margin: 0 auto;
    min-height: 91vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  #mapid {
    height: 30vh;
    width: 50vw;
    cursor: pointer;
  }
</style>
