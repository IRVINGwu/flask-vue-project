<template>
  <div class="homeContainer">
    <!-- 页首的图片 -->
    <div class="home_header">
      <img src="../assets/images/head.png" alt="" />
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
          <van-grid-item icon="photo-o" text="文字" class="van-grid-item_1"
            ><span>现有确诊</span><span class="number_1">3333</span
            ><span
              >较上日:<span class="number_1">222</span></span
            ></van-grid-item
          >
          <van-grid-item icon="photo-o" text="文字" class="van-grid-item_2"
            ><span>无症状感染者</span><span class="number_2">3333</span
            ><span>较上日:<span class="number_2"></span></span
          ></van-grid-item>
          <van-grid-item icon="photo-o" text="文字" class="van-grid-item_3"
            ><span>境外输入</span><span class="number_3">3333</span
            ><span>较上日:<span class="number_3"></span></span
          ></van-grid-item>
          <van-grid-item icon="photo-o" text="文字" class="van-grid-item_4"
            ><span>累计确诊</span><span class="number_4">3333</span
            ><span>较上日:<span class="number_4"></span></span
          ></van-grid-item>
          <van-grid-item icon="photo-o" text="文字" class="van-grid-item_5"
            ><span>累计治愈</span><span class="number_5">3333</span
            ><span>较上日:<span class="number_5"></span></span
          ></van-grid-item>
          <van-grid-item icon="photo-o" text="文字" class="van-grid-item_6"
            ><span>累计死亡</span><span class="number_6">3333</span
            ><span>较上日:<span class="number_6"></span></span
          ></van-grid-item>
        </van-grid>
        <h4>统计截止至:2020-12-08</h4>
      </div>

      <!-- 全国疫情概况 -->
      <div class="data_country">
        <h3>中国疫情地图</h3>
        <ChinaMap></ChinaMap>
        <h3>中国疫情趋势图</h3>
        <ChinaLine></ChinaLine>
      </div>
    </div>
  </div>
</template>

<script>
import { Grid, GridItem } from "vant";
import ChinaMap from "../components/ChinaDataMap.vue";
import ChinaLine from "../components/ChinaDataLine.vue";

export default {
  data() {
    return {};
  },
  components: {
    [Grid.name]: Grid,
    [GridItem.name]: GridItem,
    ChinaMap,
    ChinaLine,
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
      width: 100%;
      // background-color: pink;
      left: 0;
      top: 30px;
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
    padding: 5px;
    .data_country_daily {
      width: 100%;
      display: flex;
      flex-direction: column;
      text-align: center;
      h3 {
        font-size: 18px;
        color: #1d1c1c;
        margin: 0 0 5px 0;
      }
      h4 {
        margin: 0;
        padding: 0;
        font-size: 12px;
        color: rgb(124, 124, 124);
      }
      .vanGrid {
        .van-grid-item__content--center {
          border: 0.5px solid #ddd;
          border-radius: 5px;
          padding: 8px 0;
          :nth-child(1) {
            color: rgb(34, 34, 34);
            font-size: 13px;
          }
          :nth-child(2) {
            font-size: 24px;
          }
          :nth-child(3) {
            font-size: 12px;
            color: rgb(124, 124, 124);
          }
        }
        .van-grid-item_1 {
          .van-grid-item__content--center {
            background-color: rgb(253, 241, 241);
            .number_1 {
              color: rgb(242, 58, 59);
            }
          }
        }
        .van-grid-item_2 {
          .van-grid-item__content--center {
            background-color: rgb(250, 242, 246);
            .number_2 {
              color: rgb(202, 63, 129);
            }
          }
        }
        .van-grid-item_3 {
          .van-grid-item__content--center {
            background-color: rgb(252, 244, 240);
            .number_3 {
              color: rgb(240, 89, 38);
            }
          }
        }
        .van-grid-item_4 {
          .van-grid-item__content--center {
            background-color: rgb(253, 241, 241);
            .number_4 {
              color: rgb(204, 30, 30);
            }
          }
        }
        .van-grid-item_5 {
          .van-grid-item__content--center {
            background-color: rgb(241, 248, 244);
            .number_5 {
              color: rgb(23, 139, 90);
            }
          }
        }
        .van-grid-item_6 {
          .van-grid-item__content--center {
            background-color: rgb(243, 246, 248);
            .number_6 {
              color: rgb(78, 90, 101);
            }
          }
        }
      }
    }
    .data_country {
      h3 {
        font-size: 20px;
        color: #020202;
        margin: 5px 0;
        border-left: 5px solid red;
        padding-left: 5px;
      }
    }
  }
}
</style>
