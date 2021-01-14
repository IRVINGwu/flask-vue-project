import pandas as pd
import numpy as np
import json
import requests
import ast


class Response:
    def __init__(self):
        # self.request_name = request_name
        pass
    '''
    因为文件要在app.py里面引用，所以读取文件的位置要改成相对于app.py的位置，之前在本文件内调试都是../static开头，没有问题。
    但是要想在app.py里面正常使用，必须改成./static开头，这一点要明确。
    '''
    # 获取各个国家的预测数据

    def getPredictData(self, request_name):
        df = pd.read_csv("./static/data/predict.csv")
        try:
            d = df.loc[df['国家名'] == str(request_name), :]
            # 数据有37天的，只取30天的数据用于展示
            data = d[['日期', '确诊病例', '预测病例']].iloc[-30:, :]
            df_json = data.to_json(orient='index', force_ascii=False)
            return json.loads(df_json)
        except BaseException:
            return '暂未提供预测数据'

    # 获取单个国家的数据，用在单个国家详情中
    def getWorldSingleData(self, request_name, orient='index'):
        df = pd.read_csv('./static/data/world_all.csv')
        try:
            # 注意：传递过来的是中文国家名，所以这里不需要对request_name进行处理
            data = df.loc[df['国家名'] == str(request_name), :]
            # 将dataframe数据类型变为json类型，方便前端进行处理
            df_json = data.to_json(orient=orient, force_ascii=False)
            return json.loads(df_json)
        except BaseException:
            return '详情暂时未找到'

    # 获取世界按天排列的总数据，用于展示线形图
    def getWorldSum(self, orient='table'):
        df = pd.read_csv('./static/data/world_sum_dayline.csv')
        df_json = df.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取世界当天的疫情数据，用于展示tablelist
    def getWorldDaily(self, orient='index'):
        r = requests.get(
            'https://c.m.163.com/ug/api/wuhan/app/data/list-total',
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"})

        # 返回的数据r.json()是一个字典，需要转换为json
        content = json.dumps(r.json(), ensure_ascii=False)
        df = pd.read_json(content, orient='records')
        # 因为筛选出来的数据是字典类型，所以需要转换为json类型
        data = json.dumps(df.loc['areaTree', 'data'], ensure_ascii=False)
        return data

    # 获取中国当天的数据，用于展示地图

    def getChinaDaily(self):
        r = requests.get(
            'https://c.m.163.com/ug/api/wuhan/app/data/list-total',
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"})

        # 返回的数据r.json()是一个字典，需要转换为json
        content = json.dumps(r.json(), ensure_ascii=False)
        # df = pd.read_json(content, orient='records')
        # # 因为筛选出来的数据是字典类型，所以需要转换为json类型
        # data = json.dumps(df.loc['chinaTotal', 'data'], ensure_ascii=False)
        return content

    # 获取中国按天数排列的数据，用于展示线形图
    def getChinaSum(self, orient='index'):
        r = requests.get(
            'https://c.m.163.com/ug/api/wuhan/app/data/list-total',
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"})

        # 返回的数据r.json()是一个字典，需要转换为json
        content = json.dumps(r.json(), ensure_ascii=False)
        df = pd.read_json(content, orient='records')
        # 因为筛选出来的数据是list类型，所以需要转换为json类型
        df_json = df.loc['chinaDayList', 'data']
        df_jso = json.dumps(df_json, ensure_ascii=False)
        return df_jso

    # 获取所有国家的当天数据，用在世界疫情概览中，可以用表格呈现出来
    def getWorldAllData(self, orient='split'):
        df = pd.read_csv('./static/data/daily_world_data.csv')
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = df.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取中国省份的当天数据，用在中国疫情概览中，可以用在表格中
    def getChinaProvinDailyData(self, orient='index'):
        r = requests.get(
            'https://c.m.163.com/ug/api/wuhan/app/data/list-total',
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"})

        # 返回的数据r.json()是一个字典，需要转换为json
        content = json.dumps(r.json(), ensure_ascii=False)
        df = pd.read_json(content, orient='records')
        # 因为筛选出来的数据是list类型，所以需要转换为json类型
        df_json = df.loc['areaTree', 'data']
        df_jso = json.dumps(df_json, ensure_ascii=False)
        return df_jso

    # 获取中国省份的详细数据，是按日期排列的，用在省份详情中

    def getChinaProvinceData(self, request_name, orient='split'):
        df = pd.read_csv('./static/data/china_all.csv')
        try:
            data = df.loc[df['省份名'] == str(request_name), :]
            # 将dataframe数据类型变为json类型，方便前端进行处理
            df_json = data.to_json(orient=orient, force_ascii=False)
            return json.loads(df_json)
        except BaseException:
            return '该省份详情数据暂时未更新'

    # 获取中国省份城市当天的详细数据，用在每个省份的城市详情中

    def getChinaCityData(self, request_name, orient='index'):
        df = pd.read_csv('./static/data/daily_china_detail.csv')
        try:
            data = df.loc[df['省份名'] == str(request_name), :]['子项目'].values[0]

            # 因为data数据类型是列表，需要构造成df类型，才能转成json
            d = ast.literal_eval(data)
            dt = {
                '0': d
            }
            data1 = pd.DataFrame(dt)
            # 将dataframe数据类型变为json类型，方便前端进行处理
            df_json = data1.to_json(orient=orient, force_ascii=False)
            return json.loads(df_json)
        except BaseException:
            return '该省份详情数据暂时未更新'

    # 获取新闻的总体数据，用于展示概括
    def getNews(self, orient='index'):
        df = pd.read_csv('./static/news/news_new.csv')
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = df.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取新闻的总体数据，用于展示概括
    def getNewsItem(self, id, orient='table'):
        df = pd.read_csv('./static/news/news_new.csv')
        data = df.loc[df['id'] == id, :]
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = data.to_json(orient=orient, force_ascii=False, index=False)
        return json.loads(df_json)

    # 获取谣言的详细数据
    def getRumors(self, orient='index'):
        df = pd.read_csv('./static/rumors/rumors.csv')
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_json = df.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

    # 获取绘图所需要的json数据
    def getMapJson(self, request_name, orient='index'):
        name = str(request_name)
        df = pd.read_csv('./static/data/province.csv')
        # print(name)
        if name == 'china':
            path = './static/mapJson/' + name + '1.json'
        elif name == '香港':
            path = './static/mapJson/xianggang.json'
        elif name == '台湾':
            path = './static/mapJson/taiwan.json'
        elif name == '西藏':
            path = './static/mapJson/xizang.json'
        else:
            try:
                # 查询数据真是需要好好学啊
                eng_name = df.loc[df['省份名'] == name, :].values[0][0]
                # 将首字母改成小写，以匹配json里面的文件名
                eng_name = eng_name[0].lower() + eng_name[1:]
                # print(eng_name)
                path = './static/mapJson/' + eng_name + '.json'
            except BaseException:
                path = './static/mapJson/china.json'

        # 这里的typ='series'，终于把json文件原封不动的传递过去了，没有问题了
        df_json = pd.read_json(path, orient='records', typ='series')
        # df_json = pd.read_json(path)
        # 将dataframe数据类型变为json类型，方便前端进行处理
        df_jso = df_json.to_json(orient=orient, force_ascii=False)
        # 直接将json类型的数据发送到前端
        return df_jso


'''
转换为json类型后，需要的数据在'data'这个key里面，值是一个数组，还需要前端使用JS将数据处理一下。
'''
if __name__ == '__main__':
    response = Response().getNewsItem(1)
    print(response)
