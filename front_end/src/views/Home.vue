<template>
  <div class="homeContainer">
    <!-- 页首的图片 -->
    <div class="home_header">
      <img src="../assets/images/banner.png" alt="" />
      <div class="header_content">
        <span>科学防护 共渡难关</span>
        <span>covid-19疫情实时播报</span>
        <span>数据来源：WHO及权威媒体报道</span>
      </div>
    </div>

    <!-- 疫情数据展示 -->
    <div class="home_content">
      <!-- 当日全国疫情数据展示 -->
      <div class="data_country_daily">
        <h3>全国疫情数据(含港澳台)</h3>
        <van-grid :column-num="3" :gutter="6" class="vanGrid" :border="true">
          <van-grid-item
            icon="photo-o"
            text="文字"
            class="van-grid-item__content"
            ><span>现有确诊</span><span class="number">3333</span
            ><span>较上日:</span></van-grid-item
          >
          <van-grid-item
            icon="photo-o"
            text="文字"
            class="van-grid-item__content"
            ><span>无症状感染者</span><span class="number">3333</span
            ><span>较上日:</span></van-grid-item
          >
          <van-grid-item
            icon="photo-o"
            text="文字"
            class="van-grid-item__content"
            ><span>境外输入</span><span class="number">3333</span
            ><span>较上日:</span></van-grid-item
          >
          <van-grid-item
            icon="photo-o"
            text="文字"
            class="van-grid-item__content"
            ><span>累计确诊</span><span class="number">3333</span
            ><span>较上日:</span></van-grid-item
          >
          <van-grid-item
            icon="photo-o"
            text="文字"
            class="van-grid-item__content"
            ><span>累计治愈</span><span class="number">3333</span
            ><span>较上日:</span></van-grid-item
          >
          <van-grid-item
            icon="photo-o"
            text="文字"
            class="van-grid-item__content"
            ><span>累计死亡</span><span class="number">3333</span
            ><span>较上日:</span></van-grid-item
          >
        </van-grid>
      </div>

      <!-- 全国疫情概况 -->
      <div class="data_country">
        <h3>中国疫情</h3>
      </div>
    </div>
  </div>
</template>

<script>
import { Grid, GridItem } from "vant";
export default {
  components: {
    [Grid.name]: Grid,
    [GridItem.name]: GridItem,
  },
};
</script>

<style lang="scss">
h3 {
  margin: 0;
  padding: 0;
}
.homeContainer {
  .home_header {
    position: relative;
    img {
      width: 100%;
      height: 150px;
    }
    .header_content {
      position: absolute;
      width: 240px;
      // background-color: pink;
      left: 0;
      top: 20px;
      display: flex;
      flex-direction: column;
      font-size: 22px;
      color: white;
      text-align: center;
      :nth-child(3) {
        font-size: 16px;
      }
    }
  }
  .home_content {
    margin: 0 auto;
    .data_country_daily {
      width: 100%;
      display: flex;
      flex-direction: column;
      text-align: center;
      h3 {
        font-size: 18px;
        color: #1989fa;
      }
      .vanGrid {
        // background-color: pink;
        .van-grid-item__content {
          background-color: pink;
        }
        span {
          font-size: 12px;
        }
      }
    }
  }
}
</style>
