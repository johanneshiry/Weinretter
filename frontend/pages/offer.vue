<template>
  <div class="offer">
    <div class="container">
      <restaurant-form :save-restaurant="submit" submit-text="Registrieren" />
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
import RestaurantForm from '../components/RestaurantForm';

export default Vue.extend({
  components: {
    RestaurantForm
  },
  data() {
    return {
      error: false
    };
  },
  mounted() {
    if (!window.recaptcha) {
      let recaptchaScript = document.createElement('script');
      recaptchaScript.setAttribute(
        'src',
        'https://www.google.com/recaptcha/api.js?render=6Le3Kp4UAAAAADWlhb5dUD-FSDe7YpSr0p5rdLt_'
      );
      recaptchaScript.async = true;
      window.recaptcha = new Promise(resolve => {
        recaptchaScript.onload = () => {
          //eslint-disable-next-line no-undef
          grecaptcha.ready(() => resolve(grecaptcha));
        };
      });
      document.head.appendChild(recaptchaScript);
    }
  },
  methods: {
    async submit(restaurant) {
      try {
        let grecaptcha = await window.recaptcha;
        let captcha = await grecaptcha.execute(
          '6Le3Kp4UAAAAADWlhb5dUD-FSDe7YpSr0p5rdLt_',
          { action: 'homepage' }
        );
        await this.$store.dispatch('createRestaurant', {
          ...restaurant,
          captcha
        });
          this.$root.$bvToast.toast('Dein Restaurant wurde gespeichert', {
          title: 'Vielen Dank',
          autoHideDelay: 5000,
          variant: 'success'
        });
        this.$router.push('/');
      } catch (e) {
        this.error = true;
      }
    },
  },
  head() {
    return {
      title: 'Registriere dein Restaurant - WeinRetter'
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

