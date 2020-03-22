<template>

  <b-container fluid class="footer">
    <b-row>
      <b-col class="social">
        <a href="https://www.instagram.com/weinretter_de" target="_blank">
          <font-awesome-icon :icon="{ prefix: 'fab', iconName: 'instagram' }"/>
        </a>
      </b-col>
    </b-row>
    <b-row>
      <b-col class="imp">Impressum - Datenschutz</b-col>
    </b-row>
    <b-row>
      <b-col class="copyright"> © 2020 Copyright - WeinRetterTeam</b-col>
    </b-row>
  </b-container>
</template>


<style scoped>

  a {
    color: var(--dark-grey);
  }

  a:hover {
    color: var(--highlight-red);
  }

  .footer {
    background-color: #fff;
    margin-top: 1em;
  }

  .social {
    margin: 3px 0px;
    text-align: center;
  }

  .copyright {
    color: var(--dark-grey);
    margin-bottom: 5px;
    text-align: center;
    font-size: 12px;
  }

  .imp {
    color: var(--dark-grey);
    margin-bottom: 5px;
    text-align: center;
    font-size: 12px;
  }

</style>
