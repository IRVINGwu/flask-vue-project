<template>
  <div class="china_line_container">
    <van-tabs type="card" animated @click="onClick" id="tabs">
      <van-tab
        title="新增趋势"
        id="chartline1"
        style="width:100%; height:400px;"
      ></van-tab>
      <van-tab
        title="确诊趋势"
        id="chartline2"
        style="width:100%; height:400px;"
      >
      </van-tab>
      <van-tab
        title="治疗趋势"
        id="chartline3"
        style="width:100%; height:400px;"
      ></van-tab>
    </van-tabs>
  </div>
</template>

<script>
import echarts from "../../assets/js/echarts.min.js";
import { Tab, Tabs } from "vant";

export default {
  data() {
    return {
      current: 0,
      // 所需要的x轴和y轴数据
      xdata:[],
      ydata1:[],
      ydata2:[],
      ydata3:[],
      ydata4:[],
      ydata5:[],
      ydata6:[],
      // 制图所需要的数据
      optionline1:{},
      optionline2:{},
      optionline3:{},
    };
  },
  created() {
    this.get_chinaSum();
  },
  methods: {
    onClick(name, title='新增趋势') {
      let line1 = document.getElementById("chartline1")
      let line2 = document.getElementById("chartline2")
      let line3 = document.getElementById("chartline3")
      line1.style.display = 'block'
      line2.style.display = 'block'
      line3.style.display = 'block'

      let chartline1 = echarts.init(line1);
      let chartline2 = echarts.init(line2);
      let chartline3 = echarts.init(line3);
      // chartline1.setOption(this.optionline1);
      if (title == "确诊趋势") {
        chartline2.setOption(this.optionline2);
      } else if (title == "治疗趋势") {
        chartline3.setOption(this.optionline3);
      } else if(title == "新增趋势"){
        chartline1.setOption(this.optionline1);
        chartline1.resize()
      }
    },

    //获取制图所需要的数据
    async get_chinaSum(){
      const body = await this.$http.get('/chinaSum')
      if(body.status === 200){
        // console.log(body.data)
        let result = body.data
        for (let i = 0; i < result.length; i++) {
          this.xdata.push(result[i].date)
          //新增确诊和新增疑似病例对比
          this.ydata1.push(result[i].today.confirm)
          this.ydata2.push(result[i].today.suspect)
          //新增确诊和累计确诊病例对比
          this.ydata3.push(result[i].today.confirm)
          this.ydata4.push(result[i].total.confirm)
          //累计治愈和累计死亡病例对比
          this.ydata5.push(result[i].total.heal)
          this.ydata6.push(result[i].total.dead)
        }
      }
      // console.log(this.ydata5)
      // 创建optionline
      this.optionline1 = {
        // title:{
        //   text:"新增确诊与新增疑似",
        // },
        tooltip:{
          trigger: 'axis',
          axisPointer:{lineStyle:{color:'rgb(239, 243, 250)'},},
          backgroundColor:'#fff',
          textStyle:{color:'#999', fontSize:12,},
          extraCssText: 'box-shadow: 0 2px 10px #ccc;'
        },
        legend:{
          data:[
              '新增确诊','新增疑似'
          ],
          show: true,
          top:"20",
        },
        xAxis: [
          {
            type: 'category',
            data: this.xdata
          }
        ],
        yAxis:[{
          type: 'value'
        }],
        dataZoom: [{
          type: 'slider',
          start: 0,
          end: 100,
          bottom: 0,
          show: true
        }],
        series:[
          {
            name:'新增确诊',
            type:"line",
            data:this.ydata1
          },
          {
            name:'新增疑似',
            type:"line",
            data:this.ydata2
          }
        ],
        grid: {
          x:50,
          x2: 25,
        },
      }

      this.optionline2 = {
        // title:{
        //   text:"新增确诊与累计确诊",
        // },
        tooltip:{
          trigger: 'axis',
          axisPointer:{lineStyle:{color:'rgb(239, 243, 250)'},},
          backgroundColor:'#fff',
          textStyle:{color:'#999', fontSize:12,},
          extraCssText: 'box-shadow: 0 2px 10px #ccc;'
        },
        legend:{
          data:[
            '新增确诊','累计确诊'
          ],
          show: true,
          top:"20",
        },
        xAxis: [
          {
            type: 'category',
            data: this.xdata
          }
        ],
        yAxis:[{
          type: 'value'
        }],
        dataZoom: [{
          type: 'slider',
          start: 0,
          end: 100,
          bottom: 0,
          show: true
        }],
        series:[
          {
            name:'新增确诊',
            type:"line",
            data:this.ydata3
          },
          {
            name:'累计确诊',
            type:"line",
            data:this.ydata4
          }
        ],
        grid: {
          x:50,
          x2: 25,
        },
      }

      this.optionline3 = {
        // title:{
        //   text:"累计治愈与累计死亡",
        // },
        tooltip:{
          trigger: 'axis',
          axisPointer:{lineStyle:{color:'rgb(239, 243, 250)'},},
          backgroundColor:'#fff',
          textStyle:{color:'#999', fontSize:12,},
          extraCssText: 'box-shadow: 0 2px 10px #ccc;'
        },
        legend:{
          data:[
            '累计治愈','累计死亡'
          ],
          show: true,
          top:"20",
        },
        xAxis: [
          {
            type: 'category',
            data: this.xdata
          }
        ],
        yAxis:[{
          type: 'value'
        }],
        dataZoom: [{
          type: 'slider',
          start: 0,
          end: 100,
          bottom: 0,
          show: true
        }],
        series:[
          {
            name:'累计治愈',
            type:"line",
            data:this.ydata5
          },
          {
            name:'累计死亡',
            type:"line",
            data:this.ydata6
          }
        ],
        grid: {
          x:50,
          x2: 25,
        },
      }

      // 这句非常重要，我在查了很多资料之后才知道的，原来onClick()里面在初始化的时候没有获取到
      // 数据，结果就没有办法渲染出图表，这里的意思是，先获取数据，然后作图
      this.onClick()
    }

  },
  props: {},
  mounted() {},
  destroyed() {},
  components: {
    [Tab.name]: Tab,
    [Tabs.name]: Tabs,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.china_line_container {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  van-tabs{
    width: 100%;
    height: 400px;
    display: flex;
    overflow: hidden;
    van-tab{
      width: 100%;
      height: 400px;
      display: block;
    }
  }
}
</style>
