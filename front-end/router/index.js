import Vue from "vue";
import VueRouter from "vue-router";
import RavenBlogsMain from "../views/RavenBlogsMain.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import EditPost from "../views/EditPost.vue";
import Profile from "../views/Profile.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Main",
    component: RavenBlogsMain,
  },

  {
    path: "/login",
    name: "Login",
    component: Login,
  },

  {
    path: "/register",
    name: "Register",
    component: Register,
    props: true,
  },

  {
    path: "/edit",
    name: "Edit",
    component: EditPost,
    props: true,
  },

  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
];

const router = new VueRouter({
  mode: "hash",
  routes,
});

export default router;
