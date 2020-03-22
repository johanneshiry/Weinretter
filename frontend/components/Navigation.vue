<template>
  <div>
    <b-navbar toggleable="lg" variant="info">
      <b-navbar-brand
        ><nuxt-link to="/"
          ><img src="../assets/logo_wein_retter_1.png"/></nuxt-link
      ></b-navbar-brand>
      <b-navbar-toggle target="navbarSupportedContent"> </b-navbar-toggle>

      <b-collapse id="navbarSupportedContent" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item to="/map" class="link" right>
            Karte ansehen
          </b-nav-item>
          <b-nav-item to="/offer" class="link" right>
            Restaurant registrieren
          </b-nav-item>
          <b-nav-item to="/about" class="link" right>
            Über uns
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
