<template>
  <div class="world_container">
    <div class="world_header">
      <img src="../assets/images/world_banner.png" alt="" />
      <div class="header_content">
        <span>山川异域 日月同天</span>
        <span>covid-19世界疫情实时播报</span>
        <span>数据来源：WHO及权威媒体报道</span>
      </div>
    </div>

    <div class="world_content">
<!--      当日世界疫情数据展示-->
      <div class="data_country_daily">
        <h3>世界疫情数据</h3>
        <van-grid :column-num="3" :gutter="6" class="vanGrid" :border="true">
          <van-grid-item icon="photo-o" text="文字" class="van-grid-item_4"
          ><span>累计确诊</span><span class="number_4">{{ totalConfirm }}</span
          ><span>较上日:<span class="number_4">{{ todayConfirm | formatNumber}}</span></span
          ></van-grid-item>
          <van-grid-item icon="photo-o" text="文字" class="van-grid-item_5"
          ><span>累计治愈</span><span class="number_5">{{ totalHeal }}</span
          ><span>较上日:<span class="number_5">{{ todayHeal | formatNumber}}</span></span
          ></van-grid-item>
          <van-grid-item icon="photo-o" text="文字" class="van-grid-item_6"
          ><span>累计死亡</span><span class="number_6">{{ totalDead }}</span
          ><span>较上日:<span class="number_6">{{ todayDead | formatNumber}}</span></span
          ></van-grid-item>
        </van-grid>
        <h4>统计截止至:{{ date }}</h4>
      </div>

<!--      展示世界疫情发展概况-->
      <div class="world_line">
        <h3>世界疫情趋势图</h3>
        <WorldLine></WorldLine>
        <h3>世界疫情详情</h3>
        <WorldTable></WorldTable>
      </div>
    </div>
  </div>
</template>

<script>
import WorldLine from "../components/WorldDataLine.vue"
import WorldTable from "../components/WorldDataTable.vue"
import { Grid, GridItem } from "vant";

export default {
  data(){
    return{
      todayConfirm:'',
      todayDead:'',
      todayHeal:'',
      totalConfirm:'',
      totalDead:'',
      totalHeal:'',
      date:''
    }
  },
  methods:{
    async get_worldData(){
      const body = await this.$http.get('/worldSum')
      if(body.status == 200){
        let lastData = body.data.data.slice(-1)[0]
        let secondLastData = body.data.data.slice(-2,-1)[0]
        // console.log(secondLastData.date)
        this.date = lastData.date.slice(0,10)
        this.totalConfirm = lastData.确诊病例
        this.totalDead = lastData.死亡病例
        this.totalHeal = lastData.康复病例
        this.todayConfirm  = lastData.确诊病例 - secondLastData.确诊病例
        this.todayDead = lastData.死亡病例 - secondLastData.死亡病例
        this.todayHeal = lastData.康复病例 - secondLastData.康复病例
      }
    }
  },
  components:{
    WorldLine,
    WorldTable,
    [Grid.name]: Grid,
    [GridItem.name]: GridItem,
  },
  mounted () {
    this.get_worldData()
  }
};
</script>

<style lang="scss">
h3 {
  margin: 0;
  padding: 0;
}
.world_container {
  //margin-top: 46px;
  margin-bottom: 35px;
  .world_header {
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

  .world_content{
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
        border: 0;
      }
      h4 {
        margin: 5px 0;
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
            font-size: 20px;
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

    h3 {
      font-size: 20px;
      color: #020202;
      margin: 10px 0;
      border-left: 5px solid red;
      padding-left: 5px;
    }
  }
}
</style>
