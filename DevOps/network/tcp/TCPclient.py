# -*- coding:utf-8 -*-

import socket

# 创建套接字, TCP传输方式.
# socket.SOCK_STREAM     TCP传输方式.
tcpclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
tcpclient.connect(("18.18.23.108",8882))
# 发送数据
tcpclient.send("测试tcp网络连接是否正常".encode())
# 接收数据
recvdata = tcpclient.recv(1024)
rectxt = recvdata.decode("utf-8")
print(rectxt)
# 关闭连接
# 关闭套接字
tcpclient.close()

