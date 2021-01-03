### 1.图片问题

原来我想将图片先转为base64格式的，传递给前端，由前端JS来解析，但是我突然想到，既然是前端发送请求给后端，那为什么不直接请求后端的一个地址呢？请求图片所在的地址，直接发送到前端不就可以显示图片了吗？反正后端服务器是开着的，这样应该可行。

我在网上搜索，查看别人是怎样将图片存到数据库中，结果和我想的方法一样：

![image-20201210225332008](https://i.loli.net/2020/12/11/jlfthU9bIPOzALF.png)

我就把图片路径存到json文件中即可，反正这个app也没有交互的功能，简单点，先做出来。

我打开别人的数据，发现别人的数据里面，img是保存为地址的，那么我需要的就是保存图片的规则要制定出来，如何与具体的对象结合起来。

![image-20201228153530208](https://img-typora-irving.oss-cn-shanghai.aliyuncs.com/img/image-20201228153530208.png)

### 2.数据来源

在我的码云里面，一个叫“covid-19-data”的项目，里面存放着数据，每天从GitHub拉取更新即可得到最新的数据，但是这数据有点不一样，里面有更具体的国家、省份，还有感染数、康复数，等等。我主要看三个文件：

![image-20201201135433455](https://i.loli.net/2020/12/11/m7xsqYwfnuC6bXz.png)

这三份文件做出世界的感染数、死亡数、康复数即可，还是分为三张表放着。

中国的数据使用这个API接口https://c.m.163.com/ug/api/wuhan/app/data/list-total，里面有很丰富的信息，就看怎么解析了。

### 3.数据分类

![image-20201203150056949](https://i.loli.net/2020/12/11/K4oQgt1un9fXMFq.png)

### 4.路由问题

flask中定义的每一个路由，对应的就是前端的一个组件，而这个组件是全局组件还是私有组件，就看你怎么组装了。

```python
from flask import Flask
from flask_cors import CORS
from toolspkg.response import Response

app = Flask(__name__)
app.config.from_object(__name__)

# 可以热更新
DEBUG = True

# 开通 CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello World!'

# 传送谣言数据到前端


@app.route('/rumors', methods=['GET'])
def get_rumors():
    response = Response().getRumors()
    return response

# 传送新闻数据到前端


@app.route('/news', methods=['GET'])
def get_news():
    response = Response().getNews()
    return response


# 因为有一些文件是数据处理的文件，需要在后端服务器已启动就执行，所以需要在此文件中引入，然后放到这里执行。
if __name__ == '__main__':
    app.run()
```

因为我启用了`flask_cors`，这样我就可以以`http://127.0.0.1:5000/rumors`这种方式向前端发送数据，前端的axios只需要访问这个地址即可获取数据。下面是用postman模拟获取数据的情况：

![image-20201211190854185](https://i.loli.net/2020/12/11/mH74jvJTR8N1FD2.png)

达到了我想要的效果。

flask中的各个路由，就想前端传递不同的数据。需要几个数据接口就写几个数据接口，在细分的item路由上，可以传递参数。

```python
@app.route('/news/<numbers>', methods=['GET'])#numbers就是前端传递过来的参数，这个参数就是路由上的参数
def get_news():
    number = int(numbers)#这里是假设numbers只有一个数据
    ...
    调用后端的函数方法来对这个参数进行处理，得到我想要的数据
    ...
    return response
```



### 5.json数据问题

使用`df.to_json`时，有三种参数，`split/records/table/index`，现在看起来只有`index`做的比较好（当然具体情况具体分析，主要看源数据的格式），因为列标和内容都是以键值对的形式来传送的。

![image-20201211185519866](https://i.loli.net/2020/12/11/datNnIcQ8FisH4Y.png)

全部改为`index`即可。

**为什么不把源文件就改为json格式呢？**

如果改成json格式的话，确实比较好传送数据，但是在后端不好处理数据，我要先读取json文件，然后转换为dataframe类型，才能很好的处理数据。

### 6.后端数据只能在电脑上访问，在手机上调试不行

这是解决方法：https://blog.csdn.net/y_k_y/article/details/83043543?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control

原因在于pycharm里面的设置：

![image-20201213205511391](https://i.loli.net/2020/12/13/UoaZlOK4rAbwi16.png)

![image-20201213210955644](https://img-typora-irving.oss-cn-shanghai.aliyuncs.com/img/image-20201213210955644.png)

当然，为了保险起见，还需要在`app.py`里面将地址改掉：

```python
if __name__ == '__main__':
    app.run(
        host='192.168.0.106',#这是在cmd中使用ipconfig得到的ipv4的路由地址，可以在同一个网中访问
        port=80,
        debug=True
    )
```

还要将前端里面`axios.baseURL`由`127.0.0.1:5000`改为这个地址`192.168.0.106:5000`，这样项目就可以在手机上进行调试了。

```js
axios.defaults.baseURL = "http://192.168.0.107:8080";
```

**当然，上线之后要改掉，就改成127.0.0.1，要让别人自己的ipv4来用，免得暴露自己的地址。**

<hr>
**问题：**

![image-20201222142311668](https://img-typora-irving.oss-cn-shanghai.aliyuncs.com/img/image-20201222142311668.png)

改了之后运行的好好的，结果第二天就不行了，我还以为是pycharm的问题，结果使用VSCODE还是不行，接着几天都是这样，后来我查看CMD里面的`ipconfig`，发现ipv4的地址改变了，这是为什么呢？还不知道，以后有问题先找这里就行了。

![image-20201222142636058](https://img-typora-irving.oss-cn-shanghai.aliyuncs.com/img/image-20201222142636058.png)

网上查了一下，果然会变化：

![image-20201222143942956](https://img-typora-irving.oss-cn-shanghai.aliyuncs.com/img/image-20201222143942956.png)

### 7.增加爬取新闻的功能

因为新闻网页是下拉动态加载的，所以需要使用selenium来模拟动态加载，使用了`chromedriver.exe`来进行模拟。得到的结果是一个html的代码内容，需要使用`BeautifulSoup`来解析，并存储为文件。

现阶段只能做到爬取后覆盖原文件进行存储，以后可以添加验证重复项来存储。