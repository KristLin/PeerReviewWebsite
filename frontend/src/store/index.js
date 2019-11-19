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
  // user state getters
  getters: {
    isLoggedIn: state => {
      if (state.userId || localStorage.getItem("userId")) {
        return true
      } else {
        return false
      }
    },
    getUserId: state => {
      return state.userId ? state.userId : localStorage.getItem("userId")
    },
    getUserMajor: state => {
      return state.userMajor ? state.userMajor : localStorage.getItem("userMajor")
    },
    getUserName: state => {
      return state.userName ? state.userName : localStorage.getItem("userName")
    }
  },
  // mutations for user states
  mutations: {
    login(state, userData) {
      state.userId = userData.userId;
      state.userMajor = userData.userMajor;
      state.userName = userData.userName;
      localStorage.setItem("userId", userData.userId);
      localStorage.setItem("userMajor", userData.userMajor);
      localStorage.setItem("userName", userData.userName)
    },
    logout(state) {
      state.userId = null;
      state.userMajor = null;
      state.userName = null;
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
