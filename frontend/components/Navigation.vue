<template>
  <div>
    <b-navbar toggleable="lg">
      <b-navbar-brand>
        <nuxt-link to="/">
          <img src="../assets/logo_wein_retter_1_small.png" />
        </nuxt-link>
      </b-navbar-brand>
      <b-navbar-toggle target="navbarSupportedContent" />

      <b-collapse id="navbarSupportedContent" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item to="/map" class="link" right>
            Karte ansehen
          </b-nav-item>
          <b-nav-item to="/offer" class="link" right>
            Restaurant eintragen
          </b-nav-item>
          <b-nav-item to="/about" class="link" right>
            Über uns
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<style scoped>
.link {
  font-weight: bold;
}

.navbar-brand {
  padding: 0;
}

.navbar-brand img {
  height: 2.5em;
  margin: 10px 30px;
}
</style>
