import pandas as pd
import time
import requests
import json
import numpy as np


class CleanData:
    def __init__(self):
        pass
    # 从原始文件中提取出中国和世界的数据，并转置，让日期称为index，保存为文件

    '''
    因为文件要在app.py里面引用，所以读取文件的位置要改成相对于app.py的位置，之前在本文件内调试都是../static开头，没有问题。
    但是要想在app.py里面正常使用，必须改成./static开头，这一点要明确。
    '''

    def getNum(self):
        urls = [
            'time_series_covid19_confirmed_global.csv',
            'time_series_covid19_deaths_global.csv',
            'time_series_covid19_recovered_global.csv']
        # 因为pandas不能同时处理to_csv这种方法，所以要分开
        for i in urls:
            # 保存为文件的地址，文件名取的是confirmed_china这种形式
            name = '../static/data/' + str(i.split('_')[3]) + '_china.csv'
            # 读取文件的地址
            path = '../static/data/' + str(i)
            df = pd.read_csv(path, encoding='utf-8')

            # 获取中国的数据
            df_china = df.loc[df['Country/Region'] == 'China', :]
            df_china.drop(['Country/Region', 'Lat', 'Long'],
                          axis=1, inplace=True)
            # 将省份作为行标，便于后面的行列转置
            df_china.set_index('Province/State', inplace=True)
            # 进行行列转置
            df_china = df_china.stack()

            # 保存为单独的文件
            df_china.to_csv(name, sep=',', encoding='utf-8')
        for i in urls:
            # 保存为文件的地址，文件名取的是confirmed_china这种形式
            name1 = '../static/data/' + str(i.split('_')[3]) + '_world.csv'
            # 读取文件的地址
            path = '../static/data/' + str(i)
            df = pd.read_csv(path, encoding='utf-8')

            # 获取各个国家的数据
            df_world = df
            df_world.drop(['Province/State', 'Lat', 'Long'],
                          axis=1, inplace=True)
            df_world = df_world.groupby('Country/Region').sum()
            # 因为数据的index已经是国家名了，所以只需要进行行列转置即可
            df_world_new = df_world.stack()

            # 保存为单独的文件
            df_world_new.to_csv(name1, sep=',', encoding='utf-8')

    # 合并清洗好的中国、世界疫情数据文件，并保存为一个单独的文件

    def combineNum(self):
        ls = ['confirmed_china', 'deaths_china', 'recovered_china']
        ls_world = ['confirmed_world', 'deaths_world', 'recovered_world']
        titles = ['确诊病例', '死亡病例', '康复病例']
        df_empty = pd.DataFrame(columns=['省份', '日期'])
        df_empty_world = pd.DataFrame(columns=['国家', '日期'])
        try:
            for i in range(3):
                # 读取文件
                path = '../static/data/' + ls[i] + '.csv'
                df = pd.read_csv(
                    path,
                    encoding='utf-8',
                    names=[
                        '省份',
                        '日期',
                        titles[i]])

                # 删除首行不需要的标题
                df = df.drop(0, axis=0)

                # 合并文件
                df_empty = pd.merge(
                    left=df_empty, right=df, on=[
                        '省份', '日期'], how='outer')
            # 保存为文件
            df_empty.to_csv(
                '../static/data/china_all.csv',
                index=False,
                sep=',',
                encoding='utf-8')
            for i in range(3):
                # 读取文件
                path_world = '../static/data/' + ls_world[i] + '.csv'
                df_world = pd.read_csv(
                    path_world,
                    encoding='utf-8',
                    names=[
                        '国家',
                        '日期',
                        titles[i]])

                # 删除首行不需要的标题
                df_world = df_world.drop(0, axis=0)

                # 合并文件
                df_empty_world = pd.merge(
                    left=df_empty_world, right=df_world, on=[
                        '国家', '日期'], how='outer')

            # 保存为文件
            df_empty_world.to_csv(
                '../static/data/world_all.csv',
                index=False,
                sep=',',
                encoding='utf-8')
        except BaseException:
            print('不成功')

    # 进一步清洗中国、世界疫情数据总表，将省份、国家名的英文名换为中文名
    def translateToChinese(self):
        # 读取文件
        df_provin = pd.read_csv(
            '../static/data/province.csv',
            encoding='utf-8')
        df_china = pd.read_csv(
            '../static/data/china_all.csv',
            encoding='utf-8')

        # 更换为中文名
        df_china = pd.merge(
            left=df_provin,
            right=df_china,
            left_on='province',
            right_on='省份')
        df_china.drop(['province', '省份'], axis=1, inplace=True)

        # 保存文件
        df_china.to_csv(
            '../static/data/china_all.csv',
            index=False,
            sep=',',
            encoding='utf-8')
        # 读取文件
        df_con = pd.read_csv('../static/data/countries.csv', encoding='utf-8')
        df_world = pd.read_csv(
            '../static/data/world_all.csv',
            encoding='utf-8')

        # 更换为中文名
        df_world = pd.merge(
            left=df_con,
            right=df_world,
            left_on='countries',
            right_on='国家')
        df_world.drop(['countries', '国家'], axis=1, inplace=True)
        # 保存文件
        df_world.to_csv(
            '../static/data/world_all.csv',
            sep=',',
            index=False,
            encoding='utf-8')

    # 获取API的数据，并清洗保存为文件
    def getApiData(self):
        r = requests.get(
            'https://c.m.163.com/ug/api/wuhan/app/data/list-total',
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"})

        # 返回的数据r.json()是一个字典，需要转换为json
        content = json.dumps(r.json(), ensure_ascii=False)
        df_content = pd.read_json(content, orient='records')
        d1 = df_content.loc['areaTree', 'data']
        final_content = json.dumps(d1, ensure_ascii=False)
        df_world_daily = pd.read_json(final_content, orient='records')
        # 从json读取的数据，数据类型是NoneType，需要转换为dataframe类型才能进一步处理
        df_world = pd.DataFrame(
            df_world_daily,
            columns=[
                'today',
                'total',
                'extData',
                'name',
                'id',
                'lastUpdateTime',
                'children'])
        # 获取中国的数据
        df_china_detail = df_world.loc[2, 'children']

        # 拆分today列，并删除today列
        df_world_temp_1 = df_world['today'].apply(pd.Series)
        df_world_final_1 = pd.concat(
            [df_world, df_world_temp_1], axis=1).drop('today', axis=1)

        # 拆分total列，并删除total列
        world_titles = [
            '额外信息',
            '国家名',
            'id',
            '最新更新时间',
            '今日确诊',
            '今日疑似',
            '今日治愈',
            '今日死亡',
            '今日危重',
            '今日待确诊',
            '今日境外输入',
            '总确诊数',
            '总疑似数',
            '总治愈数',
            '总死亡数',
            '总危重数',
            '总境外输入数']

        df_world_temp_2 = df_world['total'].apply(pd.Series)
        df_world_final = pd.concat(
            [df_world_final_1, df_world_temp_2], axis=1).drop('total', axis=1)
        df_world_final.drop(['children'], axis=1, inplace=True)
        # 子项目没有必要存进去，因为另外会解析的
        df_world_final.columns = world_titles
        # 将世界数据保存为文件
        df_world_final.to_csv(
            '../static/data/daily_world_data.csv',
            encoding='utf-8',
            sep=',',
            index=False)

        # 各省份、城市的数据在children里面，不要把这个当成了儿童，其实是子项目的意思，将这个数据保存为单独的文件，其余的today和total都是
        # 单独的数据，内容很简单，可以直接显示。
        # f_china_today是字典类型，所以需要换成dataframe类型，这里的today_china直接从world_daily里面获取即可，不需要单独提取出来，
        # 因为内容很简单
        df_data = json.dumps(df_china_detail, ensure_ascii=False)
        df_china_det = pd.read_json(df_data, orient='records')
        df_china_daily = pd.DataFrame(df_china_det)

        # 拆分并删除today列
        df_china_temp_1 = df_china_daily['today'].apply(pd.Series)
        df_china_final_1 = pd.concat(
            [df_china_daily, df_china_temp_1], axis=1).drop('today', axis=1)
        # 拆分并删除total列
        china_titles = [
            '额外信息',
            '省份名',
            'id',
            '最新更新时间',
            '子项目',
            '今日确诊',
            '今日疑似',
            '今日治愈',
            '今日死亡',
            '今日危重',
            '今日待确诊',
            '总确诊数',
            '总疑似数',
            '总治愈数',
            '总死亡数',
            '总危重数',
            '境外输入数']

        df_china_temp_2 = df_china_daily['total'].apply(pd.Series)
        df_china_final = pd.concat(
            [df_china_final_1, df_china_temp_2], axis=1).drop('total', axis=1)
        df_china_final.drop(
            ['newConfirm', 'newDead', 'newHeal'], axis=1, inplace=True)
        # 子项目没有必要存进去，因为另外会解析的
        df_china_final.columns = china_titles
        df_china_final.to_csv(
            '../static/data/daily_china_detail.csv',
            encoding='utf-8',
            sep=',',
            index=False)


class dealData:
    def __init__(self):
        pass

    def dealWorldData(self, orient='table'):
        df = pd.read_csv('../static/data/world_all.csv')

        # 这一步是用pandas的to_datetime方法，将日期这一列的数据变成pandas可以处理的格式
        df['date'] = pd.to_datetime(df['日期'])
        data = df.groupby('date').agg(
            {"确诊病例": np.sum, "死亡病例": np.sum, "康复病例": np.sum})
        data.to_csv('../static/data/world_sum_dayline.csv')

if __name__ == '__main__':
    # 实例化一个对象
    cleanData = CleanData()
    dealData = dealData()
    start = time.time()
    try:
        cleanData.getNum()
        cleanData.combineNum()
        cleanData.translateToChinese()
        cleanData.getApiData()
        dealData.dealWorldData()
    except BaseException:
        print('不成功哦！')
    end = time.time()
    print('数据处理用时：', end - start, '秒')  # 1.6816秒


'''
无论是自己创建线程、多线程、多进程，都有一个问题，那就是我的IO都是相互依赖的，translate这个函数没有办法真正执行，先不用吧。
我在想，要不要把translate这个函数放到predict.py里面执行，反正里面要用到这个函数生成的文件。这样这里就可以使用多线程了。
'''
