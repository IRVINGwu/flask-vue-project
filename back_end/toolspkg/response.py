import pandas as pd
import json


class Response:
    def __init__(self, request_name):
        self.request_name = request_name

    # 获取各个国家的预测数据
    def getPredictData(self, request_name, orient='split'):
        df = pd.read_csv("../static/data/predict.csv")
        d = df.loc[df['国家名'] == str(request_name), :]
        # 数据有37天的，只取30天的数据用于展示
        data = d[['日期', '确诊病例', '预测病例']].iloc[-30:, :]
        df_json = data.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取单个国家的数据，用在单个国家详情中
    def getWorldSingleData(self, request_name, orient='split'):
        df = pd.read_csv('../static/data/world_all.csv')
        data = df.loc[df['国家名'] == str(request_name), :]
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = data.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取所有国家的当天数据，用在世界疫情概览中，可以用表格呈现出来
    def getWorldAllData(self, orient='split'):
        df = pd.read_csv('../static/data/daily_world_data.csv')
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = df.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取中国省份的当天数据，用在中国疫情概览中，可以用在表格中
    def getChinaProvinDailyData(self, orient='split'):
        df = pd.read_csv('../static/data/daily_china_detail.csv')
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = df.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取中国省份的详细数据，是按日期排列的，用在省份详情中
    def getChinaProvinceData(self, request_name, orient='split'):
        df = pd.read_csv('../static/data/china_all.csv')
        data = df.loc[df['省份名'] == str(request_name), :]
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = data.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)



'''
转换为json类型后，需要的数据在'data'这个key里面，值是一个数组，还需要前端使用JS将数据处理一下。
'''
if __name__ == '__main__':
    pass
