# main.py是将所有的处理数据的模块统一起来，在这里执行，那么app.py中就只需要执行main.py就可以了。
from toolspkg.getNews import *
from toolspkg.cleanData import CleanData, dealData
from toolspkg.predict import *
import time

if __name__ == '__main__':
    start = time.time()
    # 实例化一个对象
    cleanData = CleanData()
    dealData = dealData()
    try:
        # 清洗数据
        cleanData.getNum()
        cleanData.combineNum()
        cleanData.translateToChinese()
        cleanData.getApiData()
        dealData.dealWorldData()

        # 获取新闻
        content = get_content()
        data = parseContent(content)
        data_1 = get_newsItemContent(data)
        toCsv(data_1)

        # 计算预测数据
        ls = get_names()
        with ThreadPoolExecutor() as pool:
            df_empty = pd.DataFrame(columns=['日期', '确诊病例', '预测病例', '国家名'])
            results = pool.map(predict_each, ls)

            for result in results:
                df_empty = pd.concat([df_empty, result], ignore_index=True)

        df_empty.to_csv(
            '../static/data/predict.csv',
            sep=',',
            index=False,
            encoding='utf-8')
    except Exception as e:
        print(str(e))
    # print(re)
    end = time.time()
    print('用时：', end - start)
