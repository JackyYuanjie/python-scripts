# -*- coding:utf-8 -*-

# 第一个.
"""
1. 导入模块
2. 创建套接字
3. 建立连接
4. 拼接请求协议
5. 发送请求协议
6. 接收服务器响应内容
7. 保存内容
8. 关闭连接.
"""


import socket

filepath = "F:\\PythonProject\\python-scripts\\DevOps\\network\\tcp\\"

browsersocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 3. 建立连接
browsersocket.connect(("www.icoderi.com",80))

# 4. 拼接请求协议
# 4.1 请求行
request_line = "GET / HTTP/1.1\r\n"
# 4.2 请求头
request_header = "Host:www.icoderi.com\r\n"
# 4.3 请求空行
request_black = "\r\n"
request_data = request_line + request_header + request_black

# 5. 发送请求协议
browsersocket.send(request_data.encode())

# 6. 接收服务器响应内容
recvdata = browsersocket.recv(4096)  #4096字节.
recvtxt = recvdata.decode()
# print(recvtxt)
# 7. 保存内容
# 7.1 查询\r\n\r\n的位置.
loc = recvtxt.find("\r\n\r\n")
# 7.2 截取字符串
htmldata = recvtxt[loc+4:]
print(htmldata)

with open(filepath + "index.html","w",encoding="utf-8") as file:
    file.write(htmldata)

# 8. 关闭连接.
browsersocket.close()