<template>
  <div class="edit container">
    <restaurant-form
      v-if="restaurant"
      :save-restaurant="submit"
      :restaurant="restaurant"
      submit-text="Diese Daten speichern"
    />
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
</template>

<script>
import Vue from 'vue';
import RestaurantForm from '../../components/RestaurantForm';

export default Vue.extend({
  components: {
    RestaurantForm
  },
  data() {
    return {
      restaurant: null,
      error: false,
      id: null,
      passcode: null
    };
  },
  async mounted() {
    const [id] = this.$route.params.idCode.split(':');

    try {
      this.restaurant = await this.$store.dispatch('fetchOneRestaurant', id);
    } catch (e) {
      this.error = true;
    }
  },
  methods: {
    async submit(restaurant) {
      try {
        const [id, passcode] = this.$route.params.idCode.split(':');
        await this.$store.dispatch('updateRestaurant', {
          id,
          passcode,
          restaurant
        });
        this.$root.$bvToast.toast('Deine Änderung wurde gespeichert', {
          title: 'Vielen Dank',
          autoHideDelay: 5000,
          variant: 'success'
        });
      } catch (e) {
        this.error = true;
      }
    }
  },
  head() {
    return {
      title: 'Editiere dein Restaurant - WeinRetter'
    };
  }
});
</script>

<style scoped>
.container {
  margin: 0 auto;
  justify-content: center;
  align-items: center;
}
</style>
