<template>
  <div class="china_table">
    <table class="table table-hover">
      <thead class="thead-dark">
      <tr>
        <th scope="col">国家</th>
        <th scope="col">现有确诊</th>
        <th scope="col">累计确诊</th>
        <th scope="col">治愈</th>
        <th scope="col">死亡</th>
        <th scope="col">疫情</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(item,index) in tablelist" :key="item.id">
        <td>{{ item.name }}</td>
        <td>{{ item.today.confirm }}</td>
        <td>{{item.total.confirm }}</td>
        <td>{{item.total.heal}}</td>
        <td>{{item.total.dead}}</td>
        <router-link :to="'/world/' + item.name" tag="td">详情&gt;</router-link>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tablelist:[]
    };
  },
  methods: {
    async get_worldTable(){
      const body = await this.$http.get("/worldDaily")
      if(body.status == 200){
        this.tablelist = body.data
        // console.log(body.data)
      }
    }
  },
  created() {},
  mounted() {
    this.get_worldTable()
  },
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
          font-size: 15px;
          padding: 15px 5px;
          text-align: center;
        }
        th:nth-child(1) {
          background-color: rgb(245, 245, 245);
          color: rgb(34, 34, 34);
          font-size: 14px;
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
        font-size: 16px;
        text-align: center;
        td {
          border: 0;
          border-bottom: 1px solid #dee2e6;
        }
        td:nth-child(1){
          font-size: 14px;
        }
        td:nth-child(6){
          font-size: 14px;
          color: red;
        }
      }
    }
  }
}
</style>

