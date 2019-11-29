# -*- coding:utf-8 -*-

"""
目标:能够使用多线程实现同时接收多个客户端的多条信息

1.TCP服务器端
(1) 实现指定端口监听
(2) 实现服务器端地址重用,避免"Address in use"错误。
(3) 能够支持多个客户端连接.
(4) 能够支持支持不同的客户端同时收发消息(开启子线程)
(5) 服务器端主动关闭服务器,子线程随之结束.
"""

# 1. 该程序可以支持多客户端连接.
# 2. 该程序可以支持多客户端同时发送消息.

# 1. 导入模块
import socket
import threading

def recv_msg(new_client_socket,ip_port):

    # 循环接收tcp 客户端的消息.
    while True:
        # 7. 接收客户端发送的信息。
        recv_data = new_client_socket.recv(1024)
        if recv_data:
            # 8. 解码数据并且进行输出.
            recv_text = recv_data.decode()
            print("收到来自{i}的信息:{m}".format(i = str(ip_port),m = recv_text))
        else:
            break

    # 9. 关闭和当前客户端的连接.
    new_client_socket.close()

# 2. 创建套接字
tcp_serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 3. 设置地址可以重用
tcp_serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

# 4. 绑定端口。
tcp_serversocket.bind(("",8888))

# 5. 设置监听,套接字由主动设置为被动.
tcp_serversocket.listen(128)


while True:
    # 6. 接受客户端连接.
    new_client_socket,ip_port = tcp_serversocket.accept()
    print("新客户端连接:",ip_port)
    
    # 创建线程
    thre_recvmsg = threading.Thread(target=recv_msg,args=(new_client_socket,ip_port))
    # 设置线程守护
    thre_recvmsg.setDaemon(True)
    # 启动线程
    thre_recvmsg.start()




tcp_serversocket.close()
