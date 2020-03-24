import Vue from 'vue';

const sa_event = function() {
  const a = [].slice.call(arguments);
  sa_event.q ? sa_event.q.push(a) : sa_event.q = [a];
};

Vue.prototype.$sa_event = sa_event;
