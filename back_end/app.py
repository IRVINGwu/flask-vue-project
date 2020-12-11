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

@app.route('/mapJson/<name>',methods=['Get'])
def get_mapJson(name):
    name1 = str(name)
    print(name1)
    response = Response().getMapJson(name1)
    return response


# 因为有一些文件是数据处理的文件，需要在后端服务器已启动就执行，所以需要在此文件中引入，然后放到这里执行。
if __name__ == '__main__':
    app.run()
