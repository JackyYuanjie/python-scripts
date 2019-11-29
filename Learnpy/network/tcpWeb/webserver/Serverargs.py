# -*- coding:utf-8 -*-

# 目标: 通过终端,指定端口启动web服务器
"""
1.功能分析:
- 在终端中启动web服务器.
2.实现思路
 1. 导入sys模块.
 2. 通过sys.argv获取参数列表.
 3. 判断列表长度是否为2, 如果不等于2,要给出提示: web服务器启动失败.
 4. 取出第二个参数,判断是
"""

import socket
import os
from application import apptwo
import sys

class WebServer(object):

    # 初始化方法
    def __init__(self,ip,port):
        tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        tcp_server_socket.bind((ip,port))
        tcp_server_socket.listen()

        # 定义实例属性,保存套接字对象
        self.tcp_server_socket = tcp_server_socket        


    def start(self):
        """启动web服务器"""
        print("web服务器启动成功,等待客户端连接---")
        while True:
            new_client_socket,ip_port = self.tcp_server_socket.accept()
            print("新客户端来了:",ip_port)
            # 调用功能函数
            self.request_handler(new_client_socket,ip_port)


    def request_handler(self,new_client_socket,ip_port):
        request_data = new_client_socket.recv(1024)
        if not request_data:
            print("{}客户端已经下线.".format(str(ip_port)))
            new_client_socket.close()
            return 


        # 使用application文件夹app模块的application()函数处理.
        # response_data = app.application("static",request_data,ip_port)
        response_data = apptwo.application(request_data,ip_port)

        # 10. 发送响应报文.
        new_client_socket.send(response_data)

        # 11. 关闭连接.
        new_client_socket.close()


def main():
    """
    1. 导入sys模块
    2. 获取系统传递到程序的参数.
    3. 判断参数格式是否正确.
    4. 判断端口号是否是一个数字.
    5.获取端口号.
    6.在启动web服务器时,使用指定的端口
    """
    # 2. 获取系统传递到程序的参数.
    params_list = sys.argv
    # 3. 判断参数格式是否正确.
    if len(sys.argv) != 3:
        print("启动失败,参数格式错误,正确格式:python3 Serverargs.py IP地址 端口号")
        return 

    # 判断IP:
    if not sys.argv[1]:
        print("请输入IP地址")
    ip = str(sys.argv[1])
    # 判断端口
    if not sys.argv[2].isdigit():
        print("启动失败,端口号不是一个纯数字")
        return 
    
    # 获取端口号
    port = int(sys.argv[2])

    

    # 创建WebServer类的对象
    ws = WebServer(ip,port)
    # 对象.start() 启动web服务器
    ws.start()


if __name__=="__main__":
    main()
