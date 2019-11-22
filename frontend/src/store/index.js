import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  // user states
  state: {
    userId: null,
    userMajor: null,
    userName: null,
  },

  // getters of user states
  getters: {
    // check if user is logged in
    isLoggedIn: state => {
      if (state.userId || localStorage.getItem("userId")) {
        return true
      } else {
        return false
      }
    },

    // get user id
    getUserId: state => {
      return state.userId ? state.userId : localStorage.getItem("userId")
    },
    // get user major
    getUserMajor: state => {
      return state.userMajor ? state.userMajor : localStorage.getItem("userMajor")
    },
    // get user name
    getUserName: state => {
      return state.userName ? state.userName : localStorage.getItem("userName")
    }
  },

  mutations: {
    // handle login
    login(state, userData) {
      // store user states in memory
      state.userId = userData.userId;
      state.userMajor = userData.userMajor;
      state.userName = userData.userName;

      // store user states in local storage (cookies)
      localStorage.setItem("userId", userData.userId);
      localStorage.setItem("userMajor", userData.userMajor);
      localStorage.setItem("userName", userData.userName)
    },

    // handle logout
    logout(state) {
      // remove user states from memory
      state.userId = null;
      state.userMajor = null;
      state.userName = null;
      
      // remove user states from local storage (cookies)
      localStorage.removeItem("userId");
      localStorage.removeItem("userMajor");
      localStorage.removeItem("userName")
    }
  },
  actions: {
  },
  modules: {
  }
})
