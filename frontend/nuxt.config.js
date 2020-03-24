export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }],
    script: [
      {
        src: 'https://sa.weinretter.de/latest.js',
        body: true
      },
      {
        src: 'https://webcomponent.coverified.info/build/embed.js',
        body: true
      }
    ],
    noscript: [
      { innerHTML: '<img src="https://sa.weinretter.de/image.gif" alt="">' }
    ],
    __dangerouslyDisableSanitizers: ['noscript']
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: ['@fortawesome/fontawesome-svg-core/styles.css'],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    { src: '~/plugins/vue2-leaflet-markercluster.js', mode: 'client' },
    { src: '~/plugins/vue-typer.js', mode: 'client' },
    { src: '~/plugins/vue-leaflet-geosearch.js', mode: 'client' },
    { src: '~/plugins/simpleanalytics.js', mode: 'client' },
    '~/plugins/fontawesome.js'
  ],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: ['@nuxt/typescript-build'],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://bootstrap-vue.js.org
    'bootstrap-vue/nuxt',
    'nuxt-leaflet'
  ]
};
