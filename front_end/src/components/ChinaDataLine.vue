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
import echarts from "../assets/js/echarts.min.js";
import axios from "axios";
import { Tab, Tabs } from "vant";

export default {
  data() {
    return {
      current: 0,
      optionline: {
        title: {
          text: "ECharts 数据统计",
        },
        tooltip: {},
        legend: {
          data: ["用户来源"],
        },
        xAxis: {
          data: ["Android", "IOS", "PC", "Ohter"],
        },
        yAxis: {},
        series: [
          {
            name: "访问量",
            type: "line", //设置图表主题
            data: [500, 200, 360, 100],
          },
        ],
      },
    };
  },
  created() {
    // this.$nextTick(() => {
    //   this.drawLine1();
    //   this.drawLine2();
    //   this.drawLine3();
    // });
  },
  methods: {
    onClick(name, title) {
      let chartline1 = echarts.init(document.getElementById("chartline1"));
      let chartline2 = echarts.init(document.getElementById("chartline2"));
      let chartline3 = echarts.init(document.getElementById("chartline3"));
      if (title == "确诊趋势") {
        // console.log(chartline2);
        // console.log("确诊趋势");
        chartline2.setOption(this.optionline);
      } else if (title == "治疗趋势") {
        // console.log("治疗趋势");
        // console.log(chartline3);
        chartline3.setOption(this.optionline);
      } else {
        //绘制图表
        chartline1.setOption(this.optionline);
      }
    },
    drawLine1() {
      //基于准本好的DOM，初始化echarts实例
      let chartline1 = echarts.init(document.getElementById("chartline1"));
      //绘制图表
      chartline1.setOption(this.optionline);
    },
    drawLine2() {
      //基于准本好的DOM，初始化echarts实例
      let line2 = document.getElementById("chartline2");
      if (!line2) {
        return false;
      }
      let chartline2 = echarts.init(line2);
      // let chartline2 = echarts.init(this.$refs.line2);
      //绘制图表
      this.$nextTick(() => {
        chartline2.setOption(this.optionline);
      });
      // chartline2.resize();
    },
    drawLine3() {
      let line3 = document.getElementById("chartline3");
      let chartline3 = echarts.init(line3);
      //绘制图表
      chartline3.setOption(this.optionline);
    },

    //创造热力图
    async creatDailyChart() {
      const ret = await axios.get("china.json");
      echarts.registerMap("china", ret.data);
      let dataMap = [
        //热力图的数据
        { name: "北京", value: 500 },
        { name: "天津", value: 400 },
        { name: "上海", value: 500 },
        { name: "重庆", value: 350 },
        { name: "河北", value: 100 },
        { name: "河南", value: 200 },
        { name: "云南", value: 180 },
        { name: "辽宁", value: 100 },
        { name: "黑龙江", value: 100 },
        { name: "湖南", value: 300 },
        { name: "安徽", value: 330 },
        { name: "山东", value: 200 },
        { name: "新疆", value: 10 },
        { name: "江苏", value: 340 },
        { name: "浙江", value: 400 },
        { name: "江西", value: 360 },
        { name: "湖北", value: 300 },
        { name: "广西", value: 400 },
        { name: "甘肃", value: 100 },
        { name: "山西", value: 100 },
        { name: "内蒙古", value: 100 },
        { name: "陕西", value: 100 },
        { name: "吉林", value: 100 },
        { name: "福建", value: 350 },
        { name: "贵州", value: 100 },
        { name: "广东", value: 500 },
        { name: "青海", value: 100 },
        { name: "西藏", value: 100 },
        { name: "四川", value: 300 },
        { name: "宁夏", value: 100 },
        { name: "海南", value: 100 },
        { name: "台湾", value: 100 },
        { name: "香港", value: 300 },
        { name: "澳门", value: 200 },
        { name: "南海诸岛", value: 100 },
      ];
      // 需要在页面上直接标记出来的城市
      let specialMap = [];
      // 对dataMap进行处理，使其可以直接在页面上展示
      for (let i = 0; i < specialMap.length; i++) {
        for (let j = 0; j < dataMap.length; j++) {
          if (specialMap[i] == dataMap[j].name) {
            dataMap[j].selected = true;
            break;
          }
        }
      }
      //Echart的配置选项
      let option = {
        tooltip: {
          //悬浮时显示
          formatter: function(params) {
            var info = '<p style="font-size:18px">' + params.name + "</p>";
            // var info = '<p style="font-size:18px">' + params.name + '</p><p style="font-size:14px">这里可以写一些，想展示在页面上的别的信息</p>'
            return info;
          },
          backgroundColor: "#ff7f50", //提示标签背景颜色
          textStyle: { color: "#fff" }, //提示标签字体颜色
        },
        //左侧小导航图标
        visualMap: {
          show: true,
          x: "left",
          // y: 'center',
          bottom: "0%", //组件离容器下侧的距离,'20%'
          itemWidth: 5, //图形的宽度，即长条的宽度。
          itemHeight: 5, //图形的高度，即长条的高度。
          textGap: 5, //两端文字主体之间的距离，单位为px
          textStyle: {
            //文本样式
            fontSize: 10,
          },
          itemGap: 4, //每两个图元之间的间隔距离，单位为px
          splitList: [
            { start: 500, end: 600 },
            { start: 400, end: 500 },
            { start: 300, end: 400 },
            { start: 200, end: 300 },
            { start: 100, end: 200 },
            { start: 0, end: 100 },
          ],
          color: [
            "#663366",
            "#990033",
            "#ff0033",
            "#99cccc",
            "#cccc00",
            "#ffcc99",
          ],
        },
        series: [
          {
            name: "中国",
            type: "map",
            zoom: 1.2, //这里是关键，一定要放在 series中，地图缩放比例的配置
            mapType: "china",
            label: {
              //地图中的文字
              normal: {
                //正常显示
                show: false, //显示省份标签
                textStyle: {
                  fontSize: 10,
                  color: "#6c6a6a",
                },
              },
              // emphasis: {//悬浮时显示
              //     show: true,//对应的鼠标悬浮效果
              // }
            },

            data: dataMap,
          },
        ],
      };
      //初始化echarts实例
      let myChart = echarts.init(document.getElementById("container_daily"));
      //使用制定的配置项和数据显示图表
      myChart.setOption(option);
    },

    // charts() {
    //   let chart = this.echarts.init(document.getElementById("main"));
    //   //ajax请求接口获取数据
    //   this.Axios({
    //     url: "你自己的后台接口地址",
    //     params: _params,
    //   }).then(
    //     (response) => {
    //       var res = response.data;
    //       if (res && res.code === "0") {
    //         chart.setOption(res);
    //       } else {
    //         this.$Message.error(res.msg);
    //       }
    //     },
    //     (error) => {
    //       if (error.response) {
    //         const _result = error.response.data;
    //         this.$Message.error(_result.msg);
    //       } else {
    //         this.$Message.error("操作异常，请检查网络！");
    //       }
    //     }
    //   );
    // },
  },
  props: {},
  mounted() {
    this.$nextTick(() => {
      this.onClick();
    });
  },
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
}
</style>
