import time
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from datetime import date, timedelta

'''
因为文件要在app.py里面引用，所以读取文件的位置要改成相对于app.py的位置，之前在本文件内调试都是../static开头，没有问题。
但是要想在app.py里面正常使用，必须改成./static开头，这一点要明确。
'''

# 获取国家的数据
def get_data(n):
    df = pd.read_csv("../static/data/world_all.csv")
    d = df.loc[df['国家名'] == str(n), :]
    data = d[['日期', '确诊病例']].iloc[-30:, :]
    return data

# 获取国家名列表


def get_names():
    df = pd.read_csv('../static/data/countries.csv')
    lis = df['国家名'].tolist()
    return lis


def predict_each(i):
    df = get_data(str(i))
    try:
        # 获取序列号和日期写序列
        a = len(df['日期'])
        xdata = list(range(a))
        xlabel = list(item for item in df['日期'].tolist())
        b = df['日期'].tolist()[-1].split('/')
        start_date = date(eval('20' + str(b[2])), int(b[0]), int(b[1]) + 1)

        # 为序列和日期增加7天
        xdata.extend(list(range(a, a + 7)))
        xlabel.extend(
            list(str((start_date + timedelta(i)).strftime("%m/%d/%y")) for i in range(7)))

        X = np.array(xdata).reshape(-1, 1)
        y = np.array(df['确诊病例'].tolist()).reshape(-1, 1)

        # 因为日期增加了7天，而真实累计病例数据没有变，所以X比y多7天数据，拿5天数据出来做测试
        X_train = X[:-12]
        y_train = y[:-5]

        # --------------------------------四次多项式
        poly4 = PolynomialFeatures(degree=4)
        X_ploy = poly4.fit_transform(X_train)
        l4 = LinearRegression()
        l4.fit(X_ploy, y_train)

        # 得到预测后的数据
        # x_data = xdata
        y_data = l4.predict(poly4.fit_transform(X))

        # 生成该国的数据
        df_1 = pd.DataFrame(y_data, columns=['预测病例'])
        df_1['日期'] = xlabel
        df_1['国家名'] = [str(i)] * 37
        df_2 = pd.merge(
            left=df,
            right=df_1,
            left_on='日期',
            right_on='日期',
            how='outer')
        return df_2
    except BaseException:
        print(str(i), '文件有错误')
        return


if __name__ == '__main__':
    start = time.time()
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
    end = time.time()
    print('分析用时：', end - start)
