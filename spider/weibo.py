# -*- coding:utf-8 -*-

#author: firstoneyuan
#email: devops_yj@163.com

# 定义一个方法来获取每次请求的结果,在请求时,page是一个可变参数,可将它作为方法的参数传递进来:
from urllib.parse import urlencode
import requests,pymongo
from pyquery import PyQuery as pq 

# 定义变量,表示请求URL的前半部分.
base_url = 'https://m.weibo.cn/api/container/getIndex?'

# 请求头设置
headers = {
    'Host': 'm.weibo.cn',
    'Referer':'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

client = pymongo.MongoClient(host='x.x.x.x',port=27017)
db = client.weibo
collection = db.weibo
max_page = 10

def get_page(page):

    # 构建参数字典, page是可变参数.
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid':'1076032830678474',
        'page': page
    }

    # 调用urlencode方法将参数转为URL的GET请求参数.base_url和参数拼接形成新的URL.
    url = base_url + urlencode(params)

    try:
        # 请求该链接,加入headers,
        response = requests.get(url,headers=headers)

        # 判断响应的状态码.
        if response.status_code == 200:
            # 调用json方法将内容解析并返回.
            return response.json(),page
    except requests.ConnectionError as e:
        # 输出异常信息
        print('Error',e.args)

# 定义一个解析方法,从结果中提取信息,先遍历cards,再获取mblog中的各个信息,赋值为一个新的字典返回即可.

def parse_page(json,page:int):
    if json:
        items = json.get('data').get('cards')
        for index,item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog',{})
                weiboone = {}
                weiboone['id'] = item.get('id')
                weiboone['text'] = pq(item.get('text')).text()
                weiboone['attitudes'] = item.get('attitudes_count')
                weiboone['comments'] = item.get('comments_count')
                weiboone['reposts'] = item.get('reposts_count')
                yield weiboone
            # 借助pyquery将正文中的HTML标签去掉.


def save_to_mongo(result):
    if collection.insert(result):
        print('saved to Mongo')

if __name__=='__main__':
    for page in range(1,max_page + 1):
        json = get_page(page)
        results = parse_page(*json)
        for result in results:
            print(result)
            save_to_mongo(result)

