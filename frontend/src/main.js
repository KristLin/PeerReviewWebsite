import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import axios from 'axios'
import VueHighlightJS from 'vue-highlight.js';

Vue.config.productionTip = false
Vue.prototype.$axios = axios

import 'vue-highlight.js/lib/allLanguages'
import './assets/vs.css';
Vue.use(VueHighlightJS);

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
