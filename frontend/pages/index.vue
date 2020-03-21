<template>
  <div>
    <b-navbar toggleable="lg" variant="info">
      <b-navbar-brand><nuxt-link to="/"><img src="../assets/weinretter_logo.png"></nuxt-link></b-navbar-brand>
      <b-navbar-toggle target="navbarSupportedContent"> </b-navbar-toggle>

      <b-collapse id="navbarSupportedContent" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item to="/map" right>
              Karte ansehen
          </b-nav-item>
          <b-nav-item to="/signup" right>
              Restaurant registrieren
          </b-nav-item>
          <b-nav-item to="/about" right>
              About
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <div class="container">
      <div>
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
    color: red;
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

  .navbar{
    background-color: white !important;
  }
  .navbar-brand{
    padding: 0;
  }
  .navbar-brand img{
    height: 4em;
  }

</style>
