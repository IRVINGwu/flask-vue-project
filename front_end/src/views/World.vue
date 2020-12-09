<template>
  <div class="world_container">
    <div class="world_header">
      <img src="../assets/images/world_banner.png" alt="" />
      <div class="header_content">
        <span>山川异域 日月同天</span>
        <span>covid-19世界疫情实时播报</span>
        <span>数据来源：WHO及权威媒体报道</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss">
.world_container {
  margin-top: 46px;
  margin-bottom: 35px;
  .world_header {
    position: relative;
    img {
      width: 100%;
      height: 150px;
    }
    .header_content {
      position: absolute;
      width: 100%;
      // background-color: pink;
      left: 0;
      top: 30px;
      display: flex;
      flex-direction: column;
      font-size: 22px;
      color: white;
      text-align: center;
      :nth-child(3) {
        font-size: 16px;
      }
    }
  }
}
</style>
