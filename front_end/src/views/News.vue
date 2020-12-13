<template>
  <div class="news_container">
    <div class="news_header">
      <img src="../assets/images/news_banner.png" alt="" />
      <div class="header_content">
        <span>同心合力 抗击疫情</span>
        <span>covid-19疫情最新进展</span>
      </div>
    </div>

<!--    疫情新闻内容-->
    <div class="news_content">
      <h3>疫情追踪<span></span></h3>
<!--      疫情列表-->
      <ul class="newslist">
        <li v-for="(item,index) in news" :key="item.id">
          <div class="news_item">
            <span>{{ item.date }}</span>
            <div class="item_content">
              <h4 class="title">{{ item.title }}</h4>
              <div class="content">{{ item.content.slice(3,29) }}...
              </div>
<!--              <span @click="getNewsItem(item.id)"></span>-->
              <router-link :to="'/news/' + item.id" tag="span">查看详情&gt;&gt;&gt;</router-link>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      news:''
    }
  },
  methods:{
    async getNews(){
      const body = await this.$http.get("/news")
      if(body.status == 200){
        this.news = body.data
      }
      // console.log(this.news)
    },
    // async getNewsItem(id){
    //   // 父组件向子组件传递参数
    //   return
    // }
  },
  mounted () {
    this.getNews()
  },
  components:{
  }
};
</script>

<style lang="scss">
.news_container {
  margin-top: 46px;
  margin-bottom: 35px;
  .news_header {
    position: relative;
    background-color: rgb(0, 86, 238);
    img {
      width: 100%;
      height: 150px;
    }
    .header_content {
      position: absolute;
      width: 100%;
      // background-color: pink;
      left: 0;
      top: 40px;
      display: flex;
      flex-direction: column;
      font-size: 24px;
      color: white;
      text-align: center;
      span:nth-child(2){
        font-size: 28px;
        font-style: italic;
      }
    }
  }

  .news_content{
    padding: 15px;
    h3{
      position: relative;
      font-size: 20px;
      font-weight: bold;
      margin: 10px 0 ;
      border-left: 5px solid red;
      padding-left: 5px;
      height: 30px;
      line-height: 30px;
      span{
        position: absolute;
        display: inline-block;
        width: 106px;
        height: 30px;
        background: url("../assets/images/zhuizong.png") no-repeat;
        background-size: 100% 100%;
        right: 10px;
        top: 0;
      }
    }
    ul{
      list-style: none;
      //padding-left: 10px;
      li{
        position: relative;
        border-left:1px solid #ddd;
        width: 100%;
        height: 188px;
        padding-left: 15px;
        .news_item{
          display: flex;
          flex-direction: column;
          justify-content: space-around;

          span{
            font-size: 16px;
            color: rgb(115, 115, 160);
            margin-top: -7px;
          }
          .item_content{
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 5px;
            background-color: rgb(248, 248, 248);
            margin-top: 15px;
            h4{
              font-size: 16px;
            }
            .content{
              margin: 0 0 5px 0;
              font-size: 15px;
              color: rgb(123, 117, 120);
            }
            span{
              font-size: 15px;
              color: rgb(123, 117, 120);
            }
          }
        }
      }
      li::before{
        content: ".";
        font-size: 0;
        line-height: 0;
        position: absolute;
        width: 3.3px;
        height: 3.3px;
        border: 5.6px solid #005dff;
        border-radius: 50%;
        left: -5.7px;
        top: 0;
        background-color: #fff;
      }
    }
  }
}
</style>
