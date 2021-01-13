import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/world',
    name: 'World',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/World.vue'),
  },
  {
    path: '/news',
    name: 'News',
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/News.vue'),
  },
  {
    path: '/rumors',
    name: 'Rumors',
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/Rumors.vue'),
  },
  {
    path: '/news/:id',
    name: 'NewsItem',
    component: () =>
      import(/* webpackChunkName: "about" */ '../components/News/NewsItem'),
    props: true
  },
  {
    path: '/:id',
    name: 'ChinaProvince',
    component: () =>
      import(/* webpackChunkName: "about" */ '../components/China/ChinaProvin'),
    props: true
  },
  {
    path: '/world/:id',
    name: 'WorldCountry',
    component: () =>
      import(/* webpackChunkName: "about" */ '../components/World/WorldCountry'),
    props: true
  },
  {
    path: '/world/predict/:id',
    name: 'WorldPredict',
    component: () =>
      import(/* webpackChunkName: "about" */ '../components/World/WorldPredict'),
    props: true
  },
]
const router = new VueRouter({
  routes,
  linkActiveClass: 'van-tabbar-item--active',
  linkExactActiveClas:'van-tabbar-item--active'
})
export default router
