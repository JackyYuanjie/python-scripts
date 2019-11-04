# -*- coding:utf-8 -*-

import socket

# 创建套接字, IPv4和udp
udpsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpsocket.bind(("",2500))
# 设置广播权限(套接字默认不允许发送广播,需要开启权限)
# udpsocket.setsockopt(套接字,属性,属性值)
udpsocket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,True)
# 发送数据
udpsocket.sendto("测试广播地址".encode(),("18.18.23.255",8888))
# 关闭套接字
udpsocket.close()