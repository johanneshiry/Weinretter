import Vuex from 'vuex'

const API_ENDPOINT = 'https://weinretter.de/api';

export default new Vuex.Store({
  state: {
    fetchedRestaurants: [],
    fetchedAreas: new Set()
  },
  actions: {
    createRestaurant(restaurant) {
      return fetch(API_ENDPOINT + "/restaurant", {
        method: 'POST', body: JSON.stringify(restaurant)
      })
    },

    fetchRestaurants(context, {leftLng, rightLng, bottomLat, topLat}) {

      // Divide area in tiles
      if (leftLng > rightLng || bottomLat > topLat) {
        return;
      }

      const leftTile = Math.floor(leftLng * 10) / 10;
      const rightTile = Math.floor(rightLng * 10) / 10;
      const bottomTile = Math.floor(bottomLat * 10) / 10;
      const topTile = Math.floor(topLat * 10) / 10;

      for (let lng = leftTile; lng += 0.1; lng <= rightTile) {
        for (let lat = bottomTile; lat += 0.1; lng <= topTile) {
          const tileName = `${lng}-${lat}`;
          if (context.state.fetchedAreas.has(tileName)) continue;
          context.commit('markAsLoaded', tileName);

          fetch(API_ENDPOINT + `/restaurant?left_lng=${lng}&right_lng=${lng + 0.1}&bottomTile=${lat}&topTile=${lat + 0.1}`)
            .then(response => response.json())
            .then(restaurants => context.commit('addFetchedRestaurants', restaurants))
        }
      }
    }
  },
  mutations: {
    markAsLoaded(state, tileName) {
      state.fetchedAreas.add(tileName)
    },

    addFetchedRestaurants(state, restaurants) {
      state.fetchedRestaurants.push(...restaurants)
    }
  }
})
