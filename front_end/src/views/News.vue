<template>
  <div class="news_container">
    <div class="news_header">
      <img src="../assets/images/news_banner.png" alt=""/>
      <div class="header_content">
        <span>同心合力 抗击疫情</span>
        <span>covid-19疫情最新进展</span>
      </div>
    </div>

    <!--    疫情新闻内容-->
    <!--    <div class="news_content">-->
    <!--      <h3>疫情追踪<span></span></h3>-->
    <!--      &lt;!&ndash;      疫情列表&ndash;&gt;-->
    <!--      <ul class="newslist">-->
    <!--        <li v-for="(item,index) in newsContent" :key="item.id">-->
    <!--          <div class="news_item">-->
    <!--            <span>{{ item.time }}</span>-->
    <!--            <div class="item_content">-->
    <!--              <h4 class="title">{{ item.title }}</h4>-->
    <!--              <div class="content">{{ item.content | formatContent }}...-->
    <!--              </div>-->
    <!--              &lt;!&ndash;              <span @click="getNewsItem(item.id)"></span>&ndash;&gt;-->
    <!--              <router-link :to="'/news/' + item.id" tag="span">查看详情&gt;&gt;&gt;</router-link>-->
    <!--            </div>-->
    <!--          </div>-->
    <!--        </li>-->
    <!--      </ul>-->
    <!--&lt;!&ndash;      当新闻拉取完之后,提示没有更多内容了&ndash;&gt;-->
    <!--      <van-divider v-show="flag">上拉加载更多内容!</van-divider>-->
    <!--      <van-divider v-show="!flag">没有更多内容了!</van-divider>-->
    <!--    </div>-->

    <!--    vant上拉加载组件-->
    <div class="news_content">
      <h3>疫情追踪<span></span></h3>
      <!--      疫情列表-->
      <van-list tag="ul" class="newsul" v-model="loading" :finished="finished" finished-text="没有更多内容了！" @load="onload">
        <van-cell tag="li" class="newsli" v-for="(item,index) in newsContent" :key="index">
          <div class="news_item">
            <span>{{ item.time }}</span>
            <div class="item_content">
              <h4 class="title">{{ item.title }}</h4>
              <div class="content">{{ item.content | formatContent }}...
              </div>
              <router-link :to="'/news/' + item.id" tag="span">查看详情&gt;&gt;&gt;</router-link>
            </div>
          </div>
        </van-cell>
      </van-list>
      <!--      当新闻拉取完之后,提示没有更多内容了，此处是未使用vant的时候加的-->
      <!--      <van-divider v-show="flag">上拉加载更多内容!</van-divider>-->
      <!--      <van-divider v-show="!flag">没有更多内容了!</van-divider>-->
    </div>
  </div>
</template>

<script>
import {Divider, List, Cell} from 'vant'

