<template>
  <div class="china_table">
    <table class="table table-hover">
      <thead class="thead-dark">
      <tr>
        <th scope="col">国家</th>
        <th scope="col">现有确诊</th>
<!--        <th scope="col">累计确诊</th>-->
        <th scope="col">现有治愈</th>
        <th scope="col">现有死亡</th>
        <th scope="col">疫情</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(item,index) in tablelist" :key="item.id">
        <td>{{ item.name }}</td>
        <td>{{ item.todayConfirm }}</td>
<!--        <td>{{item.total.confirm }}</td>-->
        <td>{{item.todayHeal}}</td>
        <td>{{item.todayDead}}</td>
        <router-link :to="'/world/' + item.name" tag="td">more</router-link>
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
      if(body.status === 200){
        let table = body.data
        // console.log(table)
        for (let key in table) {
          const obj = {
            name: table[key].name,
            todayConfirm: table[key].today.confirm === null ? 0 : +table[key].today.confirm,
            todayHeal: table[key].today.heal === null ? 0 : +table[key].today.heal,
            todayDead: table[key].today.dead === null ? 0 : +table[key].today.dead,
          }
          this.tablelist.push(obj)
        }
        // console.log(body.data)
      }
      // 数组排序后输出
      // for (let i = 0; i < this.tablelist.length; i++) {
      //   for (let j = i; j < this.tablelist.length; j++) {
      //     // if(this.tablelist[i].todayConfirm == this.tablelist[j].todayConfirm){
      //     //   console.log(this.tablelist[i])
      //     // }
      //     try{
      //       if(this.tablelist[i].todayConfirm < this.tablelist[j+1].todayConfirm){
      //         let temp = this.tablelist[i]
      //         this.tablelist[i] = this.tablelist[j+1]
      //         this.tablelist[j+1] = temp
      //
      //       }
      //     }catch (err){
      //       // console.log(err)
      //     }
      //   }
      // }


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
          font-size: 0.4rem;
          padding: 15px 0;
          text-align: center;
        }
        th:nth-child(1) {
          background-color: rgb(245, 245, 245);
          color: rgb(34, 34, 34);
          text-align: left;
          padding-left: 0.8rem;
        }
        th:nth-child(2) {
          background-color: rgb(252, 242, 232);
          color: rgb(255, 114, 60);
        }
        //th:nth-child(3) {
        //  background-color: rgb(253, 238, 238);
        //  color: rgb(246, 104, 133);
        //}
        th:nth-child(3) {
          background-color: rgb(233, 247, 236);
          color: rgb(132, 139, 80);
        }
        th:nth-child(4) {
          background-color: rgb(243, 246, 248);
          color: rgb(78, 90, 101);
        }
        th:nth-child(5) {
          background-color: rgb(245, 245, 245);
          color: rgb(68, 34, 75);
        }
      }
    }
    tbody {
      tr {
        font-size: 0.5rem;
        text-align: center;
        td {
          border: 0;
          border-bottom: 1px solid #dee2e6;
        }
        td:nth-child(1){
          font-size: 0.5rem;
          text-align: left;
        }
        td:nth-child(5){
          font-size: 0.3rem;
          color: red;
          text-align: left;
        }
      }
    }
  }
}
</style>

