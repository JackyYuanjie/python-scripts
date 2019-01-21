# -*- coding:utf-8 -*-

#author: firstoneyuan
#email: devops_yj@163.com

"""
分析Ajax爬取今日头条街拍美图

通过分析Ajax请求来抓取网页数据的方法:

目标: 今日头条街拍美图,抓取完成后,将魅族图片文件夹下载到本地并保存.
1. 准备工作: 安装requests库
2. 抓取分析:
    在抓取之前,先分析抓取的逻辑,打开今日头条的首页: https://www.toutiao.com/
    在搜索入库,输入街拍 搜索一下,
    这些内容由Ajax加载,然后用JavaScript渲染出来的.切换到XHR过滤选项卡,查看一下有没有Ajax请求. 再点击Preview按钮,发现这里有许多条数据.  这些数据确实是由Ajax加载的. 

    其中的图片对应date字段中的一条数据,每条数据还有一个image_list字段,它是列表形式,其中就包含了组图的所有图片列表.

   将列表中的url字段提取出来并下载. 每一组图都建立一个文件夹,文件夹名称为组图的标题.

    分析URL的规律, 切换回Headers选项卡,观察它的请求URL和Headers信息.

    是一个GET请求,请求URL的参数有offset,format,keyword,autoload,count和cur_tab, 找出这些参数的规律.
    滑动页面,会加载一些新的Ajax请求.

    对比一下这几个ajax请求的url, 观察一下有那几个参数会经常变化,这里发现变化的只有offset参数. 第二次请求的offset值为20,第三次为40.  这个offset值就是偏移量. 推断出count参数就是一次性获取的数据条数. 用offset参数来控制数据分页.

    接下来,通过接口批量获取数据,然后将数据解析,将图片下载下来即可.
"""

import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool

# 实现一个方法,加载单个Ajax请求的结果. 将offset当做参数传递.

def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }

    # 用urlencode方法构造请求的GET参数

    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)

    try:
        # 用requests请求这个链接,
        response = requests.get(url)
        # 返回状态码,调用response的json方法将结果转为JSON格式,然后返回.
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

# 实现一个解析方法: 提取每条数据的image_list字段中的每一张图片链接,将图片链接和图片所属的标题一并返回,此时可以构造一个生成器.
def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': 'https:' + image.get('url'),
                    'title': title
                }


# 实现一个保存图片的方法, item是get_images方法返回的一个字典.
# 先根据item的title来创建文件夹,然后请求这个图片链接,获取图片的二进制数据,以二进制的形式写入文件. 图片的名称可以使用其内容的MD5值.可以去除重复.
def save_image(item):
    img_path = 'jiepaiImages' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)


    # if not os.path.exists(item.get('title')):
        # os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name = md5(response.content).hexdigest(),
                file_suffix='jpg'
            )
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded',file_path)
    except requests.ConnectionError:
        print('Failed to Save Image, item %s' % item)


# 构造一个offset数组,遍历offset,提取图片链接,并将其下载
def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

# 定义了分页的起始页数和终止页数.
GROUP_START = 1
GROUP_END = 20

# 利用多线程的线程池,调用其map方法实现多线程下载.
if __name__=="__main__":
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START,GROUP_END + 1)])
    pool.map(main,groups)
    pool.close()
    pool.join()
