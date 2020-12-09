<template>
  <div class="china_table">
    <table class="table table-hover" cellspacing="10">
      <thead class="thead-dark">
        <tr>
          <th scope="col">地区</th>
          <th scope="col">现有确诊</th>
          <th scope="col">累计确诊</th>
          <th scope="col">治愈</th>
          <th scope="col">死亡</th>
          <th scope="col">疫情</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>香港</td>
          <td>1234</td>
          <td>8888</td>
          <td>5555</td>
          <td>113</td>
          <td>详情</td>
        </tr>
        <tr>
          <td>香港</td>
          <td>1234</td>
          <td>8888</td>
          <td>5555</td>
          <td>113</td>
          <td>详情</td>
        </tr>
        <tr>
          <td>香港</td>
          <td>1234</td>
          <td>8888</td>
          <td>5555</td>
          <td>113</td>
          <td>详情</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {},
  created() {},
  mounted() {},
  props: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.china_table {
  padding: 3px;
  table {
    thead {
      height: 26px;
      tr {
        th {
          border: 0;
          font-size: 16px;
          padding: 15px 5px;
          text-align: center;
        }
        th:nth-child(1) {
          background-color: rgb(245, 245, 245);
          color: rgb(34, 34, 34);
        }
        th:nth-child(2) {
          background-color: rgb(252, 242, 232);
          color: rgb(255, 114, 60);
        }
        th:nth-child(3) {
          background-color: rgb(253, 238, 238);
          color: rgb(246, 104, 133);
        }
        th:nth-child(4) {
          background-color: rgb(233, 247, 236);
          color: rgb(132, 139, 80);
        }
        th:nth-child(5) {
          background-color: rgb(243, 246, 248);
          color: rgb(78, 90, 101);
        }
        th:nth-child(6) {
          background-color: rgb(245, 245, 245);
          color: rgb(68, 34, 75);
        }
      }
    }
    tbody {
      tr {
        font-size: 18px;
        text-align: center;
        td {
          border: 0;
          border-bottom: 1px solid #dee2e6;
        }
      }
    }
  }
}
</style>
