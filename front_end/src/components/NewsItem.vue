<template>
  <div class="newsItem">
    <h3>{{ newsItem.title }}</h3>
    <span>{{ newsItem.source }}</span><br>
    <span>{{ newsItem.time }}</span>
    <div class="content" v-html="newsItem.content">
    </div>
  </div>
</template>

<script>
export default {
  name: 'newsItem',
  data(){
    return{
      newsItem:''
    }
  },
  methods:{
    async getNewsItem(id){
      // console.log(id)
      const body = await this.$http.get("/news/" + id)
      if(body.status == 200){
        this.newsItem = body.data.data[0]
        // console.log(body.data.data[0])
      }
    }
  },
  mounted () {
    this.getNewsItem(this.id)
  },
  props:['id']
}
</script>

<style scoped lang="scss">
.newsItem{
  //margin-top: 46px;
  margin-bottom: 50px;
  padding: 10px;
  h3{
    text-align: center;
    font-size: 20px;
    color: #020202;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(0,0,0,0.5);
  }
  span{
    font-size: 16px;
    color: rgba(146, 131, 112,0.9);
    padding-left: 5px;
  }
  .content{
    font-size: 16px;
    color: #020202;
    padding: 5px;
  }
}
</style>