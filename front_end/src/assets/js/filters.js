import Vue from 'vue'
import moment from 'moment'

Vue.filter('formatDate',function(data){
  return moment(data).format('YYYY-MM-DD')
})

Vue.filter('formatNumber',function(data){
  if(data < 0 ){
    return data
  }else{
    return '+' + data
  }
})