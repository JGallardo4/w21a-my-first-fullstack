import Vue from "vue";
import App from "./App.vue";
import router from "./router/index.js";
import axios from "axios";
import Vuex from "vuex";
import VuexPersistence from "vuex-persist";
import cookies from "vue-cookies";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faUser,
  faUserTimes,
  faUserCheck,
  faUserPlus,
  faTimes,
  faCrow,
  faHeart,
  faPen,
  faUndo,
  faComment,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(
  faUser,
  faUserTimes,
  faUserCheck,
  faUserPlus,
  faTimes,
  faCrow,
  faHeart,
  faPen,
  faUndo,
  faComment
);

Vue.component("font-awesome-icon", FontAwesomeIcon);

axios.defaults.headers.common["X-Api-Key"] =
  "1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD";

axios.defaults.baseURL = "http://127.0.0.1:5000";

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;
Vue.use(Vuex);

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
});

const store = new Vuex.Store({
  state: {
    isAuthenticated: false,
    userId: 1,
    userName: "",
    loginToken: "",
    allPosts: [],
  },

  getters: {
    getIsAuthenticated(state) {
      return state.isAuthenticated;
    },

    getUserName(state) {
      return state.userName;
    },

    getUserId(state) {
      return state.userId;
    },

    getLoginToken(state) {
      return state.loginToken;
    },

    getAllPosts(state) {
      return state.allPosts;
    },
  },

  mutations: {
    SET_AUTHENTICATED(state, payload) {
      state.isAuthenticated = payload;
    },

    SET_USERID(state) {
      state.userId = 1;
    },

    SET_LOGIN_TOKEN(state, payload) {
      state.loginToken = payload;
    },

    SET_USERNAME(state, payload) {
      state.userName = payload;
    },

    DELETE_USERDATA(state) {
      state.isAuthenticated = false;
      state.userId = "";
      state.userName = "";
    },

    SET_POSTS(state, payload) {
      state.allPosts = payload;
    },
  },

  actions: {
    logIn({ commit }, payload) {
      commit("SET_AUTHENTICATED", true);
      commit("SET_USERID", 1);
      commit("SET_USERNAME", "Juan");
      console.log(payload);
      // return new Promise((resolve, reject) => {
      //   axios
      //     .post("/login", payload)
      //     .then((response) => {
      //       if (response.status === 201) {
      //         commit("SET_AUTHENTICATED", true);
      //         commit("SET_USERID", response.data.userId);
      //         commit("SET_USERNAME", response.data.username);
      //         commit("SET_LOGIN_TOKEN", response.data.loginToken);
      //         dispatch("redirect", "/");
      //         resolve(response);
      //       } else {
      //         reject(response);
      //       }
      //     })
      //     .catch((error) => {
      //       reject(error);
      //     });
      // });
    },

    logOut({ commit, dispatch }) {
      commit("DELETE_USERDATA");
      dispatch("redirect", "/login");
    },

    checkLogin({ dispatch }) {
      if (this.getters.getIsAuthenticated) {
        dispatch("redirect", "/");
      } else {
        if (router.currentRoute != "/login") {
          dispatch("logOut");
        }
      }
    },

    register({ commit, dispatch }, payload) {
      return new Promise((resolve, reject) => {
        axios
          .post("/users", payload)
          .then((response) => {
            if (response.status === 201) {
              commit("SET_AUTHENTICATED", true);
              commit("SET_USERID", response.data.userId);
              commit("SET_USERNAME", response.data.username);
              commit("SET_LOGIN_TOKEN", response.data.loginToken);
              dispatch("redirect", "/");
              resolve(response);
            } else {
              reject(response);
            }
          })
          .catch((error) => {
            reject(error);
          });
      });
    },

    initializeStore({ state }) {
      if (window.localStorage.getItem("vuex")) {
        this.replaceState(
          Object.assign(state, JSON.parse(window.localStorage.getItem("state")))
        );
      }
    },

    createPost({ getters }, payload) {
      axios
        .post("/posts", {
          user_id: getters.getUserId,
          content: payload,
        })
        .catch((response) => console.log(response));
    },

    refreshPosts({ commit, state }) {
      axios
        .get("/posts", { userId: state.userId })
        .then((response) => {
          if (response.status === 200) {
            commit("SET_POSTS", response.data);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    deletePost(state, payload) {
      axios.delete("/posts", { data: payload });
    },

    getUsers() {
      axios
        .get("/users")
        .then((response) => response.data.map((user) => user.userId))
        .then(console.log)
        .catch((error) => {
          console.log(error);
        });
    },

    redirect(state, route) {
      if (router.currentRoute != route) {
        router.push(route).catch((error) => {
          if (
            error.name !== "NavigationDuplicated" &&
            !error.message.includes(
              "Avoided redundant navigation to current location"
            )
          ) {
            console.log(error);
          }
        });
      }
    },
  },

  plugins: [vuexLocal.plugin],
});

/* eslint-disable-next-line */
window.vm = new Vue({
  router: router,
  axios: axios,
  store: store,
  cookies: cookies,
  render: (h) => h(App),
}).$mount("#app");
