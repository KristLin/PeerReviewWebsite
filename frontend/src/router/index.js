import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/Login.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import(/* webpackChunkName: "signup" */ '../views/Signup.vue')
  },
  {
    path: '/search',
    name: 'search',
    component: () => import(/* webpackChunkName: "search" */ '../views/Search.vue')
  },
  {
    path: '/myProjects',
    name: 'myProjects',
    component: () => import(/* webpackChunkName: "myProjects" */ '../views/MyProjects.vue')
  },
  {
    path: '/createProject',
    name: 'createProject',
    component: () => import(/* webpackChunkName: "createProject" */ '../views/CreateProject.vue')
  },
  {
    path: '/file',
    name: 'file',
    component: () => import(/* webpackChunkName: "file" */ '../views/File.vue')
  },
  {
    path: '/news',
    name: 'news',
    component: () => import(/* webpackChunkName: "news" */ '../views/News.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 }
  }
})

export default router
