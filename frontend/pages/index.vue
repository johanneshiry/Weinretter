<template>
  <div id="index">
    <router-view />
    <Navigation></Navigation>
    <div class="content">
      <div class="skew">
        <div class="skew-inner">
          <p class="title">
            Rette dein <span class="highlight">Lieblingsrestaurant</span>
            <wbr />durch das Kaufen von Wein
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
  },

  head() {
    return {
      title: 'WeinRetter'
    }
  }
})
</script>

<style>
body,
html,
#__nuxt,
#__layout,
#index,
.content {
  height: 92vh;
}

.grecaptcha-badge {
  visibility: collapse !important;
}

.weinretter-button {
  padding: 10px 20px;
  border: 3px solid var(--highlight-red);
  border-radius: 10px;
  color: var(--dark-grey);
  margin-right: 20px;
}

.weinretter-button:hover {
  text-decoration: none;
  color: var(--light-grey);
}

.prominent {
  background: var(--highlight-red);
  color: white;
}

.content {
  display: flex;
  flex-direction: row;
}

.skew {
  min-height: 100%;
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
  background-image: url('https://source.unsplash.com/collection/8821407');
  background-size: cover;
  height: 100%;
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
  line-height: 1.1;
}

.link a {
  padding: 10px 10px 10px 10px;
}

.highlight {
  color: var(--highlight-red);
}

.navbar {
  background-color: white !important;
}

.navbar-brand {
  padding: 0;
}

.navbar-brand img {
  height: 2.5em;
  margin: 10px 30px;
}

/* Tablet Styles */
@media screen and (max-width: 899px) {
  .hero-img {
    display: none;
  }
  .skew,
  .skew-inner {
    transform: none;
  }
  .skew {
    width: 100%;
    margin: 0 50px;
  }
}

/* Phone Styles */
@media screen and (max-width: 649px) {
  .highlight {
    display: inline;
  }
  .title {
    display: block;
    word-wrap: break-word;
    white-space: normal;
    width: calc(100vw - 60px);
    font-size: 30px;
  }
  .skew {
    margin: 0 30px;
  }
}
</style>
