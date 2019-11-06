import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import { BSpinner } from 'bootstrap-vue'

Vue.component('b-spinner', BSpinner)

import axios from 'axios'
import VueHighlightJS from 'vue-highlight.js';

Vue.config.productionTip = false
Vue.prototype.$axios = axios

import 'vue-highlight.js/lib/allLanguages'
import './assets/my-vs.css';
Vue.use(VueHighlightJS);

import VueSweetalert2 from 'vue-sweetalert2';
Vue.use(VueSweetalert2);
import 'sweetalert2/dist/sweetalert2.min.css';

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
