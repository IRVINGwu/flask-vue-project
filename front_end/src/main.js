import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import echarts from "./assets/js/echarts.min.js";
// import "echarts/map/js/china.js";
import axios from "axios";

Vue.prototype.$echarts = echarts;
Vue.config.productionTip = false;

// axios.defaults.baseURL = "http://127.0.0.1:3333/";
// axios.defaults.headers["Content-Type"] = "application/x-www-form-urlencoded";
Vue.prototype.$http = axios;
// 这是在之前的项目中配置axios的方法，都看一下
// import axios from "axios";
// Vue.prototype.$http = axios.create({
//   baseURL: "http://api.cms.liulongbin.top/", //在全局设置 axios 的请求根路径，这样，在发起请求的时候，就可以不写根路径了
// });

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
