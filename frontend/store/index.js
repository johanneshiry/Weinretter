import Vuex from 'vuex'


const API_ENDPOINT = 'https://weinretter.de/api';

export default {
  state: {
    fetchedRestaurants: [],
    fetchedAreas: new Set()
  },
  actions: {
    createRestaurant(context, restaurant) {
      return fetch(API_ENDPOINT + "/restaurant", {
        method: 'POST', body: JSON.stringify(restaurant), headers: new Headers({'content-type': 'application/json'})
      })
    },

    fetchRestaurants(context, {leftLng, rightLng, bottomLat, topLat}) {
      // Divide area in tiles
      if (leftLng > rightLng || bottomLat > topLat) {
        return;
      }

      const leftTile = Math.floor(leftLng * 2) / 2;
      const rightTile = Math.floor(rightLng * 2) / 2;
      const bottomTile = Math.floor(bottomLat * 2) / 2;
      const topTile = Math.floor(topLat * 2) / 2;

      for (var lng = leftTile; lng <= rightTile; lng += 0.5) {
        for (let lat = bottomTile; lat <= topTile; lat += 0.5) {
          const tileName = `${lng}-${lat}`;

          if (context.state.fetchedAreas.has(tileName)) continue;
          context.commit('markAsLoaded', tileName);

          fetch(API_ENDPOINT + `/restaurant?left_lng=${lng}&right_lng=${lng + 0.5}&bottom_lat=${lat}&top_lat=${lat + 0.5}`)
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
}
