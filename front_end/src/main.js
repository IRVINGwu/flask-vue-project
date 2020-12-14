import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import echarts from "./assets/js/echarts.min.js";
// import "echarts/map/js/china.js";
import axios from "axios";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import moment from "moment"

Vue.prototype.$echarts = echarts;
Vue.config.productionTip = false;

// 设置基准路由地址
axios.defaults.baseURL = "http://127.0.0.1:5000";
// axios.defaults.headers["Content-Type"] = "application/x-www-form-urlencoded";
Vue.prototype.$http = axios;

Vue.filter('formatDate',function(data){
  return moment(data).format('YYYY-MM-DD')
})

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
