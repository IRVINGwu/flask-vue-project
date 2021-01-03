<template>
  <div class="world_country">

    <h3>{{ id }}当日疫情趋势</h3>
        <div class="data_country_daily">
          <van-grid :column-num="3" :gutter="6" class="vanGrid" :border="true">
            <van-grid-item icon="photo-o" text="文字" class="van-grid-item_1"><span>现有确诊</span><span
              class="number_1" v-cloak>{{ todayNum.today.confirm }}</span></van-grid-item>

            <van-grid-item icon="photo-o" text="文字" class="van-grid-item_2"><span>现有治愈</span><span
              class="number_2" v-cloak>{{ todayNum.today.heal }}</span></van-grid-item>

            <van-grid-item icon="photo-o" text="文字" class="van-grid-item_3"><span>现有死亡</span><span
              class="number_3" v-cloak>{{ todayNum.today.dead }}</span></van-grid-item>

            <van-grid-item icon="photo-o" text="文字" class="van-grid-item_4"><span>累计确诊</span><span
              class="number_4" v-cloak>{{ todayNum.total.confirm }}</span></van-grid-item>

            <van-grid-item icon="photo-o" text="文字" class="van-grid-item_5"><span>累计治愈</span><span
              class="number_5" v-cloak>{{ todayNum.total.heal }}</span></van-grid-item>

            <van-grid-item icon="photo-o" text="文字" class="van-grid-item_6"><span>累计死亡</span><span
              class="number_6" v-cloak>{{ todayNum.total.dead }}</span></van-grid-item>
          </van-grid>
          <h4 v-cloak>统计截止至:{{ todayNum.lastUpdateTime }}</h4>
        </div>

    <h3>{{ id }}疫情发展趋势</h3>
    <div id="country_line" class="line" style="width: 100%;height: 400px;">
    </div>

    <h3>{{ id }}疫情详情</h3>
    <div id="country_table" class="table">
      <table class="table table-hover">
        <thead class="thead-dark">
        <tr>
          <th scope="col">日期</th>
          <th scope="col">累计确诊</th>
          <th scope="col">累计治愈</th>
          <th scope="col">累计死亡</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(item,index) in tablelist" :key="index">
          <td>{{ item.date | formatDate }}</td>
          <td>{{ item.confirm }}</td>
          <td>{{ item.heal }}</td>
          <td>{{ item.dead }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>

</template>

<script>
import echarts from '../../assets/js/echarts.min.js'
import { Grid, GridItem } from "vant"

export default {
  data () {
    return {
      tablelist: [],
      todayNum: {},
      xdata: [],
      ydata1: [],
      ydata2: [],
      ydata3: [],
      optionline: {},
    }
  },
  methods: {
    async get_data () {
      const body = await this.$http.get('/worldDailyData/' + this.id)

      // TODO:加了具体数字的显示之后,echarts图显示不出来了,不知道是什么原因,如果实在不行的话,就不加了
      const body1 = await this.$http.get('/worldDaily')
      if (body1.status === 200) {
        let table = body1.data
        // console.log(table)
        for (let key in table) {
          if (table[key].name == this.id) {
            // console.log(typeof table[key])
            this.todayNum = table[key]
          }
        }
      }
      if (body == '详情暂时未找到') {
        let myChart = document.getElementById('country_line')
        myChart.innerHTML = '不好意思，本地区暂未提供疫情趋势图'
        myChart.style.textAlign = 'center'
      } else {
        if (body.status === 200) {
          for (let key in body.data) {
            let data = body.data[key]
            // console.log(data)
            let date = data.日期
            let confirm = data.确诊病例
            let heal = data.康复病例
            let dead = data.死亡病例
            const obj = {
              date: date,
              confirm: confirm,
              heal: heal,
              dead: dead
            }
            // 创建图表所需数据
            this.xdata.push(date)
            this.ydata1.push(confirm)
            this.ydata2.push(heal)
            this.ydata3.push(dead)
            // 创建表格所需数据
            this.tablelist.push(obj)
          }
          this.draw()
        }
      }
    },
    draw () {
      // 创建optionline
      this.optionline = {
        // title:{
        //   text:this.id + '疫情趋势',
        // },
        tooltip: {
          trigger: 'axis',
          axisPointer: {lineStyle: {color: 'rgb(239, 243, 250)'},},
          backgroundColor: '#fff',
          textStyle: {color: '#999', fontSize: 12,},
          extraCssText: 'box-shadow: 0 2px 10px #ccc;'
        },
        legend: {
          data: [
            '累计确诊', '累计治愈', '累计死亡'
          ],
          show: true,
          top: '20',
        },
        xAxis: [
          {
            type: 'category',
            data: this.xdata
          }
        ],
        yAxis: [{
          type: 'value',
          axisLabel: {
            formatter: function (num) {
              let numStr = num.toString()
              // 万以内直接返回
              if (numStr.length < 5) {
                return numStr
              }
              //大于8位数是亿
              else if (numStr.length > 8) {
                let decimal = numStr.substring(numStr.length - 8, numStr.length - 8)
                return parseFloat(parseInt(num / 100000000) + '.' + decimal) + '亿'
              }
              //大于6位数是十万 (以10W分割 10W以下全部显示)
              else if (numStr.length > 5) {
                let decimal = numStr.substring(numStr.length - 4, numStr.length - 4)
                return parseFloat(parseInt(num / 10000) + '.' + decimal) + '万'
              } else if (numStr.length == 5) {
                let decimal = numStr.substring(numStr.length - 3, numStr.length - 4)
                return parseFloat(parseInt(num / 10000) + '.' + decimal) + '万'
              }
            }
          }
        }],
        dataZoom: [{
          type: 'slider',
          start: 0,
          end: 100,
          bottom: 0,
          show: true
        }],
        series: [
          {
            name: '累计确诊',
            type: 'line',
            data: this.ydata1
          },
          {
            name: '累计治愈',
            type: 'line',
            data: this.ydata2
          },
          {
            name: '累计死亡',
            type: 'line',
            data: this.ydata3
          }
        ],
        grid: {
          x: 50,
          x2: 25,
        },
      }
      //初始化表格
      let chartline = echarts.init(document.getElementById('country_line'))
      chartline.setOption(this.optionline)
    },
    // async get_numList () {
    //   const body = await this.$http.get('/worldDaily')
    //   if (body.status === 200) {
    //     let table = body.data
    //     // console.log(table)
    //     for (let key in table) {
    //       if (table[key].name == this.id) {
    //         // console.log(typeof table[key])
    //         this.todayNum = table[key]
    //       }
    //     }
    //   }
    // }
  },
  mounted () {
    this.get_data();
    // this.get_numList();
  },
  props: ['id'],
  components:{
    [Grid.name]: Grid,
    [GridItem.name]: GridItem,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.world_country {
  //margin-top: 46px;
  margin-bottom: 35px;
  padding: 5px;

  h3 {
    font-size: 20px;
    color: #020202;
    margin: 10px 0;
    border-left: 5px solid red;
    padding: 0 0 0 5px;
  }

  //当日疫情数字
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

  //疫情数据表格
  .table {

    table {
      thead {
        height: 26px;

        tr {
          th {
            border: 0;
            font-size: 0.625rem;
            padding: 15px 0;
            text-align: center;
          }

          th:nth-child(1) {
            background-color: rgb(245, 245, 245);
            color: rgb(34, 34, 34);
            text-align: left;
            padding-left: 0.8rem;
          }

          th:nth-child(2) {
            background-color: rgb(252, 242, 232);
            color: rgb(255, 114, 60);
          }

          th:nth-child(3) {
            background-color: rgb(233, 247, 236);
            color: rgb(132, 139, 80);
          }

          th:nth-child(4) {
            background-color: rgb(243, 246, 248);
            color: rgb(78, 90, 101);
          }

        }
      }

      tbody {
        tr {
          font-size: 0.625rem;
          text-align: center;

          td {
            border: 0;
            border-bottom: 1px solid #dee2e6;
          }

          td:nth-child(1) {
            text-align: left;
          }
        }
      }
    }
  }
}

</style>
