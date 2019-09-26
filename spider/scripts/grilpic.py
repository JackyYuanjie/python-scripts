# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request as req 
import time 
import os 
import requests
from multiprocessing import Pool 

jpg = "F:\\PythonProject\\AI\\bibiPython\\spider\\scripts\\"

class Gril():
    '''
    妹子图网站
    '''
    def __init__(self):
        self.baseUrl="https://www.mzitu.com"
        self.header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        self.url_list = []

    def getRequestContent(self,url):
        '''
        获取页面请求信息
        '''
        try:
            req_str = req.Request(url,headers = self.header)
            response = req.urlopen(req_str,timeout = 10)
        except Exception as e:
            print(url)
            print("页面请求失败",e)
        else:
            return response.read().decode('utf-8')

    def spider(self,url):
        '''
        解析页面
        '''
        html = self.getRequestContent(url)
        # print(html)
        soup = BeautifulSoup(html,'html.parser')
        # print(soup)
        div = soup.find('div',attrs={'class': 'all'})
        # print(div)
        a_list = div.find_all('a')
        # print(len(a_list))
        # url_list = [] # 保存所有的网址
        for a in a_list:
            if "https://www.mzitu.com/old/" == a['href']:
                continue
            if "https://www.mzitu.com/190415" == a['href']:
                continue
            # print(a['href'])
            # break 
            # url_list.append(a['href'])
            self.url_list.append(a['href'])
            # print(url_list)
        """
        for url_str in url_list:
            self.img_info(url_str)
            break 
        """
    
    def img_info(self,url):
        html = self.getRequestContent(url)
        # print(html)
        soup = BeautifulSoup(html,'html.parser')
        main_image = soup.find('div',attrs={'class':'main-image'})
        fd_name = soup.find('h2').text   # 文件夹名
        # print(fd_name)
        
        if not os.path.exists(fd_name):
            os.mkdir(fd_name)

        # 获取总页数
        div = soup.find('div',attrs={'class':'pagenavi'})
        a_list = div.find_all('a')
        print(a_list[-2])
        total_page = int(a_list[-2].text)

        for i in range(1, total_page + 1):
            temp_url =  url + "/{}".format(i)
            print(temp_url,"OK")
            self.dl_img(temp_url,fd_name,i) 
            time.sleep(2)
        time.sleep(2)
        """
        img_src = main_image.find('img')['src']
        # print(img_src)
        # Referer: https://www.mzitu.com/190415
        self.header['Referer'] = url
        img = requests.get(img_src,headers = self.header)
        print(img.status_code)
        with open(jpg,'wb') as f:
            f.write(img.content)
        """

    def dl_img(self,url,fd_name,page):
        '''
        下载图片
        '''
        html = self.getRequestContent(url)
        # print(html)
        soup = BeautifulSoup(html,'html.parser')

        main_image = soup.find('div',attrs={'class':'main-image'})
        
        img_src = main_image.find('img')['src']

        self.header['Referer'] = url 
        img = requests.get(img_src,headers = self.header)
        print(img.status_code)
        with open(fd_name + "\\" + str(page) + '.jpg','wb') as f:
            f.write(img.content) 

if __name__=="__main__":
    gril = Gril()
    url = gril.baseUrl + "/all"
    gril.spider(url)

    pool = Pool(processes=2)
    pool.map(gril.img_info,gril.url_list)