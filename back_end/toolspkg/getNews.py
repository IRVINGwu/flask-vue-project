from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd


# 使用selenium模拟页面滚动，获取内容
def get_content():
    # 创建chrome浏览器驱动，无头模式
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        "../static/tools/chromedriver.exe",
        options=chrome_options)

    # 加载界面
    driver.get(
        "https://www.sohu.com/c/8/1461?spm=smpc.news-home.top-subnav.3.1608633802228Wu4UITH")
    time.sleep(3)

    # 获取页面初始高度
    js = "return action=document.body.scrollHeight"
    height = driver.execute_script(js)

    # 将滚动条调整至页面底部
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(5)

    # 定义初始时间戳（秒）
    t1 = int(time.time())

    # 定义循环标识，用于终止while循环
    status = 1000

    # 重试次数
    num = 0

    while status > 0:
        # 获取当前时间戳（秒）
        t2 = int(time.time())
        # 判断时间初始时间戳和当前时间戳相差是否大于30秒，小于30秒则下拉滚动条
        if t2 - t1 < 30:
            new_height = driver.execute_script(js)
            if new_height > height:
                time.sleep(1)
                driver.execute_script(
                    'window.scrollTo(0, document.body.scrollHeight)')
                # 重置初始页面高度
                height = new_height
                # 重置初始时间戳，重新计时
                t1 = int(time.time())

            status -= 50
        elif num < 3:  # 当超过30秒页面高度仍然没有更新时，进入重试逻辑，重试3次，每次等待30秒
            time.sleep(3)
            num = num + 1
        else:  # 超时并超过重试次数，程序结束跳出循环，并认为页面已经加载完毕！
            print("滚动条已经处于页面最下方！")
            # 滚动条调整至页面顶部
            driver.execute_script('window.scrollTo(0, 0)')
            break

    # 打印页面源码
    # content = driver.page_source
    # print(content)
    return driver.page_source


# 使用BeautifulSoup来解析网页内容
def parseContent(content):
    soup = BeautifulSoup(content, 'html.parser')
    # print(soup)

    # 获取今天（现在时间）
    today = datetime.datetime.today()
    # 昨天
    yesterday = today - datetime.timedelta(days=1)

    data = []

    for new in soup.select(
            '.news-wrapper>.news-box'):  # BeautifulSoup提供的方法通过select选择想要的html节点类名，标签等，获取到的内容会被放到列表中
        try:
            if len(new.select('h4')) > 0 and len(
                    new.select('.other>.name>a')) != 0:
                ls = ['疫情', 'covid-19', '疫苗', '新冠']
                for i in ls:
                    if i in new.select('h4')[0].text:
                        obj = {
                            'title': '',
                            'link': '',
                            'time': '',
                            'source': ''
                        }
                        # obj = {}
                        obj['title'] = new.select(
                            'h4')[0].text.replace('\n', '').strip()
                        obj['link'] = new.select('h4>a')[0]['href']

                        # 由于时间格式不一样，有的有data-val这个属性，有的没有，所以直接获取标签里面的数据，然后进行转换。
                        tim = new.select('.other>.time')[0].string.split(' ')
                        if tim[0] == '今天':
                            obj['time'] = today.strftime(
                                "%Y-%m-%d") + ' ' + tim[1]
                        elif tim[0] == '昨天':
                            obj['time'] = yesterday.strftime(
                                "%Y-%m-%d") + ' ' + tim[1]
                        else:
                            obj['time'] = ''

                        obj['source'] = new.select('.other>.name>a')[0].string
                #         print(obj)
                        data.append(obj)
                        break
        except Exception as e:
            print(str(e))

    return data


# 获取每个新闻的详细内容
def get_newsItemContent(data):
    for i in range(len(data)):
        lin = data[i]['link']
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
        res = requests.get(lin, headers=headers)

        # 请求获取链接返回的内容
        res.encoding = 'utf-8'  # 设置编码格式为utf-8
        # 前面已经介绍将html文档格式化为一个树形结构，每个节点都是一个对python对象，方便获取节点内容
        soup = BeautifulSoup(res.text, 'html.parser')

        cont = ''
        for new in soup.select(
                '#mp-editor > p'):  # BeautifulSoup提供的方法通过select选择想要的html节点类名，标签等，获取到的内容会被放到列表中
            p = ''
            if len(new) > 0 and new.string is not None and '原标题' not in new.string:
                p = '<p>' + new.string + '</p>'
                cont += p
        data[i]['content'] = cont
    return data


# 将data中的数据保存为csv文件
def toCsv(data):
    '''
    因为获取到的数据现在很难排除重复项，所以直接保存为一个文件，项目操作时，操作一次就是一个新文件，直接覆盖。
    以后可以这样做，每天晚上爬取，判断时间是‘今天’的就存储，这样就能够排除一部分重复的内容。
    python有一个APScheduler定时任务模块，可以定时执行任务。
    '''
    # df_news = pd.read_csv('../static/news/news_new.csv', encoding='utf-8')
    # df_news.drop(['id'], axis=1, inplace=True)
    titles = [data[i]['title'] for i in range(len(data))]
    links = [data[i]['link'] for i in range(len(data))]
    times = [data[i]['time'] for i in range(len(data))]
    sources = [data[i]['source'] for i in range(len(data))]
    contents = [data[i]['content'] for i in range(len(data))]

    dt = {
        'title': titles,
        'link': links,
        'time': times,
        'source': sources,
        'content': contents
    }
    df = pd.DataFrame(dt)

    # 新增一列时间列，将新闻按照时间来进行排序
    df['date'] = pd.to_datetime(df['time'])
    df = df.sort_values(by='date', ascending=False)

    df['id'] = df.index
    # df_new = pd.concat([df, df_news])
    # df_new = df_new.sort_values(by='date', ascending=False)
    # df_new['id'] = df_new.index
    df.to_csv(
        '../static/news/news_new.csv',
        encoding='utf-8',
        index=False
    )


if __name__ == '__main__':
    start = time.time()
    try:
        content = get_content()
        data = parseContent(content)
        data_1 = get_newsItemContent(data)
        toCsv(data_1)
    except Exception as e:
        print(str(e))
    end = time.time()
    print('爬取新闻用时：', end - start, '秒')
