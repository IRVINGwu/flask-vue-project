import Vue from "vue";
import moment from "moment";

Vue.filter("formatDate", function(data) {
  return moment(data).format("YYYY-MM-DD");
});

Vue.filter("formatNumber", function(data) {
  if (data < 0) {
    return data;
  } else if (data > 0) {
    return "+" + data;
  } else {
    return "+0";
  }
});

Vue.filter("formatContent", function(data) {
  if (data === null) {
    return "暂时未找到新闻内容";
  } else if (data.includes("p")) {
    return data
      .replaceAll("<p>", "")
      .replaceAll("</p>", "")
      .slice(0, 20);
  } else {
    return data.slice(3, 20);
  }
});
