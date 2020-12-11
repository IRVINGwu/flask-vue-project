<template>
  <div class="app_container">

    <!-- header区域 -->
    <van-nav-bar
        title="疫情动态"
        left-text="返回"
        left-arrow
        @click-left="goBack"
        fixed
    />

    <!-- tabbar区域 -->
    <div class="tabbar">
      <van-tabbar v-model="active">
        <router-link to="/" tag="a" class="van-tabbar-item"
        >
          <van-tabbar-item icon="chart-trending-o"
          >国内疫情
          </van-tabbar-item
          >
        </router-link
        >
        <router-link to="/world" tag="a" class="van-tabbar-item"
        >
          <van-tabbar-item icon="bar-chart-o"
          >世界疫情
          </van-tabbar-item
          >
        </router-link
        >
        <router-link to="/news" tag="a" class="van-tabbar-item"
        >
          <van-tabbar-item icon="newspaper-o"
          >疫情新闻
          </van-tabbar-item
          >
        </router-link
        >
        <router-link to="/rumors" tag="a" class="van-tabbar-item"
        >
          <van-tabbar-item icon="notes-o"
          >谣言粉碎
          </van-tabbar-item
          >
        </router-link
        >
      </van-tabbar>
    </div>
    <router-view v-slot="{ Component }">
      <transition>
        <component :is="Component"/>
      </transition>
    </router-view>
  </div>
</template>
<script>
import {NavBar, Tabbar, TabbarItem} from 'vant'

export default {
  name: 'App',
  data () {
    return {
      active: 0,
      flag: true,
    }
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    },
  },
  components: {
    [Tabbar.name]: Tabbar,
    [TabbarItem.name]: TabbarItem,
    [NavBar.name]: NavBar,
  },
}
</script>
<style lang="scss" scoped>
.app_container {
  // tabbar区域样式
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

    a {
      text-decoration: none;
    }

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
        text-decoration: none;
      }
    }
  }
}
</style>
