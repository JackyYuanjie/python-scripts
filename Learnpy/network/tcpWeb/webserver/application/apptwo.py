# -*- coding:utf-8 -*-

from application import utils

import os

def parse_request(request_data,ip_port):
    """解析请求的报文,返回客户端请求的资源路径"""
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
    # print(request_line_list)

    # 得到请求的资源路径
    file_path = request_line_list[1]
    # print(file_path)
    print("{a}正在请求:{b}".format(a=str(ip_port),b=file_path))

    # 设置默认首页
    if file_path == "/":
        file_path = "/index.html"
    
    return file_path


# def application(current_dir,request_data,ip_port):
def application(request_data,ip_port):

    # 调用parse_request函数,解析请求协议,返回请求的资源路径.
    file_path = parse_request(request_data,ip_port)
    indexpath = "F:\\PythonProject\\python-scripts\\DevOps\\network\\tcpWeb\\static\\index.html"

    # resource_path = os.path.join(os.getcwd() + "python-scripts\\DevOps\\network\\tcpWeb\\" + current_dir + "\\\\" + file_path

    try:
        # 返回固定页面, 通过with读取文件.
        with open(indexpath,"rb") as file:
            # 把读取的文件内容返回给客户端.
            response_body = file.read()

        # 调用utils模块的create_http_response 函数,拼接响应协议
        response_data = utils.create_http_response("200 ok",response_body)

    except Exception as e:
        # 重新修改响应行为404
        response_line = "HTTP/1.1 404 Not Found\r\n"
        # 响应的内容为错误.
        response_body = "Error! {}".format(str(e))
        # 把内容转换为字节码
        response_body = response_body.encode()

        # 
        response_data = utils.create_http_response("404 Not Found",response_body)
        

    return response_data
