# -*- coding:utf-8 -*-

import urllib.request as req 
from bs4 import BeautifulSoup
import requests
import os 
import time 
from multiprocessing import Pool

# Resume = "F:\PythonProject\Otherdata\resume"

class PPT():
    '''
    整个爬虫的类
    '''
    def __init__(self):
        self.baseUrl = "http://www.ypppt.com/moban/"
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}
        # self.page_count = 

    def getResponseContent(self,url):
        '''
        获取页面请求信息
        '''
        try:
            req_str = req.Request(url,headers = self.header)
            response = req.urlopen(req_str,timeout = 10)
        except:
            print("请求失败")
        else:
            return response.read().decode('utf-8')

    def spyder(self,url):
        '''
        解析第一个页面
        '''
        html = self.getResponseContent(url)
        # print(html)

        soup = BeautifulSoup(html,'html.parser')
        divs = soup.find_all('div',attrs={'class':'wrapper'})

        div = divs[1] # 目标div

        page_info = div.find('div',attrs={'class':'page-navi'})
        print(page_info)
        a_list = page_info.find_all('a')
        last_a = a_list[len(a_list) - 1]
        print(last_a)

        href = last_a['href']
        page_count = href.replace('list-','').replace('.html','')
        print(page_count)



        """
        for div in divs:
            print(div)
            print('-'*30)
        """

        # """
        ul = div.find_all('ul')[3]

        li_list = ul.find_all('li')
        ppt_link_list = []
        for li in li_list:
            aTag_href = li.find_all('a')[1]['href']
            ppt_link = "http://www.ypppt.com" + aTag_href
            # print(ppt_link)
            # self.PPT_info(ppt_link)
            # break
            time.sleep(2)  
            ppt_link_list.append(ppt_link)

        pool = Pool(processes= 4)
        pool.map(self.PPT_info,ppt_link_list)
        # """

        for page in range(2,int(page_count) + 1):
            print(page)
            print("-"*20)



    def PPT_info(self,url):
        '''
        ppt下载页面
        '''
        html = self.getResponseContent(url)
        soup = BeautifulSoup(html,'html.parser')
        down_button = soup.find('a',attrs={'class':'down-button'})['href']
        down_url = "http://www.ypppt.com" + down_button
        self.DL_PPT(down_url)

    def DL_PPT(self,url):
        '''
        下载ppt页面
        '''
        html = self.getResponseContent(url)
        soup = BeautifulSoup(html,'html.parser')
        ul = soup.find('ul',attrs={'class':'down clear'})
        rar_link = ul.find_all('a')[0]['href']

        if rar_link.find('.com') > 0:
            pass
        else: 
            rar_link = 'http://www.ypppt.com' + rar_link
        # print(rar_link)
        ppt_name = soup.find('h1').text 
        if ppt_name.find('-') > 0:
            ppt_name = ppt_name.split('-')[0].strip()
        # print(ppt_name)
        f = requests.get(rar_link,headers = self.header)
        '''
        with open('a.rar','wb') as rar:
            rar.write(f.content)
        '''
        with open(ppt_name + '.rar','wb') as rar:
            rar.write(f.content)

        print(ppt_name, "下载完成...")    


if __name__=="__main__":
    ppt = PPT()
    start_time = time.time()

    ppt.spyder(ppt.baseUrl)
