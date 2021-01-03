## echarts中国地图是怎么解决的？

## echarts切换不显示是怎么解决的？

将id直接放在vant的元素上面，获取到图表。这就解决了获取不到元素的问题。

------

### span标签里面的文字垂直居中，我先将其调整为inline-block，然后设置height,line-height，怎么都不居中，结果调整成float，就居中了，不知道怎么回事。

------

![image-20201210210729583](https://i.loli.net/2020/12/11/J4XjDOETxra3soK.png)

这个图标我用的是伪元素，里面设置background，我使用了vertical-align:middle，怎么都不与后面的文字垂直居中。结果我只好设置background-position:10% 10%;（这里的数字是随便写的），这样微调才能和后面的文字保持一致，查一查这样的原因是什么？
我在后面又遇到了这种情况，也是文字与图标不能对齐，我看了一下腾讯的做法，他们用的是“子绝父相”这种方法。效果比较好。
------

bootstrap里面的样式修改很简单，我直接将复制过来的代码，里面的类名的样式编写一下，就可以进行更改，非常方便。

但是vant的代码里面，由于没有显示出类名出来，我必须在浏览器的调试窗口来复制类名，然后才能进行更改，有什么类名隐藏的比较深，找起来也有点麻烦，很多情况下一个地方改了，另外一个地方没有跟着变化，所以还是比较麻烦的。

------

新闻模块和谣言模块，难点很多，其中一个难点就是json文件的准备，我都没有准备过json文件，该怎么做呢？只要把这个文件做好了，接收数据都不是难事。

使用JS来编写json文件，那绝对是非常复杂的，我在想，能不能使用excel来编写文件，然后转换为json格式。先试一试。

------

因为我的后端路由是127.0.0.1:5000，而绘制地图时获取的china.json数据，在前端进行请求时也是127.0.0.1:5000，所以要将这个数据放到后端去。

![image-20201211192421831](https://i.loli.net/2020/12/11/hEmOAJdPBQ84V9W.png)

------

从后端引入的china.json文件为什么不行？

![image-20201212001010981](https://i.loli.net/2020/12/12/QfAxwBdV2Uqm57b.png)

上面是从后端引入的json文件，可以看到键值对是`键：{值}`这样的形式。值是对象。

而我直接使用`import ret from "../../public/china.json"`引入的文件，不是这样的：

![image-20201212001232708](https://i.loli.net/2020/12/12/CgqDzjPaisXUNyh.png)

也就是说传递过来的json文件格式一点都不能乱，必须保持原样。那应该怎么做呢？

读取json文件的时候，要把它当做`typ='series'`类型来读取，这样就不会改变格式了。这里是网址：https://www.cnblogs.com/happymeng/p/10481293.html

```python
def getMapJson(self, request_name, orient='index'):
    name = str(request_name)
    df = pd.read_csv('./static/data/province.csv')
    if name == 'china':
        path = './static/mapJson/' + name + '.json'
    else:
        eng_name = df.iloc[df['省份名'] == name, :]
        path = './static/mapJson/' + eng_name + '.json'

        # 这里的typ='series'，终于把json文件原封不动的传递过去了，没有问题了
        df_json = pd.read_json(path, orient='records', typ='series')
        df_jso = df_json.to_json(orient=orient, force_ascii=False)
        # 直接将json类型的数据发送到前端
        return df_jso
```

可以正常使用了。

------

父组件向子组件传递参数：

过程我总结了一下，就是创建全局路由→打开参数传递props→在父组件中使用v-bind绑定参数→在子组件中使用props接收参数。

创建全局路由，打开参数传递：

```js
{
    path: "/news/:id",      //注意这里要传递参数，就要使用:，id是参数名，对应的是父组件中v-bind绑定的id
    name: "NewsItem",
    component: () =>
      import(/* webpackChunkName: "about" */ "../components/NewsItem"),
    props:true              //打开参数传递
  },
```

在父组件中使用v-bind绑定参数：

```vue
<router-link :to="'/news/' + item.id" tag="span">查看详情&gt;&gt;&gt;</router-link>

<!--
注意：这里的:to就是要传递到哪一个组件中去，item.id对应的就是创建路由时的:id
这里没有在<script>里面写任何内容，这和私有组件不一样
-->
```

在子组件中使用props接收参数：

```js
<script>
export default {
  name: 'newsItem',
  data(){
    return{
      newsItem:''
    }
  },
  methods:{
    async getNewsItem(id){
      const body = await this.$http.get("/news/" + id)
      if(body.status == 200){
        this.newsItem = body.data.data[0]
      }
    }
  },
  mounted () {
    this.getNewsItem(this.id)//这里的this.id就是props里面的id 
  },
  props:['id']            //这里使用props来接收父组件传递过来的参数，那么在此vm实例中就可以用this.id来调用了
}
</script>
```

------

echarts图表明明在created()里面就获取了数据，为什么在mounted()里面还是没有能够获取到呢？

![image-20201212180851516](https://i.loli.net/2020/12/12/nezQ9WEIqDkUafp.png)

从下面的代码可以看到，我是先获取数据，再执行绘图任务的，但是绘图任务中没有拿到数据，这是为什么呢？这就不是echarts的问题了，而是vue的问题了。

```js
export default {
  data() {
    return {};
  },
  created() {
    this.get_chinaSum();//获取数据
  },
  methods: {
    onClick(name, title='新增趋势') {
      let line1 = document.getElementById("chartline1")
      let line2 = document.getElementById("chartline2")
      let line3 = document.getElementById("chartline3")
      line1.style.display = 'block'
      line2.style.display = 'block'
      line3.style.display = 'block'

      let chartline1 = echarts.init(line1);
      let chartline2 = echarts.init(line2);
      let chartline3 = echarts.init(line3);
      // chartline1.setOption(this.optionline1);
      if (title == "确诊趋势") {
        chartline2.setOption(this.optionline2);
      } else if (title == "治疗趋势") {
        chartline3.setOption(this.optionline3);
      } else if(title == "新增趋势"){
        console.log(this.optionline1)
        chartline1.setOption(this.optionline1);
        chartline1.resize()
      }
    },

    //获取制图所需要的数据
    async get_chinaSum(){
      const body = await this.$http.get('/chinaSum')
      }

  },
  mounted() {
    this.$nextTick(() => {
      this.onClick();//初始化表格
    });
  },

};
```

参考文档：https://blog.csdn.net/weixin_43481793/article/details/88533048?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control

文档中说需要使用`watch`来监控数据，但是我看了一下评论，居然在里面找到了答案，那就是先获取数据，把作图的函数放到获取函数中，放到获取数据之后来执行，这样就行了，没有问题。

```js
export default {
  data() {
    return {};
  },
  created() {
    this.get_chinaSum();//直接初始化这个方法即可
  },
  methods: {
    onClick(name, title='新增趋势') {},
    //获取制图所需要的数据
    async get_chinaSum(){
      const body = await this.$http.get('/chinaSum')
      // 这句非常重要，我在查了很多资料之后才知道的，原来onClick()里面在初始化的时候没有获取到
      // 数据，结果就没有办法渲染出图表，这里的意思是，先获取数据，然后作图
      this.onClick()
      }

  },
  mounted() {},
};
```

echarts图表确实很麻烦，我的调试方法是：每一步都`console.log()`一下，看是哪里的问题，再百度找方法。

------

### 底部tab栏的选中高亮状态

查看的文档：https://blog.csdn.net/weixin_43817709/article/details/104023966?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.control

我使用了vant的tabbar模块，它有一个用于显示高亮的方法：

```vue
<van-tabbar v-model="active">
  <van-tabbar-item icon="home-o">标签</van-tabbar-item>
  <van-tabbar-item icon="search">标签</van-tabbar-item>
  <van-tabbar-item icon="friends-o">标签</van-tabbar-item>
  <van-tabbar-item icon="setting-o">标签</van-tabbar-item>
</van-tabbar>

<script>
export default {
  data() {
    return {
      active: 0,     //通过绑定active的值，来实现在切换tab时，同时切换高亮的状态。
    };
  },
};
</script>	
```

但是我按返回键之后，返回了原来的界面，高亮状态并没有跟着改变，为什么呢？因为在按返回键的时候，active的值并没有发生改变，是不是，想清楚没有？那么如何才能监听到active值的变化呢？或者更进一步的，让active的值跟着返回键所在的界面，返回相应的值？

直接监听返回键是很难的，但是可以监听App.vue这个vue实例的router对象，这个对象会返回很多值，这个对象很重要，返回键也是使用这个对象的go方法来返回的（`this.$router.go(-1)`）。通过上述文档，我发现可以利用`this.$router.name`来返回相应的值，然后为`active`这个函数返回一个值，就会显示相应的tabbar。

以下是代码：

```js
computed: {
    active () {//匹配路由的名字，给active赋值
      if(this.$route.name == 'Home'){
        return 0
      }else if(this.$route.name == 'World'){
        return 1
      }else if(this.$route.name == 'News'){
        return 2
      }else{
        return 3
      }
    }
  }
```

注意，这时候`<van-tabbar v-model="active">`里面的这个active就是这个active函数，只要这个函数返回的是一个值即可。

这里还用到了`computed:{}`属性，这个属性就会监听url地址的变化。但是这里需要设置两个方法，vue规定的，get()和set()方法，但这里太复杂，所以我将`v-model`换为了`:value`，这就没有问题了。

这是computed{}方法报错的解决办法：https://blog.csdn.net/weixin_38779534/article/details/105989139?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromBaidu-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromBaidu-1.control



## 使用VUE3.0+TYPESCRIPT来重写前端代码

网易的API接口，直接在前端进行使用，使用axios来获取数据，axios(url:'',headers={}).then(res=>{})，上次不成功，是因为我已经定义了axios.baseURL="127.0.0.1"，所以在后面请求网易数据时，网址错了。都试过了，还是不能行，说是headers错误，也不知道是什么错误、怎么改，还是直接在后端运行吧。