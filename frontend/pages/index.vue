<template>
  <div id="index">
    <router-view />
    <Navigation></Navigation>
    <div class="content">
      <div class="skew">
        <div class="skew-inner">
          <p class="title">
            Rette dein <span class="highlight">Lieblingsrestaurant</span>
            <wbr /> durch das Kaufen von Wein
          </p>
          <div class="links">
            <nuxt-link to="/map" class="weinretter-button prominent">
              Karte ansehen
            </nuxt-link>
            <nuxt-link to="/offer" class="weinretter-button">
              Wein anbieten
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
body,
html {
  height: 100%;
}

.weinretter-button {
  padding: 10px 20px;
  border: 3px solid #b12525;
  border-radius: 10px;
  color: black;
  margin-right: 20px;
}

.weinretter-button:hover {
  text-decoration: none;
  color: gray;
}

.prominent {
  background: #b12525;
  color: white;
}

.weinretter-button:hover {
  text-decoration: none;
  color: gray;
}

.content {
  display: flex;
  flex-direction: row;
}

.skew {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
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
  font-weight: bolder;
  font-size: 60px;
  color: #35495e;
  letter-spacing: 1px;
  margin-block: 50px;
}

.link a {
  padding: 10px 10px 10px 10px;
}

.highlight {
  color: #b12525;
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
