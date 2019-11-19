import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

// import vue bootstrap
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import { BSpinner } from 'bootstrap-vue'

// user bootstrap spinner class
Vue.component('b-spinner', BSpinner)

// import axios and assign it to prototype $axios
import axios from 'axios'
Vue.prototype.$axios = axios

// import vue-highlight.js
import VueHighlightJS from 'vue-highlight.js';
import 'vue-highlight.js/lib/allLanguages'
import './assets/my-vs.css';
Vue.use(VueHighlightJS);

// import vue sweet alert 2
import VueSweetalert2 from 'vue-sweetalert2';
Vue.use(VueSweetalert2);
import 'sweetalert2/dist/sweetalert2.min.css';

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
