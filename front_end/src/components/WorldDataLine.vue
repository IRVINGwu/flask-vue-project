<template>
  <div class="world_line">
    <div id="line1" class="line" style="width: 100%;height: 400px;"></div>
    <div id="line2" class="line" style="width: 100%;height: 400px;"></div>
    <div id="line3" class="line" style="width: 100%;height: 400px;"></div>
  </div>
</template>

<script>
import echarts from '@/assets/js/echarts.min'

export default {
  name: 'WorldDataLine',
  data () {
    return {
      // 所需要的x轴和y轴数据
      xdata: [],
      ydata1: [],
      ydata2: [],
      ydata3: [],
      // 制图所需要的数据
      optionline1: {},
      optionline2: {},
      optionline3: {},
    }
  },
  created () {
    this.get_worldSum()
  },
  methods: {
    draw () {
      let line1 = document.getElementById('line1')
      let line2 = document.getElementById('line2')
      let line3 = document.getElementById('line3')
      line1.style.display = 'block'
      line2.style.display = 'block'
      line3.style.display = 'block'
      let chartline1 = echarts.init(line1)
      let chartline2 = echarts.init(line2)
      let chartline3 = echarts.init(line3)
      chartline1.setOption(this.optionline1)
      chartline2.setOption(this.optionline2)
      chartline3.setOption(this.optionline3)
    },
    //获取制图所需要的数据
    async get_worldSum () {
      const body = await this.$http.get('/worldSum')
      if (body.status == 200) {
        // console.log(body.data.data)
        let result = body.data.data
        for (let i = 0; i < result.length; i++) {
          this.xdata.push(result[i].date.slice(0, 10))
          this.ydata1.push(result[i].确诊病例)
          this.ydata2.push(result[i].死亡病例)
          this.ydata3.push(result[i].康复病例)
        }
      }
      // 创建optionline
      this.optionline1 = {
        title: {
          text: '累计确诊',
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {lineStyle: {color: 'rgb(239, 243, 250)'},},
          backgroundColor: '#fff',
          textStyle: {color: '#999', fontSize: 12,},
          extraCssText: 'box-shadow: 0 2px 10px #ccc;'
        },
        legend: {
          data: [
            '累计确诊'
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

          // 这里是为了让y轴数字规范一下，很重要
          axisLabel: {
            formatter: function(num){
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
        ],

        // 这里是为了让图表右边的空白少一点，看上去好看一些
        grid: {
          x:50,
          x2: 25,
        },
      }
      this.optionline2 = {
        title: {
          text: '累计死亡',
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {lineStyle: {color: 'rgb(239, 243, 250)'},},
          backgroundColor: '#fff',
          textStyle: {color: '#999', fontSize: 12,},
          extraCssText: 'box-shadow: 0 2px 10px #ccc;'
        },
        legend: {
          data: [
            '累计死亡'
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
            formatter: function(num){
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
            name: '累计死亡',
            type: 'line',
            data: this.ydata2
          },
        ],
        grid: {
          x:50,
          x2: 25,
        },
      }

      this.optionline3 = {
        title: {
          text: '累计治愈',
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {lineStyle: {color: 'rgb(239, 243, 250)'},},
          backgroundColor: '#fff',
          textStyle: {color: '#999', fontSize: 12,},
          extraCssText: 'box-shadow: 0 2px 10px #ccc;'
        },
        legend: {
          data: [
            '累计治愈'
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
            formatter: function(num){
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
            name: '累计治愈',
            type: 'line',
            data: this.ydata3
          },
        ],
        grid: {
          x:50,
          x2: 25,
        },
      }
      // 这句非常重要，我在查了很多资料之后才知道的，原来onClick()里面在初始化的时候没有获取到
      // 数据，结果就没有办法渲染出图表，这里的意思是，先获取数据，然后作图
      this.draw()
    },
  },
  mounted () {
  },
}
</script>

<style scoped lang="scss">
.world_line{
  .line{
    margin: 15px 0;
  }
}
</style>