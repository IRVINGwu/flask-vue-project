<template>
  <div class="app_container">
    <!-- header区域 -->
    <div class="navbar">
      <span>&lt;&nbsp;&nbsp;&nbsp;&nbsp;返回</span>
      <span>疫情动态</span>
    </div>

    <!-- tabbar区域 -->
    <div class="tabbar">
      <van-tabbar v-model="active">
        <router-link to="/" tag="a" class="van-tabbar-item"
          ><van-tabbar-item icon="chart-trending-o"
            >国内疫情</van-tabbar-item
          ></router-link
        >
        <router-link to="/world" tag="a" class="van-tabbar-item"
          ><van-tabbar-item icon="bar-chart-o"
            >世界疫情</van-tabbar-item
          ></router-link
        >
        <router-link to="/news" tag="a" class="van-tabbar-item"
          ><van-tabbar-item icon="newspaper-o"
            >疫情新闻</van-tabbar-item
          ></router-link
        >
        <router-link to="/rumors" tag="a" class="van-tabbar-item"
          ><van-tabbar-item icon="notes-o"
            >谣言粉碎</van-tabbar-item
          ></router-link
        >
      </van-tabbar>
    </div>
    <router-view v-slot="{ Component }">
      <transition>
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<script>
import { NavBar, Tabbar, TabbarItem } from "vant";

export default {
  name: "App",
  data() {
    return {
      active: 0,
      flag: true,
    };
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
  },
  components: {
    [Tabbar.name]: Tabbar,
    [TabbarItem.name]: TabbarItem,
    [NavBar.name]: NavBar,
  },
};
</script>

<style lang="scss" scoped>
.navbar {
  background-color: rgba(238, 240, 241, 0.5);
  height: 30px;
  display: flex;
  align-items: center;
  span:first-child {
    color: #1989fa;
    flex: 3;
    text-align: center;
    font-size: 12px;
  }
  span:last-child {
    color: rgba(13, 47, 195, 0.938);
    flex: 8;
    font-size: 15px;
    font-weight: 100;
    padding-left: 52px;
  }
}

.tabbar {
  position: fixed;
  bottom: 0;
  left: 0;
  z-index: 99;
  border-top: 1px solid #ccc;
  display: -webkit-box;
  display: -webkit-flex;
  display: flex;
  box-sizing: content-box;
  width: 100%;
  height: 50px;
  padding-bottom: constant(safe-area-inset-bottom);
  padding-bottom: env(safe-area-inset-bottom);
  background-color: #ddd;
  .van-tabbar-item {
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    background-color: #ddd;
    -webkit-box-flex: 1;
    -webkit-flex: 1;
    flex: 1;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
    flex-direction: column;
    -webkit-box-align: center;
    -webkit-align-items: center;
    align-items: center;
    -webkit-box-pack: center;
    -webkit-justify-content: center;
    justify-content: center;
    color: #646566;
    font-size: 14px;
    line-height: 1;
    cursor: pointer;
    .van-tabbar-item--active {
      color: #1989fa;
      background-color: #ddd;
    }
  }
}
</style>
