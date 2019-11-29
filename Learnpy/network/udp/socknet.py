# -*- coding:utf-8 -*-

# 一: UDP网络程序--发送数据
"""
1. 使用socket的sendto方法发送数据
2. 使用encode()方法对发送的数据进行编码
"""
# 创建UDP socket
"""
1. 创建套接字,使用IPV4, UDP方式
2. 数据传递
3. 关闭套接字
"""

import socket
"""
# 协议类型: AF_INET(IPv4). 使用UDP传输方式(无连接):socket.SOCK_DGRAM
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  数据传递: 发送数据的二进制格式:, 对方IP和端口号.
# 将数据转换为二进制格式:字符串.encode()
# 对方IP和端口号为一个元组. 字符串类型为IP地址, 整数类型的端口号.
udpSocket.sendto("测试".encode(),("18.18.23.2",8888))
udpSocket.close()
"""


# 二: udp网络程序--发送--接收数据
"""
1. 使用socket的recvfrom方法接收数据
2. 使用decode()方法对接收到的数据进行解码.
"""
# udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 发送数据:
# udpSocket.sendto("测试".encode(),("18.18.23.2",8888))
"""
接收数据(二进制)
recvfrom(1024)方法的作用:
1.从套接字中接收1024个字节的数据.
2.此方法造成程序阻塞,等待另外一台计算机发送数据.
3.如果对方发送数据了,recvfrom方法会自动解除阻塞.
4.如果对方没有发送数据,程序会一致等待.
"""
# recvdata = udpSocket.recvfrom(1024)
# print(recvdata)



# windows主机: 
# cat socketsend.py 
# -*- coding:utf-8 -*-
# udp端口绑定(发送端)
import socket
# 创建套接字
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定发送端自己的ip和端口号
# udpSocket.bind(("18.18.23.254",2500))
udpSocket.bind(("",2500))
# 将数据转换成二进制格式
udpSocket.sendto("我发送了很多的数据".encode(),("18.18.23.108",8888))
# 关闭套接字
udpSocket.close()


"""
# linux主机:
# cat socketreceive.py 
# -*- coding:utf-8 -*-
# udp端口绑定(接收端)
import socket 
# 创建套接字
udpsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定的是接收端自己的ip和端口
udpsocket.bind(("18.18.23.108",8888))
# 接收发送方发送的数据,1024为接收缓冲区大小(每次接收多少个字节)
recv = udpsocket.recvfrom(1024)
# 数据解码
recvtxt = recv[0].decode("utf-8")
# 打印数据
print(recvtxt) 
# 关闭套接字
udpsocket.close()
# linux返回的结果为: "我发送了很多的数据"
"""
