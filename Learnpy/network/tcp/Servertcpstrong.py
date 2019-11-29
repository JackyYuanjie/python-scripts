# -*- coding:utf-8 -*-

import socket

# 创建套接字, TCP传输方式.
tcpserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定端口和IP。
tcpserver.bind(("",8882))
# 开启监听(设置套接字为被动模式)
# 设置tcpserver套接字为被动监听模式,不能再主动发送数据.
# 在windows系统 128 有效. 在linux上无效.
tcpserver.listen(128)
"""
等待客户端连接.accept 开始接受客户端连接,程序会默认进入阻塞状态(等待客户端连接),如果由客户端连接后,程序会自动解除阻塞.
recvdata数据会有两部分:
1) 返回了一个新的套接字socket
2) 客户端的IP地址和端口号.
"""
# recvdata = tcpserver.accept()
# print(recvdata)

while True:
    newClientsocket ,client_ipport = tcpserver.accept()
    print("新客户端来了:{}".format(str(client_ipport)))
    # 收发数据
    while True:
        # recv() 会让程序再次阻塞, 收到信息后再次阻塞.
        recvdata = newClientsocket.recv(1024)
        # 当接收到数据为"空"的时候,表示客户端已经断开连接了,服务端也要断开.
        if len(recvdata) != 0:
            recv_text = recvdata.decode("utf-8")
            print("接收到{C}信息:{M}".format(C=str(client_ipport),M=recv_text))
        else:
            print("客户端已经断开连接.")
            break


    # 表示不能再和当前的客户端通信了.
    newClientsocket.close()

# 关闭连接,表示程序不再接受新的客户端连接,已经连接的可以继续服务.
tcpserver.close()
