const API_ENDPOINT = '/api';

export default {
  state: () => ({
    fetchedRestaurants: [],
    fetchedAreas: new Set()
  }),
  actions: {
    async createRestaurant(context, restaurant) {
      const response = await fetch(API_ENDPOINT + '/restaurants', {
        method: 'POST',
        body: JSON.stringify(restaurant),
        headers: new Headers({ 'content-type': 'application/json' })
      });
      if (!response.ok) {
        throw new Error(await response.json());
      }
      return response.json()
    },

    async updateRestaurant(context, { id, passcode, restaurant }) {
      const response = await fetch(
        `${API_ENDPOINT}/restaurant/${id}?passcode=${passcode}`,
        {
          method: 'PUT',
          body: JSON.stringify(restaurant),
          headers: new Headers({ 'content-type': 'application/json' })
        }
      );
      if (!response.ok) {
        throw new Error(await response.json());
      }
    },

    fetchRestaurants(context, { leftLng, rightLng, bottomLat, topLat }) {
      // Divide area in tiles
      if (leftLng > rightLng || bottomLat > topLat) {
        return;
      }

      const leftTile = Math.floor(leftLng * 0.1) / 0.1;
      const rightTile = Math.floor(rightLng * 0.1) / 0.1;
      const bottomTile = Math.floor(bottomLat * 0.1) / 0.1;
      const topTile = Math.floor(topLat * 0.1) / 0.1;

      for (var lng = leftTile; lng <= rightTile; lng += 10) {
        for (let lat = bottomTile; lat <= topTile; lat += 10) {
          const tileName = `${lng}-${lat}`;

          if (context.state.fetchedAreas.has(tileName)) continue;
          context.commit('markAsLoaded', tileName);

          fetch(
            API_ENDPOINT +
              `/restaurants?left_lng=${lng}&right_lng=${lng +
                10}&bottom_lat=${lat}&top_lat=${lat + 10}`
          )
            .then(response => response.json())
            .then(restaurants =>
              context.commit('addFetchedRestaurants', restaurants)
            );
        }
      }
    },
    async addressLookup(context, { street, housenumber, city, plz }) {
      const response = await fetch(
        'https://nominatim.openstreetmap.org/search?' +
          `street=${encodeURIComponent(street)}%20${encodeURIComponent(
            housenumber
          )}` +
          `&city=${encodeURIComponent(city)}&postalcode=${encodeURIComponent(
            plz
          )}&country=Germany&format=json`
      );
      const result = await response.json();
      if (result && result.length) {
        return {
          lat: parseFloat(result[0].lat),
          lng: parseFloat(result[0].lon)
        };
      }
    },
    fetchOneRestaurant(context, restaurantId) {
      return fetch(API_ENDPOINT + '/restaurant/' + restaurantId).then(res =>
        res.json()
      );
    }
  },
  mutations: {
    markAsLoaded(state, tileName) {
      state.fetchedAreas.add(tileName);
    },

    addFetchedRestaurants(state, restaurants) {
      state.fetchedRestaurants.push(...restaurants);
    }
  }
};
