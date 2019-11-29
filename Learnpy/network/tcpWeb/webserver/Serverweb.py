# -*- coding:utf-8 -*-

# 第7个.
# 目标: 优化代码,分模块开发.
"""
1. 整体功能
   - 创建框架构建相关的文件夹.
   - 创建app模块文件.
   - 在app模块文件中创建application函数(用于处理请求)
   - 将request_handler函数的处理逻辑交给app模块的application函数完成.
   - app模块的application函数,返回响应报文.

"""

import socket
import os
from application import app

class WebServer(object):

    # 初始化方法
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        tcp_server_socket.bind(("18.18.23.254",8882))
        tcp_server_socket.listen()

        # 定义实例属性,保存套接字对象
        self.tcp_server_socket = tcp_server_socket        


    def start(self):
        """启动web服务器"""
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
        response_data = app.application(request_data,ip_port)

        # 10. 发送响应报文.
        new_client_socket.send(response_data)

        # 11. 关闭连接.
        new_client_socket.close()


def main():
    # 创建WebServer类的对象
    ws = WebServer()
    # 对象.start() 启动web服务器
    ws.start()


if __name__=="__main__":
    main()