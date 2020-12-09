<template>
  <div class="news_container">
    <div class="news_header">
      <img src="../assets/images/news_banner.png" alt="" />
      <div class="header_content">
        <span>同心合力 抗击疫情</span>
        <span>covid-19疫情最新进展</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
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
    }
  }
}
</style>
