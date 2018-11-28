import requests  # 请求URL页面内容
from bs4 import BeautifulSoup  # 获取页面元素
import pymysql  # 链接数据库
import time  # 时间函数
import lxml  # 解析库（支持HTML\XML解析，支持XPATH解析）


# get_page函数作用：通过requests的get方法得到url链接的内容，再整合成BeautifulSoup可以处理的格式
def get_page(url):
    response = requests.get(url)


    soup = BeautifulSoup(response.text, 'lxml')
    return soup


# get_links函数的作用：获取列表页所有租房链接
def get_links(link_url):
    soup = get_page(link_url)


    links_div = soup.find_all('div', class_="pic-panel")
    links = [div.a.get('href') for div in links_div]
    return links


# get_house_info函数作用是：获取某一个租房页面的信息：价格、单位、面积等
def get_house_info(house_url):
    soup = get_page(house_url)


    price = soup.find('span', class_='total').text
    unit = soup.find('span', class_='unit').text.strip()
    area = 'test'  # 这里area字段我们自定义一个test做测试
    info = {
        '价格': price,
        '单位': unit,
        '面积': area
    }
    return info
# 数据库的配置信息写到字典
DataBase = {
    'host': '127.0.0.1',
    'database': 'exam',
    'user': 'root',
    'password': 'Ln2018!!',
    'charset': 'utf8mb4'}


# 链接数据库
def get_db(setting):
    return pymysql.connect(**setting)


# 向数据库插入爬虫得到的数据
def insert(db, house):
    values = "'{}'," * 2 + "'{}'"


    sql_values = values.format(house['价格'], house['单位'], house['面积'])
    sql = """
insert  into house(price,unit,area) values({})
""".format(sql_values)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
# 主程序流程：1.连接数据库 2.得到各个房源信息的URL列表3.FOR循环从第一个URL开始获取房源具体信息（价格等）4.一条一条地插入数据库
db = get_db(DataBase)
links = get_links('https://bj.lianjia.com/zufang/')
for link in links:
    time.sleep(2)
house = get_house_info(link)
insert(db, house)