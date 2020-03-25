<template>
  <div id="about">
    <div class="about">
      <h2 class="about-title">
        Über WeinRetter
      </h2>
      <div style="text-align:center; margin: 10px">
        <iframe
          width="560"
          height="315"
          src="https://www.youtube.com/embed/aVk9_ipRQ9Q"
          frameborder="0"
          allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        />
      </div>
      <p>
        Die COVID-19-Krise trifft insbesondere Restaurants schwer. Durch die
        behördlich verordneten Schließungen oder beschränkten Öffnungszeiten
        erleiden viele einen erheblichen Umsatzrückgang, bis hin zum
        vollständigen Umsatzausfall.
      </p>
      <p>
        Gleichzeitig verfügen viele Restaurants über ungenutztes Potenzial:
        volle Weinkeller. Indem diese Bestände verkauft werden, können
        Restaurants einen Teil ihrer laufenden Kosten decken und ihre
        wirtschaftliche Lage verbessern.
      </p>
      <p>
        Trage zum Fortbestand deines Lieblingsrestaurants bei, indem du Wein aus
        dessen Lagerbestand kaufst!
      </p>
      <p>
        Diese Seite wurde innerhalb des
        <a href="https://wirvsvirushackathon.org/" target="_blank">
          #WirVsVirus Hackathons
        </a>
        erstellt und basiert auf dem Vorbild von
        <a href="https://cellars.nyc" target="_blank">Cellars.NYC</a>. Bei
        Fragen kontaktiere uns einfach auf
        <a href="https://www.instagram.com/weinretter_de" target="_blank">
          <font-awesome-icon :icon="{ prefix: 'fab', iconName: 'instagram' }" />
          Instagram
        </a>
        oder per E-Mail an
        <a href="mailto:weinretterde@gmail.com">weinretterde@gmail.com</a>.
      </p>
      <img
        class="wvvlogo"
        src="../assets/Logo_WirVsVirus.png"
        alt="#WirVsVirus Logo"
      />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  components: {},

  head() {
    return {
      title: 'Über uns - WeinRetter'
    };
  }
});
</script>

<style scoped>
iframe {
  max-width: 100%;
}

a {
  color: var(--highlight-red);
  text-decoration: none;
}

a:hover {
  color: var(--highlight-red);
  text-decoration: underline;
}

.wvvlogo {
  width: 100%;
}

.about-title {
  margin-bottom: 0.5em;
}

.about {
  max-width: 45em;
  width: 90%;
  margin-left: auto;
  margin-right: auto;
  padding: 1em;
}
</style>
