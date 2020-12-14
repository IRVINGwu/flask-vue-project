<template>
  <div class="app_container">

    <!-- header区域 -->
    <div class="header">
      <span @click="goBack" v-show="flag">&lt;返回</span>
      <span>疫情动态</span>
    </div>

    <!-- tabbar区域 -->
    <div class="tabbar">
      <van-tabbar :value="active">
        <router-link to="/" name="Home" tag="a" class="van-tabbar-item">
          <van-tabbar-item icon="chart-trending-o">国内疫情</van-tabbar-item>
        </router-link>
        <router-link to="/world" name="World" tag="a" class="van-tabbar-item">
          <van-tabbar-item icon="bar-chart-o">世界疫情</van-tabbar-item>
        </router-link>
        <router-link to="/news" name="News" tag="a" class="van-tabbar-item">
          <van-tabbar-item icon="newspaper-o">疫情新闻</van-tabbar-item>
        </router-link>
        <router-link to="/rumors" name="Rumors" tag="a" class="van-tabbar-item">
          <van-tabbar-item icon="notes-o">谣言粉碎</van-tabbar-item>
        </router-link
        >
      </van-tabbar>
    </div>

    <transition>
      <router-view></router-view>
    </transition>

  </div>
</template>

<script>
import {Tabbar, TabbarItem} from 'vant'

export default {
  name: 'App',
  data () {
    return {
      // active: 0,
      flag: false,
    }
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    },
  },
  created () {
  },
  components: {
    [Tabbar.name]: Tabbar,
    [TabbarItem.name]: TabbarItem,
    // [NavBar.name]: NavBar,
  },
  watch: {
    '$route.path': function (newval, oldval) {
      if (newval === '/') {
        this.flag = false
      } else {
        this.flag = true
      }
    }
  },
  computed: {
    active () {//获取到路由的名字给active赋值
      if(this.$route.name == 'Home'){
        return 0
      }else if(this.$route.name == 'World'){
        return 1
      }else if(this.$route.name == 'News'){
        return 2
      }else{
        return 3
      }
    }
  }
}
</script>
<style lang="scss">
.app_container {
  overflow: hidden;

  .header {
    position: relative;
    width: 100%;
    height: 30px;
    line-height: 30px;
    background-color: #eee;

    span:nth-child(1) {
      position: absolute;
      font-size: 0.6rem;
      color: #1989fa;
      left: 5%;
      top: 0;
    }

    span:nth-child(2) {
      position: absolute;
      font-size: 0.8rem;
      color: #020202;
      margin-left: 50%;
      transform: translateX(-1.9rem);
    }
  }

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
    background-color: #eeeeee;

    a {
      text-decoration: none;
    }

    .van-tabbar-item {
      display: -webkit-box;
      display: -webkit-flex;
      display: flex;
      background-color: #eeeeee;
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
        text-decoration: none;
      }
    }
  }

  //路由切换的动画效果
  .v-enter {
    opacity: 0;
    transform: translateX(100%);
  }

  .v-leave-to {
    opacity: 0;
    transform: translateX(-100%);
    position: absolute;
    display: none;
  }

  .v-enter-active,
  .v-leave-active {
    //transition: all 0.6s ease;
  }

  .my-active {
    color: #1989fa;
    background-color: #ddd;
    text-decoration: none;
  }
}

</style>
