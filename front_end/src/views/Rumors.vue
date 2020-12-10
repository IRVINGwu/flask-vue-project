<template>
  <div class="rumor_container">
    <div class="rumor_header">
      <img src="../assets/images/rumor_banner.png" alt="" class="img1"/>
      <img src="../assets/images/rumor_title.png" alt="" class="img2"/>
      <div class="header_content">
        <span>covid-19疫情实时辟谣</span>
        <span>信息来源：中国医师协会健康传播工作委员会</span>
      </div>
    </div>

    <!--    谣言部分-->
    <div class="rumor_content">

      <!--      内容介绍-->
      <div class="rumor_introduction">
        <p>这次新型肺炎牵动了无数人的心，伴随着疫情的发展，各种谣言也在网上流传。
          这些谣言对防治新型冠状病毒并没有起到正面作用，反而会引起不必要的抢购潮，甚至引发恐慌。
          <br>
          这里整理了10条在网上广为流传的谣言，希望大家在谣言面前擦亮眼睛，科学预防新型冠状病毒。
        </p>
      </div>

      <!--      谣言版块-->
      <!--      TODO:准备好疫情新闻和谣言的json文件，然后使用v-for来渲染，这样才能充分发挥vue的威力-->
      <div class="card bg-light mb-3">
        <div class="card-header">年轻人和儿童感染几率非常小<span class="icon1">谣言</span></div>
        <div class="card-body">
          <h5 class="title">
            鉴定：<span class="icon2">假</span><span class="icon3">谣言</span>
          </h5>
          <h5 class="title">真相：<span class="icon4">没有感染的人都可能会感染</span></h5>
          <h5 class="title">查据要点：</h5>
          <p>
            有专家提到，年轻人和儿童不易感染新型冠状病毒，但不易感染≠不会感染。<br>
            就目前的流行病学而言，儿童、年轻人对病毒不易感，但这并不意味着大家可以掉以轻心。<br>
            新型冠状病毒已经确定可以人传人，它的传播途径以呼吸道传播为主，像咳嗽、打喷嚏等均会传播病毒，在人流聚集的地方，一旦预防不到位，没有感染的人都可能会感染。
            国家卫健委高级别专家组成员李兰娟也指出：“没有感染过这个疾病的人，都是易感的。”<br>
            无论男女老少，都要重视预防，尤其是老年人、孕妇、婴幼儿等免疫功能较差的群体，一旦感染，病情发展往往更快，更要注意保护自己。<br>
          </p>
          <h5 class="title">查证来源：<span class="icon4">央视新闻</span></h5>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {}
  },
  mounted () {
  },
  methods: {},
  props: {},
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.rumor_container {
  margin-top: 46px;
  margin-bottom: 35px;

  .rumor_header {
    position: relative;

    .img1 {
      width: 100%;
      height: 150px;
    }

    .img2 {
      position: absolute;
      width: 15%;
      height: 60%;
      left: 10px;
      top: 10px;
    }

    .header_content {
      position: absolute;
      width: 100%;
      // background-color: pink;
      left: 0;
      top: 40px;
      display: flex;
      flex-direction: column;
      color: white;
      text-align: center;

      span:nth-child(1) {
        font-size: 26px;
      }

      span:nth-child(2) {
        font-size: 16px;
      }
    }
  }

  .rumor_content {
    padding: 5px;

    .rumor_introduction {
      font-size: 16px;
      color: rgb(0, 0, 0);
    }

    .card {
      width: 100%;
    }

    .card-header {
      text-align: center;
      padding: 5px 0;
      color: #020202;
      font-size: 18px;

      .icon1 {
        display: float;
        margin-left: 3px;
        border: 1px solid red;
        color: white;
        background-color: red;
        border-radius: 5px;
        padding: 0 3px 2px;
        height: 22px;
        line-height: 22px;
        font-size: 16px;
      }
    }

    .card-body {
      color: rgb(75, 78, 75);
      padding: 15px 2px 0px 15px;
      background-color: rgb(248, 248, 248);

      h5 {
        font-size: 18px;
        color: rgb(10, 10, 10);

        span {
          display: float;
        }

        .icon2 {
          border: 1px solid red;
          color: white;
          background-color: red;
          border-radius: 5px 0 0 5px;
          padding: 0 3px 2px;
          height: 22px;
          line-height: 22px;
          font-size: 16px;
        }

        .icon3 {
          border: 1px solid red;
          color: red;
          font-weight: bold;
          background-color: #fff;
          border-radius: 0 5px 5px 0;
          padding: 0 3px 2px;
          height: 22px;
          line-height: 22px;
          font-size: 16px;
        }

        .icon4 {
          color: #000;
          font-size: 20px;
        }

      }

      p {
        font-size: 16px;
        color: #646566;
      }
    }
  }
}
</style>
