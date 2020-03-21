<template>
  <div id="index">
    <router-view />
    <Navigation></Navigation>
    <div class="content">
      <div class="skew">
        <div class="skew-inner">
          <p class="title">
            Rette dein <span class="highlight">Lieblingsrestaurant</span> durch
            das Kaufen von Wein
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
      <div class="hero-img"></div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Logo from '../components/Logo.vue'
import Navigation from '../components/Navigation.vue'

export default Vue.extend({
  components: {
    Logo,
    Navigation
  }
})
</script>

<style>
.content {
  display: flex;
  flex-direction: row;
}

.skew {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  transform: skewX(-7deg) translateX(100px);
  width: 60%;

  z-index: 10;
  background: white;
  margin: 0;
  padding: 0;
}

.skew-inner {
  transform: skewX(7deg) translateX(-50px);
}

.hero-img {
  width: 40%;
  background-image: url('https://images.unsplash.com/photo-1525576064846-083dce8b33ba?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=900&q=60');
  height: 100vh;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 50px;
  color: #35495e;
  letter-spacing: 1px;
}

.link a {
  padding: 10px 10px 10px 10px;
  color: blue;
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

.navbar {
  background-color: white !important;
}

.navbar-brand {
  padding: 0;
}

.navbar-brand img {
  height: 4em;
}

.navbar {
  background-color: white !important;
}
.navbar-brand {
  padding: 0;
}
.navbar-brand img {
  height: 4em;
}
</style>
