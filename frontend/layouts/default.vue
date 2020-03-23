<template>
  <div class="default-layout">
    <Navigation />
    <nuxt />
    <Footer />
  </div>
</template>

<script>
import Footer from '../components/Footer'
import Navigation from '../components/Navigation.vue'
import Vue from 'vue'

export default Vue.extend({
  components: {
    Footer,
    Navigation
  }
})
</script>

<style>
html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
  /* To stop the page from jumping when some pages need to scroll and some don't */
  overflow-y: scroll;
}

:root {
  --highlight-red: #b12525;
  --light-grey: #d2d2d2;
  --dark-grey: #5e5757;
}

web-info-widget {
  right: 1.5rem;
  bottom: 1.5rem;
  --color-primary: var(--highlight-red);
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}

.default-layout {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
