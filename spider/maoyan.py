# -*- coding:utf-8 -*-

# 利用requests库和正则表达式抓取猫眼电影TOP100的内容
"""
1. 目标: 提取猫眼电影TOP100的电影名称,时间,评分,图片等信息.提取站点: https://maoyan.com/board/4, 保存至文件中.

2. 准备工作:
    pip3 install requests

3. 抓取分析
    排名第一电影:霸王别姬,页面中显示信息: 影片名称,主演,上映时间,上映地区,评分,图片等信息.

    点击第2页,观察URL和内容变化
    offset=10 这是一个偏移量的参数,
    offset代表偏移量值,如果偏移量为n,则显示的电影序号为n+1到n+10,
    每页显示10个. 
    获取TOP100电影,分开请求10次,10次的offset参数分别设置为0,10,..即可. 获取不同页面后,再用正则表达式提取出相关信息.

4. 抓取首页
    抓取第一页,传入url参数,将抓取页面结果返回,再通过main()方法调用.
"""
import requests,re,json,time
from requests.exceptions import RequestException

def get_one(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
'''
def main():
    url = 'https://maoyan.com/board/4'
    html = get_one(url)
    print(html)

main()
#  成功获取首页源代码,获取源代码后,解析页面,提取出重要信息.
'''

"""
5. 正则提取
    打开开发者工具,在Network(Response)选项卡中查看原始请求得到的源代码.
    注意: 在Elements查看的源码可能经过js操作与原始请求不同.

    一部电影信息对应的源代码是一个dd节点,用正则表达式来提取电影信息.
    先提取它的排名信息,它的排名信息是在class为board-index的i节点内, 利用非贪婪匹配来提取i节点内的信息.源码为:<dd> <i class="board-index board-index-1">1</i> ...</dd>, 正则表达式为: <dd>.*?board-index.*?>(.*?)</i>

    接下来提取电影图片,后面有a节点,其内部有两个img节点,第二个img节点的data-src属性是图片的链接,这里提取第二个img节点的data-src属性,
    源码为: 
     <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img" />
    </a>

    正则表达式为:<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"

    需要提取电影名称,在后面的p节点内,class为name,用name做一个标志位,然后进一步提取到其内a节点的正文内容,
    源码为:
    <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
        <p class="star">
    正则表达式为: <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>

    再提取主演,发布时间,评分等内容时,都是相同原理,
    源码为:
            <p class="star">
                主演：张国荣,张丰毅,巩俐
        </p>
<p class="releasetime">上映时间：1993-01-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>        
    </div>

    正则表达式写为: <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>
    

    一个正则表达式可以匹配一个电影的结果,里面匹配了7个信息,通过调用findall()方法提取出所有的内容.
"""

# 定义解析页面的方法,通过正则表达式从结果中提取出需要的内容.
def parse_one(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)

    items = re.findall(pattern,html)
    # print(items)
    # 成功将一页的10个电影信息都提取出来,这是一个列表形式.

    # 将匹配结果处理一下,遍历提取结果并生成字典,
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }
    # print(item)
    # 成功提取出电影排名,图片,标题,演员,时间,评分等内容.并赋值为字典,形成结构化数据. 成功获取单页的电影信息.

'''
def main():
    url = 'https://maoyan.com/board/4'
    html = get_one(url)
    parse = parse_one(html)
    # print(html)
    print(parse)

main()
'''



'''
6. 写入文件
    将提取结果写入文件,通过JSON库的dumps()方法实现字典的序列化,并指定ensure_ascii参数为False,保证输出结果为中文.
'''
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
    # 调用write_to_file()方法实现将字典写入到文件,content参数就是单部电影的提取结果,是一个字典形式.


'''
7. 整合代码
    实现main方法调用前面实现的方法,将单页电影结果写入文件.
'''
'''
def main():
    url = 'https://maoyan.com/board/4'
    html = get_one(url)
    for item in parse_one(html):
        write_to_file(item)
# 完成单页电影提取, 首页10部电影成功提取并保存到文件中.

main()
'''

'''
8. 分页爬取
    需要抓取TOP100的电影,需要遍历,给这个链接传入offset参数,
'''

# 需要将main()方法修改一下,接收一个offset值作为偏移量,然后构造URL进行爬取.

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one(url)
    for item in parse_one(html):
        print(item)
        write_to_file(item)

# 添加调用:
if __name__=='__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)

# 运行脚本,页面输出信息和results.txt文件内都可以看到TOP100电影信息.





