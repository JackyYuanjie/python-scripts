# -*- coding:utf-8 -*-

# 第6个.
# 使用面向对象思想进行封装.
# 目标: 能够使用面向对象思想,对web服务器进行封装.
"""
1. 功能分析
  - 使用面向对象思想进行封装.
  - 通过对象方法start(),启动web服务器.
2. 实现思路
  - 创建HttpServer类.
  - 创建HttpServer类的构造方法,并在构造方法中对tcp_server_socket创建初始化.
  - 创建start()方法,用来web服务器启动。
"""


import socket
import os

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

        # 根据客户端浏览器请求的资源路径,返回请求资源. 
        # 1) 把请求协议解码,得到请求报文的字符串
        request_text = request_data.decode()
        # 2) 得到请求行
        #  - 查找,第一个\r\n出现的位置.
        loc = request_text.find("\r\n")
        #  - 截取字符串,从开头嫁娶到第一个\r\n出现的位置.
        request_line = request_text[:loc]
        print(request_line)    
        #  - 把请求行,按照空格拆分, 得到列表.
        request_line_list = request_line.split(" ")
        print(request_line_list)

        # 得到请求的资源路径
        file_path = request_line_list[1]
        # print(file_path)
        print("{a}正在请求:{b}".format(a=str(ip_port),b=file_path))

        # 设置默认首页
        # if file_path == "/":
            # file_path = "/index.html"

        # 9. 拼接响应报文.
        # 9.1 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 9.2 响应头
        response_header = "Server:Python3-vscodeIDE/2.1\r\n"
        # 9.3 响应空行
        response_blank = "\r\n"
        # 9.4 响应主体
        indexpath = "F:\\PythonProject\\python-scripts\\DevOps\\network\\tcpWeb\\static\\index.html"

        try:
            # 返回固定页面, 通过with读取文件.
            with open(indexpath,"rb") as file:
                # 把读取的文件内容返回给客户端.
                response_body = file.read()
        except Exception as e:
            # 重新修改响应行为404
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应的内容为错误.
            response_body = "Error! {}".format(str(e))
            # 把内容转换为字节码
            response_body = response_body.encode()

        response_data = (response_line + response_header + response_blank).encode() + response_body

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