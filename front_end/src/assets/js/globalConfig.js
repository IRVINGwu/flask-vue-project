import Vue from "vue";
import axios from "axios";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import echarts from "./echarts.min.js";

// 设置基准路由地址
axios.defaults.baseURL = "http://127.0.0.1:8080";
// axios.defaults.headers["Content-Type"] = "application/x-www-form-urlencoded";
Vue.prototype.$http = axios;
Vue.prototype.$echarts = echarts;

