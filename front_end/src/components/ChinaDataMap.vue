<template>
  <div class="china_map_container">
    <div class="map">
      <!-- 中国疫情现有确诊热力图 -->
      <div id="container_daily" class="china_map" v-show="mapShow"></div>
      <!-- 中国疫情累计确诊热力图 -->
      <div id="container_sum" class="china_map" v-show="!mapShow">nihao</div>
    </div>

    <!-- 两个按钮用于切换显示热力图 -->
    <div class="map_button">
      <van-button plain type="primary" class="button_item" @click="showDaily"
      >现有确诊
      </van-button
      >
      <van-button plain type="primary" class="button_item" @click="showSum"
      >累计确诊
      </van-button
      >
    </div>
  </div>
</template>

<script>
import echarts from '../assets/js/echarts.min.js'
import {Button} from 'vant'

export default {
  data () {
    return {
      mapShow: true,
    }
  },
  mounted () {
    this.$nextTick(function () {
      // this.drawLine();
      this.creatDailyChart()
      this.getSumChart()
    })
  },
  methods: {
    //今日确诊热力图
    async creatDailyChart () {
      // 获取地图所需的json数据
      const result = await this.$http.get('/mapJson/china')
      echarts.registerMap('china', result.data)
      // console.log(result.data)
      // 获取疫情数据
      const body = await this.$http.get('/chinaProvinceDaily')
      // console.log(body.data)
      // 创建dataMap
      let dataMap = []
      // 因为body.data的类型是对象，所以要用循环对象的方法来做
      for (let key in body.data) {
        let name = body.data[key].省份名
        let num = body.data[key].今日确诊
        let obj = {
          name: name,
          value: num
        }
        dataMap.push(obj)
      }
      // console.log(dataMap)
      // 需要在页面上直接标记出来的城市
      let specialMap = []
      // 对dataMap进行处理，使其可以直接在页面上展示
      for (let i = 0; i < specialMap.length; i++) {
        for (let j = 0; j < dataMap.length; j++) {
          if (specialMap[i] == dataMap[j].name) {
            dataMap[j].selected = true
            break
          }
        }
      }
      //Echart的配置选项
      let option = {
        tooltip: {
          //悬浮时显示
          formatter: function (params) {
            var info = '<p style="font-size:16px;color:white;padding-left: 0;width: 108px;height: 30px;text-align: center;padding-top: 4px;">' + params.name + '<br>'+ '今日确诊：' + params.value + '</p>'
            return info
          },
          backgroundColor: 'rgba(0,0,0,0.5)', //提示标签背景颜色
          textStyle: {color: '#fff'}, //提示标签字体颜色
        },
        //左侧小导航图标
        visualMap: {
          show: true,
          x: 'left',
          // y: 'center',
          bottom: '0%', //组件离容器下侧的距离,'20%'
          itemWidth: 5, //图形的宽度，即长条的宽度。
          itemHeight: 5, //图形的高度，即长条的高度。
          textGap: 5, //两端文字主体之间的距离，单位为px
          textStyle: {
            //文本样式
            fontSize: 10,
          },
          itemGap: 4, //每两个图元之间的间隔距离，单位为px
          splitList: [
            {start: 5000, end: 10000},
            {start: 1000, end: 5000},
            {start: 500, end: 1000},
            {start: 100, end: 500},
            {start: 10, end: 99},
            {start: 1, end: 9},
            {start: 0, end: 0},
          ],
          color: [
            '#663366',
            '#990033',
            '#ff0033',
            '#99cccc',
            '#cccc00',
            '#f6c7a3',
            'rgb(226, 235, 244)',
          ],
        },
        series: [
          {
            name: '中国',
            type: 'map',
            zoom: 1.2, //这里是关键，一定要放在 series中，地图缩放比例的配置
            mapType: 'china',
            label: {
              //地图中的文字
              normal: {
                //正常显示
                show: true, //显示省份标签
                textStyle: {
                  fontSize: 6,
                  color: '#2b2b2b',
                },
              },
            },
            data: dataMap,
          },
        ],
      }
      //初始化echarts实例
      let myChart = echarts.init(document.getElementById('container_daily'))
      //使用制定的配置项和数据显示图表
      myChart.setOption(option)
    },
    async getSumChart(){
      // 获取地图所需的json数据
      const result = await this.$http.get('/mapJson/china')
      echarts.registerMap('china', result.data)
      // console.log(result.data)
      // 获取疫情数据
      const body = await this.$http.get('/chinaProvinceDaily')
      // console.log(body.data)
      // 创建dataMap
      let dataMap = []
      // 因为body.data的类型是对象，所以要用循环对象的方法来做
      for (let key in body.data) {
        let name = body.data[key].省份名
        let num = body.data[key].总确诊数
        let obj = {
          name: name,
          value: num
        }
        dataMap.push(obj)
      }
      // console.log(dataMap)
      // 需要在页面上直接标记出来的城市
      let specialMap = []
      // 对dataMap进行处理，使其可以直接在页面上展示
      for (let i = 0; i < specialMap.length; i++) {
        for (let j = 0; j < dataMap.length; j++) {
          if (specialMap[i] == dataMap[j].name) {
            dataMap[j].selected = true
            break
          }
        }
      }
      //Echart的配置选项
      let option = {
        tooltip: {
          //悬浮时显示
          formatter: function (params) {
            var info = '<p style="font-size:14px;color:white;width: 108px;height: 30px;text-align: center;padding-top: 4px;padding-left: 0;">' + params.name + '<br>'+ '累计确诊：' + params.value + '</p>'
            return info
          },
          backgroundColor: 'rgba(0,0,0,0.5)', //提示标签背景颜色
          textStyle: {color: '#fff'}, //提示标签字体颜色
        },
        //左侧小导航图标
        visualMap: {
          show: true,
          x: 'left',
          // y: 'center',
          bottom: '0%', //组件离容器下侧的距离,'20%'
          itemWidth: 5, //图形的宽度，即长条的宽度。
          itemHeight: 5, //图形的高度，即长条的高度。
          textGap: 5, //两端文字主体之间的距离，单位为px
          textStyle: {
            //文本样式
            fontSize: 10,
          },
          itemGap: 4, //每两个图元之间的间隔距离，单位为px
          splitList: [
            {start: 100001, end: 500000},
            {start: 50001, end: 100000},
            {start: 10001, end: 50000},
            {start: 1001, end: 10000},
            {start: 101, end: 1000},
            {start: 1, end: 100},
            {start: 0, end: 0},
          ],
          color: [
            '#663366',
            '#990033',
            '#ff0033',
            '#99cccc',
            '#cccc00',
            '#f6c7a3',
            'rgb(226, 235, 244)',
          ],
        },
        series: [
          {
            name: '中国',
            type: 'map',
            zoom: 1.2, //这里是关键，一定要放在 series中，地图缩放比例的配置
            mapType: 'china',
            label: {
              //地图中的文字
              normal: {
                //正常显示
                show: true, //显示省份标签
                textStyle: {
                  fontSize: 6,
                  color: '#2b2b2b',
                },
              },
            },
            data: dataMap,
          },
        ],
      }
      //初始化echarts实例
      let chart = document.getElementById('container_sum')

      //用这个就让切换时图表不会出现width:100px的情况，inline-block和block都可以，这样会在初始化的时候就出现
      //为了解决在初始化时出现两张图表的情况，在.map中，将溢出部分隐藏即可
      chart.style.display = 'inline-block'
      let myChart = echarts.init(chart)
      //使用制定的配置项和数据显示图表
      myChart.resize()
      myChart.setOption(option,true)
    },
    showDaily () {
      this.mapShow = true
    },
    showSum () {
      this.mapShow = false
    },
  },
  props: {},
  components: {
    [Button.name]: Button,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.china_map_container {
  padding: 0;
  margin: 0;
  box-sizing: border-box;

  .map{
    width: 100%;
    height: 300px;
    overflow: hidden;
    .china_map {
      width: 100%;
      height: 300px;
      border: 1px solid #ccc;
    }
  }


  .map_button {
    display: flex;
    justify-content: space-between;
    margin: 5px;

    :nth-child(1) {
      margin-right: 10px;
    }

    .button_item {
      flex: 1;
      border-radius: 5px;
      border: 1px solid rgb(210, 210, 210);
      font-size: 16px;
      color: rgb(72, 70, 71);
    }

    .button_active {
      border-color: red;
      color: red;
    }
  }
}
</style>
