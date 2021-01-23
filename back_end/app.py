from gevent import pywsgi, monkey
monkey.patch_all()

from toolspkg.response import Response
from flask_cors import CORS
from flask import Flask

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


@app.route('/api/rumors', methods=['GET'])
def get_rumors():
    response = Response().getRumors()
    return response

# 传送新闻数据到前端


@app.route('/api/news', methods=['GET'])
def get_news():
    response = Response().getNews()
    return response

# 传送新闻详情到前端


@app.route('/api/news/<number>', methods=['GET'])
def get_news_item(number):
    number = eval(number)
    response = Response().getNewsItem(number)
    return response


# 传送地图所需要的json数据到前端


@app.route('/api/mapJson/<name>', methods=['GET'])
def get_mapJson(name):
    name1 = str(name)
    response = Response().getMapJson(name1)
    return response


# 发送中国各个省份数据到前端，用于展示每个省份的具体情况
@app.route('/api/chinaProvinceDaily', methods=['GET'])
def get_chinaProvinceDaily():
    response = Response().getChinaProvinDailyData()
    return response


# 发送各个国家详情数据，用于展示每个国家的具体情况


@app.route('/api/worldDailyData/<country>', methods=['GET'])
def get_worldDailyData(country):
    response = Response().getWorldSingleData(country)
    return response

# 发送世界的详情数据，用于展示世界疫情数字


@app.route('/api/worldDaily', methods=['GET'])
def get_worldDaily():
    response = Response().getWorldDaily()
    return response

# 发送世界的详情数据，用于展示世界疫情发展趋势，线形图


@app.route('/api/worldSum', methods=['GET'])
def get_worldSum():
    response = Response().getWorldSum()
    return response

# 发送中国当天数据到前端，用于展示地图


@app.route('/api/chinaDaily', methods=['GET'])
def get_chinaDaily():
    response = Response().getChinaDaily()
    return response

# 发送中国当天数据到前端，用于展示按日期排列的线形图


@app.route('/api/chinaSum', methods=['GET'])
def get_chinaSum():
    response = Response().getChinaSum()
    return response

# 发送中国当天数据到前端，用于展示线形图


@app.route('/api/chinaProvince/<name>', methods=['GET'])
def get_chinaProvince(name):
    response = Response().getChinaProvinceData(name)
    return response

# 发送中国省份的城市当天数据到前端，用于展示地图和table表格


@app.route('/api/chinaProvinCity/<name>', methods=['GET'])
def get_chinaCity(name):
    response = Response().getChinaCityData(name)
    return response


# 传送疫情预测数据到前端
@app.route('/api/worldpredict/<name>', methods=['GET'])
def get_worldPredict(name):
    response = Response().getPredictData(name)
    return response


# 因为有一些文件是数据处理的文件，需要在后端服务器已启动就执行，所以需要在此文件中引入，然后放到这里执行。
if __name__ == '__main__':
    # app.run(
    #     host='192.168.10.24',
    #     port=8080,
    #     debug=True
    # )
    # 使用gevent的服务器
    server = pywsgi.WSGIServer(('192.168.10.24', 8080), app)
    server.serve_forever()
