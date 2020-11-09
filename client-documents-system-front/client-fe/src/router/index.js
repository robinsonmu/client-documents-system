import Vue from 'vue'
import VueRouter from 'vue-router'
import store from "../store";
import jwtUtils from "../utils/jwt";

Vue.use(VueRouter)

const ifNotAuthenticated = (to, from, next) => {
  if (!store.getters["authModule/isAuthenticated"]) {
    store
      .dispatch("authModule/createSessionFromToken")
      .then(() => next("/home"))
      .catch(() => next());
    return;
  }
  next();
};

const ifAuthenticated = (to, from, next) => {
  if (!store.getters["authModule/isAuthenticated"]) {
    store
      .dispatch("authModule/createSessionFromToken")
      .then(() => next())
      .catch(() => next("/login"));
    return;
  } else {
    const token = store.getters["authModule/getToken"]
    if (!jwtUtils.tokenIsValid(token)) {
      store
        .dispatch("authModule/revokeAuthToken")
        .then(() => {
          next('/login')
        })
    }
  }
  next();
};

const routes = [
  {
    path: '/',
    redirect: 'login'
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/login.vue'),
    beforeEnter: ifNotAuthenticated,
  },
  {
    path: '/home',
    name: 'home',
    component: () => import('../views/Home.vue'),
    beforeEnter: ifAuthenticated,
  },
  {
    path: '/documents',
    name: 'documents',
    component: () => import('../views/Document.vue'),
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
