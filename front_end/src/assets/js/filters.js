import Vue from 'vue'
import moment from 'moment'

Vue.filter('formatDate',function(data){
  return moment(data).format('YYYY-MM-DD')
})

Vue.filter('formatNumber',function(data){
  if(data < 0 ){
    return data
  }else if(data > 0){
    return '+' + data
  }else{
    return ''
  }
})

Vue.filter('formatContent',function(data){
  if(data === null ){
    return '暂时未找到新闻内容'
  }else{
    return data.slice(3,20)
  }
})