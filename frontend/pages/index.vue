<template>
  <div id="index">
    <div class="index-content">
      <div class="skew">
        <div class="skew-inner">
          <p class="title">
            Rette dein
            <span class="highlight">Lieblingsrestaurant</span>
            <wbr>durch das Kaufen von
            <vue-typer
              :text="[
                'Wein',
                'Bier',
                'Lebensmitteln',
                'Cocktails',
                'To-Go-Essen',
                'Eis',
                'Wein'
              ]"
              :repeat="0"
            />
          </p>
          <div class="links">
            <nuxt-link to="/map" class="big-button wr-button main">
              Karte ansehen
            </nuxt-link>
            <nuxt-link to="/offer" class="big-button wr-button secondary">
              Restaurant eintragen
            </nuxt-link>
          </div>
        </div>
      </div>
      <div class="hero-img" />
    </div>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue';

  export default Vue.extend({
  components: {},

  head() {
    return {
      title: 'WeinRetter - Hol dir dein Lieblingslokal ins Wohnzimmer'
    };
  }
});
</script>

<style>
body,
html,
#__nuxt,
#__layout {
  height: 92vh;
}
.index-content,
#index {
  height: 100vh;
  margin-bottom: 0em;
}

.grecaptcha-badge {
  visibility: collapse !important;
}

.big-button {
  padding: 10px 20px;
  border-radius: 10px;
  margin-right: 20px;
  margin-bottom: 20px;
}

.wr-button {
  border: 3px solid var(--highlight-red);
}

.wr-button:hover {
  text-decoration: none;
}

.wr-button.secondary, .wr-button.main:hover, .wr-button.main:focus {
  background-color: white;
  color: var(--dark-grey);
}

.wr-button.secondary:hover, .wr-button.secondary:focus, .wr-button.main {
  background-color: var(--highlight-red);
  color: white;
}

.index-content {
  display: flex;
  flex-direction: row;
}

.links {
  display: flex;
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
  letter-spacing: 1px;
  margin-block: 50px;
  line-height: 1.1;
}

.vue-typer {
  color: var(--dark-grey);
}

.link a {
  padding: 10px 10px 10px 10px;
}

.highlight {
  color: var(--highlight-red);
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

  .links {
    flex-direction: column;
    align-items: start;
  }
}
</style>
