#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import requests
from bs4 import BeautifulSoup


"""
https://wenku.baidu.com/browse/getrequest?doc_id=a1eec6289b6648d7c1c7468f&pn=22&rn=1&type=ppt&callback=bd__cbs__s5lw72
https://wenku.baidu.com/browse/getrequest?doc_id=a1eec6289b6648d7c1c7468f&pn=23&rn=1&type=ppt&callback=bd__cbs__coo5j5
https://wenku.baidu.com/browse/getrequest?doc_id=a1eec6289b6648d7c1c7468f&pn=21&rn=1&type=ppt&callback=bd__cbs__2hc9ds
https://wenku.baidu.com/browse/getrequest?doc_id=a1eec6289b6648d7c1c7468f&pn=5&rn=1&type=ppt&callback=bd__cbs__nh2gao
"""
linkfiles = "F:\\PythonProject\\python-scripts\\spider\\wenkubaidu\\odnimages\\"

class WK():
    '''
    百度文库
    '''
    def __init__(self):
        self.baseUrl = "https://wenku.baidu.com/view/564fc70a77a20029bd64783e0912a21615797ff7.html"
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    def getResponse(self,url):
        try:
            req = urllib.request.Request(url,headers = self.header)
            response = urllib.request.urlopen(req,timeout = 10)

        except:
            print("页面请求失败")
        else:
            return response.read().decode('gb2312')

    def spyder(self,url):
        html = self.getResponse(url)
        # print(html)

        start_index = html.find("https:")
        # print(start_index)
        print('-'*30)
        end_index = html.find('","')
        # print(end_index)
        print(html[start_index:end_index])      

        """
        with open(linkfiles + "wenkucontent.txt",'a+') as fa:
            fa.write(html)
            fa.write("\n")
        """

        header = self.header 
        header['Cookie'] = 'BAIDUID=2CC737B4D3E3D51EA7529F8065A8B708:FG=1; PSTM=1553749648; BIDUPSID=36D49C7DE8F84F920A6D6ADE0E719043; _click_param_pc_rec_doc_2017_testid=4; ZD_ENTRY=bing; cflag=13%3A3; session_name=cn.bing.com; isJiaoyuVip=1; wk_shifen_pop_window=7765_1_1567070315751; Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1566318226,1566571568,1567070267,1567070708; session_id=1567070708094; BCLID=11327784929476180808; BDSFRCVID=aD0OJeC624LjSNrwjvtqhFVMiLK2tRQTH6055tzl7cu_UIsP_XwLEG0PDM8g0Ku-5SOpogKK0mOTHv-F_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=JJ-qVCPbtDvbfP0kb-r_bPk0hNLHJK62aKDs3l-MBhcqEIL4jMv80UCX5U6q-no33HcuBlRcttbCVfbSj60hjJ0hhaJ2-lRPW67TMMn5Bp5nhMJeXj7JDMP0qHogWbOy523ion6vQpn-KqQ3DRoWXPIqbN7P-p5Z5mAqKl0MLIOkbRO4-TFaejOQDfK; userFirstTime=true; ___wk_scode_token=XdTTTDexiuWKJhoY9dcpx3hQOGs%2Bniyz9YrLayUnQsQ%3D; Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1567072063'
        # print(header)
        urlrep = html[start_index:end_index].replace('\\','')
        # print(urlrep)
        # req = requests.get('https://wkretype.bdimg.com//retype//zoom//6a30bde2f8c75fbfc77db23c?pn=4&raww=1080&rawh=810&o=jpg_6&md5sum=f9ace759cd13bfd0f9ad186d77af05fa&sign=0756077547&png=41164-280359&jpg=227559-365825')
        req = requests.get(urlrep,headers = header)        
        """
        with open(linkfiles + "b.png",'wb') as fb:
            fb.write(req.content)
        """

        p_index = html.find('"page":')
        p_end = html.find('}]')
        pag = html[p_index+7:p_end]

        with open(linkfiles + pag + ".png",'wb') as fb:
            fb.write(req.content)

if __name__=="__main__":
    wk = WK()
    for pn in range(1,26):
        url = 'https://wenku.baidu.com/browse/getrequest?doc_id=a1eec6289b6648d7c1c7468f&pn={}&rn=1&type=ppt&callback=bd__cbs__nh2gao'.format(pn)
        print(url,"下载完成")
        wk.spyder(url)
        

        """
        with open(linkfiles + "wenkulink.txt",'a+') as fw:
            # fw.write(url)   # 是统计的页数连接,可以从中获取到图片的链接 
            # fw.write("\n")
        """
    # wk.spyder(wk.baseUrl)



"""
注意该网址粘贴到浏览器上访问是可以的,但是在代码中若不替换\该字符,会导致报错.
https:\/\/wkretype.bdimg.com\/retype\/zoom\/6a30bde2f8c75fbfc77db23c?pn=4&raww=1080&rawh=810&o=jpg_6&md5sum=f9ace759cd13bfd0f9ad186d77af05fa&sign=0756077547&png=41164-280359&jpg=227559-365825
"""