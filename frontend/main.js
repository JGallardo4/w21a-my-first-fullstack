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

axios.defaults.headers.common["token"] = this.$store.getters.authToken;

axios.defaults.baseURL = "http://127.0.0.1:5000/api";

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;
Vue.use(Vuex);

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
});

const store = new Vuex.Store({
  state: {
    authToken: "",
    allPosts: [],
  },

  getters: {
    authToken: (state) => state.authToken,
    allPosts: (state) => state.allPosts,
  },

  mutations: {
    SET_AUTH_TOKEN(state, payload) {
      state.authToken = payload;
    },

    SET_POSTS(state, payload) {
      state.allPosts = payload;
    },
  },

  actions: {
    logIn({ commit, dispatch, resolve }, payload) {
      return new Promise((reject) => {
        axios
          .post("/user/login", {
            username: payload["username"],
            password: payload["password"],
          })
          .then((response) => {
            if (response.status === 200) {
              commit("SET_AUTH_TOKEN", response.data["token"]);
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

    logOut({ commit, dispatch }) {
      commit("SET_AUTH_TOKEN", "");
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

    register({ dispatch }, payload) {
      return new Promise((resolve, reject) => {
        axios
          .post("/users", payload)
          .then((response) => {
            if (response.status === 201) {
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
          headers: this.dispatch("getAuthHeader"),
        })
        .catch((response) => console.log(response));
    },

    refreshPosts({ commit }) {
      axios
        .get("/posts", {})
        .then((response) => {
          if (response.status === 200) {
            commit(
              "SET_POSTS",
              response.data.sort((a, b) => {
                return new Date(b.created_at) - new Date(a.created_at);
              })
            );
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    deletePost(state, payload) {
      axios.delete("/posts", {
        data: payload,
        headers: this.dispatch("getAuthHeader"),
      });
    },

    getUsers() {
      axios
        .get("/users", { headers: this.dispatch("getAuthHeader") })
        .then((response) => response.data.map((user) => user.userId))
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

    // getAuthHeader(state) {
    //   if (token != "") {
    //     return JSON.stringify({ token: state.authToken });
    //   } else {
    //     return {};
    //   }
    // },
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