export default {
  data () {
    return {
      news: [],
      newsContent: [],
      // newsLen: 10,
      newsLen: 0,
      flag: true,
      loading: false,
      finished: false,
      refreshing: false,
    }
  },
  methods: {
    async getNews () {
      const body = await this.$http.get('/api/news')
      if (body.status == 200) {
        // body.data传递过来的是伪数组,使用循环赋值的方法获取到真数组
        // this.news = body.data
        for (let key in body.data) {
          this.news.push(body.data[key])
        }
      }
      // console.log(typeof this.news) //object
      // 下拉加载可以这样做,指定一个news用来接收所有的数据,但是初始化的newsContent只截取前10个数据,
      // v-for循环的是newsContent,那么在我下拉的时候,每次加10条数据到newsContent里面,直到最后可能没有
      // 10条数据了,加个判断即可,加载完了就显示"已经到底了".
      // console.log(this.news)
      // if(this.news)
      // for (let i = 0; i < this.newsLen; i++) {
      //   this.newsContent.push(this.news[i])
      // }
      //this.newsContent = this.news.slice(0,this.newsLen)
    },
    //实现上拉加载
    // 获取滚动条当前的位置
    // getScrollTop () {
    //   let scrollTop = 0
    //   if (document.documentElement && document.documentElement.scrollTop) {
    //     scrollTop = document.documentElement.scrollTop
    //   } else if (document.body) {
    //     scrollTop = document.body.scrollTop
    //   }
    //   return scrollTop
    // },
    // // 获取当前可视范围的高度
    // getClientHeight () {
    //   let clientHeight = 0
    //   if (document.body.clientHeight && document.documentElement.clientHeight) {
    //     clientHeight = Math.min(document.body.clientHeight, document.documentElement.clientHeight)
    //   } else {
    //     clientHeight = Math.max(document.body.clientHeight, document.documentElement.clientHeight)
    //   }
    //   return clientHeight
    // },
    // // 获取文档完整的高度
    // getScrollHeight () {
    //   return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)
    // },
    // // 滚动事件触发下拉加载
    // onScroll () {
    //   if (this.getScrollHeight() - this.getClientHeight() - this.getScrollTop() <= 0) {
    //     //如果请求次数大于5次,就不再请求,而是输出"没有更多内容了."
    //     // console.log(this.news.length)
    //     if(this.newsContent.length < this.news.length){
    //       this.newsLen += 10
    //       this.newsContent = []
    //       for (let i = 0; i < this.newsLen; i++) {
    //         if(this.news[i] !== ''){
    //           this.newsContent.push(this.news[i])
    //         }
    //       }
    //     }else if(this.newsContent.length >= this.news.length){
    //       // console.log('没有更多内容了!!!')
    //       // this.$toast('没有更多内容了!!!')
    //       console.log(this.newsContent.length)
    //       console.log(this.news.length)
    //       this.flag = false
    //     }
    //   }
    // },
    onload () {
      setTimeout(() => {
        if (this.refreshing) {
          this.newsContent = []
          this.refreshing = false
        }
        this.newsLen += 10
        this.newsContent = []
        for (let i = 0; i < this.newsLen; i++) {
          if (this.news[i] !== '') {
            this.newsContent.push(this.news[i])
          }
        }
        this.loading = false
        if (this.newsContent.length >= this.news.length) {
          this.finished = true
        }
      }, 1000)
    },
    onRefresh () {
      // 清空列表数据
      this.finished = false
      // 重新加载数据
      // 将 loading 设置为 true，表示处于加载状态
      this.loading = true
      this.onLoad()
    },
  },
  mounted () {
    this.getNews()
    this.onload()
  },
  components: {
    [Divider.name]: Divider,
    [List.name]: List,
    [Cell.name]:Cell,
  }
}
</script>

<style lang="scss">
.news_container {
  //margin-top: 46px;
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

      span:nth-child(2) {
        font-size: 28px;
        font-style: italic;
      }
    }
  }

  .news_content {
    padding: 15px;

    h3 {
      position: relative;
      font-size: 20px;
      font-weight: bold;
      margin: 10px 0;
      border-left: 5px solid red;
      padding-left: 5px;
      height: 30px;
      line-height: 30px;

      span {
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

    .newsul {
      width: 100%;

      .newsli {
        padding: 0;

        .news_item {
          position: relative;
          display: flex;
          flex-direction: column;
          justify-content: space-around;
          padding: 15px 0 20px 0;
          border-bottom: 2px solid #f3f3f3;

          span {
            font-size: 16px;
            color: rgb(115, 115, 160);
            margin-top: -7px;
          }

          .item_content {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 5px;
            background-color: rgb(248, 248, 248);
            margin-top: 15px;

            h4 {
              font-size: 16px;
            }

            //h4::before {
            //  content: "";
            //  font-size: 0;
            //  line-height: 0;
            //  position: absolute;
            //  width: 3.3px;
            //  height: 3.3px;
            //  border: 5.6px solid #005dff;
            //  border-radius: 50%;
            //  left: -5px;
            //  top: 0;
            //  background-color: #fff;
            //}

            .content {
              margin: 0 0 5px 0;
              font-size: 15px;
              color: rgb(123, 117, 120);
            }

            span {
              font-size: 15px;
              color: rgb(123, 117, 120);
            }
          }
        }
      }


    }
  }
}
</style>
