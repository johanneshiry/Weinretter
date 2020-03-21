<template>
  <div class="container">
    <div>
      <logo/>
      <p class="title">
        Rette dein <span class="highlight">Lieblingsrestaurant</span> durch das Kaufen von Wein
      </p>
      <h2 class="subtitle">
        weinretter
      </h2>
      <div class="links">
        <nuxt-link to="/map" class="button--green">
          Karte ansehen
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import Logo from '~/components/Logo.vue'

  export default Vue.extend({
    components: {
      Logo
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

  .title {
    font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    display: block;
    font-weight: 300;
    font-size: 100px;
    color: #35495e;
    letter-spacing: 1px;
  }

  .highlight {
    color: #B12525;
  }

  .subtitle {
    font-weight: 300;
    font-size: 42px;
    color: #526488;
    word-spacing: 5px;
    padding-bottom: 15px;
  }

  .links {
    padding-top: 15px;
  }
</style>
