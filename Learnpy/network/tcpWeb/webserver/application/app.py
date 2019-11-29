# -*- coding:utf-8 -*-

# 第7.1个.
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

    # 定义变量保存资源路径
    # resource_path = os.path.join(os.getcwd() + "python-scripts\\DevOps\\network\\tcpWeb\\" + current_dir + "\\\\" + file_path
    # 9. 拼接响应报文.
    # 9.1 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 9.2 响应头
    response_header = "Server:Python3-vscodeIDE/2.1\r\n"
    # 9.3 响应空行
    response_blank = "\r\n"
    # 9.4 响应主体

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

    return response_data
