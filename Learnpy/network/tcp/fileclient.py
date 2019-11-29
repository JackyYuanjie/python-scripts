# -*- coding:utf-8 -*-

"""
文件下载器
功能分析:
- 建立TCP连接
- 告诉服务器要下载的文件名
- 服务器接受下载文件请求.

实现步骤:
客户端:
1. 导入模块
2. 创建套接字
3. 建立和服务器的连接
4. 接收客户端键入的文件名
5. 发送文件名到服务器端。
6. 创建文件,准备保存.
6. 接收服务端发送的数据,保存文件到本地.
7. 关闭套接字.
"""

import socket

Filesocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Filesocket.connect(("18.18.23.108",8822))


filename = input("请输入要下载的文件名:"+ "\n\n")
Filesocket.send(filename.encode())
Filepath = "F:\\PythonProject\\python-scripts\\DevOps\\network\\tcp\\"

with open(Filepath + filename,"wb") as f:
    while True:
        filedata = Filesocket.recv(1024)
        # 判断数据是否发送完毕.
        if filedata:
            f.write(filedata)
        else:
            break

Filesocket.close()

