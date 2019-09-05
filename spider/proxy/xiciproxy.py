#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request as req 
import time 

class Xici():
    def __init__(self):
        self.baseUrl = 'https://www.xicidaili.com/nn/'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    def getRequestContent(self,url):

        try:
            req_str = req.Request(url,headers = self.header)
            response = req.urlopen(req_str,timeout = 10)
        except:
            print("获取页面请求失败")
        else:
            return response.read().decode('utf-8')

        
    def spyder(self,url):
        """
        获取页面内容
        """
        html = self.getRequestContent(url)
        print(html)



if __name__=="__main__":
    xici = Xici()
    xici.spyder(xici.baseUrl)
