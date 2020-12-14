<template>
  <div class="china_table">
    <table class="table table-hover" id="table">
      <thead class="thead-dark" id="thead">
      <tr id="tr">
        <th scope="col">地区</th>
        <th scope="col">现有确诊</th>
        <th scope="col">累计确诊</th>
        <th scope="col">治愈</th>
        <th scope="col">死亡</th>
        <th scope="col">疫情</th>
      </tr>
      </thead>
      <tbody id="tbody">
      <tr v-for="(item,index) in tablelist" :key="item.id">
        <td>{{ item.省份名 }}</td>
        <td>{{ item.今日确诊 }}</td>
        <td>{{ item.总确诊数 }}</td>
        <td>{{ item.总治愈数 }}</td>
        <td>{{ item.总死亡数 }}</td>
        <router-link :to="'/' + item.省份名" tag="td">详情</router-link>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// import $ from 'jquery'

export default {
  data () {
    return {
      tablelist: []
    }
  },
  methods: {
    async get_chinaTable () {
      const body = await this.$http.get('/chinaProvinceDaily')
      if (body.status == 200) {
        this.tablelist = body.data
        // console.log(body.data)
      }
    },
    // fix_thead () {
    //   window.onscroll = function () {
    //     let toTop = document.querySelector('#thead')
    //     let tr = document.querySelector("#tr")
    //
    //     let clonedNode = tr.cloneNode(true); // 克隆节点
    //     clonedNode.setAttribute("id", "tr1"); // 修改一下id 值，避免id 重复
    //
    //     if (document.documentElement.scrollTop >= 1339) {
    //       toTop.appendChild(clonedNode)
    //       clonedNode.style.position = 'fixed'
    //       clonedNode.style.top = '0'
    //       clonedNode.style.zIndex = '999'
    //       // clonedNode.style.width = '100%'
    //     } else if(document.documentElement.scrollTop < 1339){
    //       clonedNode.style.display = 'none'
    //     }
    //   }
    // }
  },
  created () {
  },
  mounted () {
    this.get_chinaTable()
  },
  props: {},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.china_table {
  padding: 3px;

  table {
    table-layout: fixed;

    thead {
      height: 26px;

      tr {
        th {
          border: 0;
          font-size: 0.625rem;
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
        font-size: 0.6rem;
        text-align: center;

        td {
          border: 0;
          border-bottom: 1px solid #dee2e6;
        }

        td:nth-child(1) {
          text-align: left;
        }

        td:nth-child(6) {
          color: red;
          font-size: 0.5rem;
        }
      }
    }
  }
}
</style>
