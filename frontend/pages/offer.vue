<template>
  <div class="offer">
    <div class="container">
      <b-form @submit.prevent="submit">
        <b-form-group
          id="input-group-name"
          label="Name deines Restaurants:"
          label-for="input-name"
        >
          <b-form-input
            id="input-name"
            v-model="name"
            class="input"
            required
            placeholder="La Pizza"
          />
        </b-form-group>

        <b-form-group
          id="input-group-url"
          label="Link zu deinem Angebot:"
          label-for="input-url"
        >
          <b-form-input
            id="input-url"
            v-model="link"
            class="input"
            type="url"
            required
            placeholder="http://lapizza.de"
          />
        </b-form-group>

        <b-form-group
          id="input-group-tel"
          label="(Optional) Telefonnummer"
          label-for="input-tel"
        >
          <b-form-input
            id="input-2"
            v-model="telephone"
            class="input"
            type="tel"
            placeholder="030 123456"
          />
        </b-form-group>

        <b-form-group
          id="input-group-description"
          label="(Optional) Kurze Beschreibung:"
          label-for="input-description"
        >
          <b-form-textarea
            id="input-description"
            v-model="description"
            rows="3"
            max-rows="6"
          />
        </b-form-group>

        <b-form-group
          v-if="!addressEntered"
          id="input-group-address"
          label="Addresse:"
          label-for="input-2"
        >
          <div id="input-group-address-inner">
            <b-form-input
              id="input-street"
              v-model="address.street"
              class="input"
              required
              placeholder="Friedrichstraße"
            />
            <b-form-input
              id="input-housenumber"
              v-model="address.housenumber"
              class="input"
              required
              placeholder="5B"
            />
            <b-form-input
              id="input-plz"
              v-model="address.plz"
              class="input"
              type="tel"
              required
              placeholder="10115"
            />
            <b-form-input
              id="input-city"
              v-model="address.city"
              class="input"
              required
              placeholder="Berlin"
            />
          </div>
        </b-form-group>
        <b-form-group
          v-else
          id="input-group-4"
          label="Standort auf der Karte auswählen:"
          label-for="mapid"
        >
          <l-map
            id="mapid"
            ref="map"
            :zoom="7"
            :center="[51.163375, 10.447683]"
          >
            <l-tile-layer url="https://{s}.tile.osm.org/{z}/{x}/{y}.png" />
            <VGeosearch :options="geosearchOptions" />
            <l-marker v-if="location" :lat-lng="location" />
          </l-map>
        </b-form-group>

        <b-form-group id="input-group-tags" label="Tags:">
          <div>
            <b-badge v-for="tag in availableTags" :key="tag" variant="info" class="tag" @click="addTag(tag)">
              {{ tag }} +
            </b-badge>
          </div>
          <br>
          <div>
            <b-form-tag
              v-for="tag in selectedTags"
              :key="tag"
              :title="tag"
              variant="dark"
              class="mr-1 tag selected"
              @remove="removeTag(tag)"
            >
              <b>{{ tag }}</b>
            </b-form-tag>
          </div>
        </b-form-group>
        <b-button v-if="addressEntered" type="submit" class="submit">
          <b>Registrieren</b>
        </b-button>
        <b-button v-else type="submit" class="submit">
          Weiter
        </b-button>
      </b-form>

      <b-alert
        v-model="mapMarkerMissing"
        class="position-fixed fixed-bottom m-0 rounded-0"
        style="z-index: 2000;"
        variant="danger"
        dismissible
      >
        Wähle bitte den Standort deines Restaurant auf der Karte aus
      </b-alert>
      <b-alert
        v-model="error"
        class="position-fixed fixed-bottom m-0 rounded-0"
        style="z-index: 2000;"
        variant="danger"
        dismissible
      >
        Da ist leider etwas schief gelaufen
      </b-alert>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import VGeosearch from 'vue2-leaflet-geosearch';
import { OpenStreetMapProvider } from 'leaflet-geosearch';
import 'leaflet-geosearch/assets/css/leaflet.css';

  export default Vue.extend({
    components: {
      VGeosearch
    },
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
        availableTags: ['Lieferung', 'Selbstabholung', 'Wein', 'Bier', 'Cocktails', 'Meal Kits', 'Speisen', 'Tee/Kaffee', 'weitere Lebensmittel'],
        selectedTags: [],
        location: null,
        addressEntered: false,
        mapMarkerMissing: false,
        error: false
      }
    },
    mounted() {
      if (!window.recaptcha) {
        let recaptchaScript = document.createElement('script');
        recaptchaScript.setAttribute('src', 'https://www.google.com/recaptcha/api.js?render=6Le3Kp4UAAAAADWlhb5dUD-FSDe7YpSr0p5rdLt_');
        recaptchaScript.async = true;
        window.recaptcha = new Promise((resolve) => {
          recaptchaScript.onload = () => {
            //eslint-disable-next-line no-undef
            grecaptcha.ready(() => resolve(grecaptcha))
          };
        });
        document.head.appendChild(recaptchaScript);
      }
    },
    methods: {
      async submit() {
        if (!this.addressEntered) {
          this.addressEntered = true;
          Vue.nextTick(() => this.$refs["map"].mapObject.on('click', (e) => {
            this.location = e.latlng;
            this.mapMarkerMissing = false;
          }));
          let result = await this.$store.dispatch('addressLookup', this.address);
          if (result) {
            this.location = result;
            Vue.nextTick(() => this.$refs["map"].mapObject.setView([result.lat, result.lng], 15));
          }
          return;
        }
        if (this.addressEntered && !this.location) {
          this.mapMarkerMissing = true;
          return;
        }
        try {
          let grecaptcha = await window.recaptcha;
          let captcha = await grecaptcha.execute('6Le3Kp4UAAAAADWlhb5dUD-FSDe7YpSr0p5rdLt_', {action: 'homepage'});
          await this.$store.dispatch('createRestaurant', {
            name: this.name,
            link: this.link,
            location: this.location,
            telephone: this.telephone,
            address: this.address,
            tags: this.selectedTags,
            captcha
          });
          this.$root.$bvToast.toast('Dein Restaurant wurde gespeichert', {
            title: 'Vielen Dank',
            autoHideDelay: 5000,
            variant: 'success'
          });
          this.$router.push("/");
        } catch (e) {
          this.error = true;
        }
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
    head() {
      return {
        title: "Registriere dein Restaurant - WeinRetter",
      }
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

  .submit:hover {
    background-color: var(--highlight-red);
    color: var(--light-grey);
  }

.tag {
  font-size: 15px;
  border: 2px solid var(--highlight-red);
  cursor: pointer;
  padding: 6px;
  background-color: transparent;
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

  .selected {
    background-color: var(--highlight-red);
    color: var(--light-grey);
  }

  .tag {
    margin-right: 5px;
    margin-bottom: 5px;
  }

</style>
