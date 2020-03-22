<template>
  <div class="offer">
    <Navigation/>
    <div class="container">
      <b-form @submit.prevent="submit">
        <b-form-group
          id="input-group-name"
          label="Name deines Restaurants:"
          label-for="input-name"
        >
          <b-form-input
            id="input-name"
            class="input"
            v-model="name"
            required
            placeholder="La Pizza"
          />
        </b-form-group>

        <b-form-group id="input-group-url" label="Link zu deinem Angebot:" label-for="input-url">
          <b-form-input
            id="input-url"
            class="input"
            v-model="link"
            type="url"
            required
            placeholder="http://lapizza.de"
          />
        </b-form-group>

        <b-form-group id="input-group-tel" label="(Optional) Telefonnummer" label-for="input-tel">
          <b-form-input
            id="input-2"
            class="input"
            v-model="telephone"
            type="tel"
            placeholder="030 123456"
          />
        </b-form-group>

        <b-form-group id="input-group-description" label="(Optional) Kurze Beschreibung:" label-for="input-description">
          <b-form-textarea
            id="input-description"
            v-model="description"
            rows="3"
            max-rows="6"
          />
        </b-form-group>

        <b-form-group v-if="!addressEntered" id="input-group-address" label="Addresse:" label-for="input-2">
          <div id="input-group-address-inner">
            <b-form-input
              id="input-street"
              class="input"
              v-model="address.street"
              type="tel"
              required
              placeholder="Friedrichstraße"
            />
            <b-form-input
              id="input-housenumber"
              class="input"
              v-model="address.housenumber"
              required
              type="tel"
              placeholder="5B"
            />
            <b-form-input
              id="input-plz"
              class="input"
              v-model="address.plz"
              required
              placeholder="10115"
            />
            <b-form-input
              id="input-city"
              class="input"
              v-model="address.city"
              required
              placeholder="Berlin"
            />
          </div>
        </b-form-group>
        <b-form-group v-else id="input-group-4" label="Standort auf der Karte auswählen:" label-for="mapid">
          <l-map ref="map" id="mapid" :zoom=7 :center="[51.163375, 10.447683]">
            <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"/>
            <VGeosearch :options="geosearchOptions"/>
            <l-marker v-if="location" :lat-lng="location"/>
          </l-map>
        </b-form-group>

        <b-form-group id="input-group-tags" label="Tags:">
          <div>
            <b-badge v-for="tag in availableTags" @click="addTag(tag)" variant="info" class="tag">{{tag}} +</b-badge>
          </div>
          <br/>
          <div>
            <b-form-tag
              v-for="tag in selectedTags"
              @remove="removeTag(tag)"
              :key="tag"
              :title="tag"
              variant="dark"
              class="mr-1 tag selected"
            ><b>{{ tag }}</b>
            </b-form-tag>
          </div>
        </b-form-group>

        <b-button v-if="addressEntered" type="submit" class="submit"><b>Registrieren</b></b-button>
        <b-button v-else type="submit" class="submit">Weiter</b-button>
      </b-form>
    </div>
    <Footer/>
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
        description: '',
        telephone: '',
        address: {
          street: '',
          housenumber: '',
          plz: '',
          city: ''
        },
        availableTags: ['Lieferung', 'Selbstabholung', 'Wein', 'Bier', 'Cocktails', 'Meal Kits', 'weitere Lebensmittel'],
        selectedTags: [],
        location: null,
        addressEntered: false
      }
    },
    methods: {
      async submit() {
        if (!this.addressEntered) {
          this.addressEntered = true;
          Vue.nextTick(() => this.$refs["map"].mapObject.on('click', (e) => this.location = e.latlng));
          return;
        }
        if (this.addressEntered && !this.location) {
          this.$bvToast.toast('Wähle bitte den Standort deines Restaurant auf der Karte aus', {
            title: 'Fehler',
            autoHideDelay: 5000,
            variant: 'danger'
          });
          return;
        }

        let grecaptcha = await window.recaptcha;
        let captcha = await grecaptcha.execute('6Le3Kp4UAAAAADWlhb5dUD-FSDe7YpSr0p5rdLt_', {action: 'homepage'});
        await this.$store.dispatch('createRestaurant', {
          name: this.name,
          link: this.link,
          location: this.location,
          telephone: this.telephone,
          tags: this.selectedTags,
          captcha
        });
        this.$bvToast.toast('Deine Restaurant wurde gespeichert', {
          title: 'Vielen Dank',
          autoHideDelay: 5000,
          variant: 'success'
        });
      },
      addTag(tag) {
        this.availableTags = this.availableTags.filter(t => t !== tag);
        this.selectedTags.push(tag);
      },
      removeTag(tag) {
        this.selectedTags = this.selectedTags.filter(t => t !== tag);
        this.availableTags.push(tag)
      }
    },
    mounted() {
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
    justify-content: center;
    align-items: center;
  }


  #mapid {
    position: relative;
    height: 30vh;
    min-height: 300px;
    min-width: 400px;
    cursor: pointer;
  }

  .submit {
    margin: 10px auto;
    width: 100%;
    font-weight: bold;
    color: var(--highlight-red);
    background-color: transparent;
  }

  .submit:hover{
    background-color: var(--highlight-red);
    color: var(--light-grey);
  }

  .tag {
    font-size: 15px;
    border: 2px solid var(--highlight-red);
    cursor: pointer;
    padding: 6px;
    background-color:transparent;
    color: var(--highlight-red);
  }

  #input-group-address-inner {
    display: grid;
    grid-template-columns: 90px auto 70px;
    grid-column-gap: 10px;
    grid-row-gap: 15px;
  }


  #input-street {
    grid-row-start: 1;
    grid-row-end: 1;
    grid-column-start: 1;
    grid-column-end: 3;
  }

  #input-housenumber {
    grid-row-start: 1;
    grid-row-end: 1;
    grid-column-start: 3;
    grid-column-end: 4;
  }

  #input-plz {
    grid-row-start: 2;
    grid-row-end: 2;
    grid-column-start: 1;
    grid-column-end: 1;

  }

  #input-city {
    grid-row-start: 2;
    grid-row-end: 2;
    grid-column-start: 2;
    grid-column-end: 4;
  }

  .selected{
    background-color: var(--highlight-red);
    color: var(--light-grey);
  }
  .tag + .tag {
    margin: 5px;
  }

</style>
