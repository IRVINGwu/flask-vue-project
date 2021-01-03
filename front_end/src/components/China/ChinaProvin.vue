<template>
  <div class="china_province">
    <h3>{{ id }}疫情地图</h3>
    <div id="province_map" class="map" style="width: 100%;height: 400px;">
    </div>
    <h3>{{ id }}疫情详情</h3>
    <div id="province_table" class="table">
      <table class="table table-hover">
        <thead class="thead-dark">
        <tr>
          <th scope="col">城市</th>
          <th scope="col">现有确诊</th>
          <th scope="col">累计确诊</th>
          <th scope="col">治愈</th>
          <th scope="col">死亡</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(item,index) in tablelist" :key="index">
          <td v-text="item.name === '未明确地区' ? id : item.name"></td>
          <td>{{ item.todayConfirm }}</td>
          <td>{{ item.totalConfirm }}</td>
          <td>{{ item.totalHeal }}</td>
          <td>{{ item.totalDead }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import echarts from '@/assets/js/echarts.min'

export default {
  data () {
    return {
      tablelist: [],
      dataMap:[],
    }
  },
  methods: {
    // 获取数据来做地图和表格
    async get_Data () {
      // 获取地图所需的json数据
      const result = await this.$http.get('/mapJson/' + this.id)
      echarts.registerMap(this.id, result.data)
      // console.log(result.data)
      // 获取疫情数据
      const body = await this.$http.get('/chinaProvinCity/' + this.id)
      // console.log(body.data)


      // 创建地图所需的 dataMap
      let name = ''
      if (this.id == '上海' || this.id == '天津' || this.id == '重庆' || this.id == '北京') {
        // 因为body.data的类型是对象，所以要用循环对象的方法来做
        for (let key in body.data) {
          let data = body.data[key][0]
          // console.log(data)
          name = data.name + '区'
          let value = data.today.confirm
          const obj = {
            name: name,
            value: value
          }
          this.dataMap.push(obj)
        }
        this.draw()
      }else if(this.id == '香港' || this.id == '澳门' || this.id == '台湾'){
        // console.log(body.data[0][0])
        let myChart = document.getElementById('province_map')
        myChart.innerHTML = '不好意思，本地区暂未提供疫情地图热力图'
        myChart.style.textAlign = 'center'
      } else{
        // 因为body.data的类型是对象，所以要用循环对象的方法来做
        for (let key in body.data) {
          let data = body.data[key][0]
          // console.log(data)
          if (data.name == '神农架林区') {
            name = data.name
          } else if (data.name == '恩施州') {
            name = '恩施土家族苗族自治州'
          } else {
            name = data.name + '市'
          }
          let value = data.today.confirm
          const obj = {
            name: name,
            value: value
          }
          this.dataMap.push(obj)
        }
        this.draw()
      }
      // console.log(this.dataMap)

      // 创建表格所需的数据
      for (let key in body.data) {
        let data = body.data[key][0]
        // console.log(body.data[key][0])
        let name = data.name
        let todayConfirm = data.today.confirm
        let totalConfirm = data.total.confirm
        let totalHeal = data.total.heal
        let totalDead = data.total.dead
        const obj = {
          name: name,
          todayConfirm:todayConfirm,
          totalConfirm:totalConfirm,
          totalHeal:totalHeal,
          totalDead:totalDead,
        }
        this.tablelist.push(obj)
      }
      // console.log(this.tablelist)
    },
    draw(){
      // Echart的配置选项
      let option = {
        tooltip: {
          //悬浮时显示
          formatter: function (params) {
            let info = '<p style="font-size:16px;color:white;padding-left: 0;width: 108px;height: 30px;text-align: center;padding-top: 4px;">' + params.name.toString() + '<br>' + '今日确诊：' + params.value + '</p>'
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
            {start: 1000, end: 10000},
            {start: 200, end: 1000},
            {start: 100, end: 200},
            {start: 50, end: 100},
            {start: 10, end: 50},
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
            name: this.id,
            type: 'map',
            zoom: 1.2, //这里是关键，一定要放在 series中，地图缩放比例的配置
            mapType: this.id,
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
            data: this.dataMap,
          },
        ],
        grid: {
          x:50,
          x2: 25,
        },
      }
      //初始化echarts实例
      let myChart = echarts.init(document.getElementById('province_map'))
      //使用制定的配置项和数据显示图表
      myChart.setOption(option)
    },
  },
  mounted () {
    this.get_Data()
  },
  props: ['id'],
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.china_province {
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

  .table {
    padding: 3px;

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
            background-color: rgb(253, 238, 238);
            color: rgb(246, 104, 133);
          }

          th:nth-child(4) {
            background-color: rgb(233, 247, 236);
            color: rgb(132, 139, 80);
          }

          th:nth-child(5) {
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
