import pandas as pd
import json


class Response:
    def __init__(self):
        # self.request_name = request_name
        pass
    '''
    因为文件要在app.py里面引用，所以读取文件的位置要改成相对于app.py的位置，之前在本文件内调试都是../static开头，没有问题。
    但是要想在app.py里面正常使用，必须改成./static开头，这一点要明确。
    '''
    # 获取各个国家的预测数据

    # TODO:将所有的api接口做好，并且调试清楚
    def getPredictData(self, request_name, orient='split'):
        df = pd.read_csv("./static/data/predict.csv")
        d = df.loc[df['国家名'] == str(request_name), :]
        # 数据有37天的，只取30天的数据用于展示
        data = d[['日期', '确诊病例', '预测病例']].iloc[-30:, :]
        df_json = data.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取单个国家的数据，用在单个国家详情中
    def getWorldSingleData(self, request_name, orient='split'):
        df = pd.read_csv('./static/data/world_all.csv')
        data = df.loc[df['国家名'] == str(request_name), :]
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = data.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取所有国家的当天数据，用在世界疫情概览中，可以用表格呈现出来
    def getWorldAllData(self, orient='split'):
        df = pd.read_csv('./static/data/daily_world_data.csv')
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = df.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取中国省份的当天数据，用在中国疫情概览中，可以用在表格中
    def getChinaProvinDailyData(self, orient='split'):
        df = pd.read_csv('./static/data/daily_china_detail.csv')
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = df.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取中国省份的详细数据，是按日期排列的，用在省份详情中
    def getChinaProvinceData(self, request_name, orient='split'):
        df = pd.read_csv('./static/data/china_all.csv')
        data = df.loc[df['省份名'] == str(request_name), :]
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = data.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取新闻的总体数据，用于展示概括
    def getNews(self, orient='index'):
        df = pd.read_csv('./static/news/news.csv')
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = df.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取谣言的详细数据
    def getRumors(self, orient='index'):
        df = pd.read_csv('./static/rumors/rumors.csv')
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = df.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取绘图所需要的json数据
    def getMapJson(self, request_name, orient='columns'):
        name = str(request_name)
        df = pd.read_csv('./static/data/province.csv')
        print(name)
        if name == 'china':
            path = './static/mapJson/' + name + '.json'
        else:
            eng_name = df.iloc[df['省份名'] == name, :]
            path = './static/mapJson/' + eng_name + '.json'
        df_json = pd.read_json(path, orient='records')
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_jso = df_json.to_json(orient=orient, force_ascii=False)
        # 直接将json类型的数据发送到前端
        return df_jso


'''
转换为json类型后，需要的数据在'data'这个key里面，值是一个数组，还需要前端使用JS将数据处理一下。
'''
if __name__ == '__main__':
    response = Response().getMapJson('china')
    print(response)
