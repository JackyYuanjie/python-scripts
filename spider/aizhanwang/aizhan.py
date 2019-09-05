#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

res = requests.get('https://icp.aizhan.com/www.csdn.net/',headers=headers)
# print(res.text)

try:
    soup = BeautifulSoup(res.text,'lxml')
    div = soup.find('div',attrs = {'id':'icp-table'})
    # print(div)
    # print(soup.prettify())
    td_list = div.find_all('td')
    # print(td_list)
    # print(len(td_list))
    """
    for td in td_list:
        print(td)
        print('-'*30)

    for i in range(0,len(td_list),2):
        print(td_list[i].text)
        print(td_list[i + 1].text)
        print('--'*30)
    """
    for i in range(0,len(td_list),2):
        info = td_list[i].text + ":" + td_list[i + 1].text 
        print(info)
        print('-'*30)

except ConnectionError:
    print("网站链接失败")