<template>
  <div class="rumor_container">
    <div class="rumor_header">
      <img src="../assets/images/rumor_banner.png" alt="" class="img1" />
      <img src="../assets/images/rumor_title.png" alt="" class="img2" />
      <div class="header_content">
        <span>covid-19疫情实时辟谣</span>
        <span>信息来源：中国医师协会健康传播工作委员会</span>
      </div>
    </div>
    <!-- TODO:谣言就用bootstrap的卡片来做，直接展示出来，不需要点击然后跳转 -->
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  mounted() {},
  methods: {},
  props: {},
};
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
}
</style>
