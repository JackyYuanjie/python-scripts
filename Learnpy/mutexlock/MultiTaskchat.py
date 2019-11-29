# -*- coding:utf-8 -*-

# 多任务版udp聊天器(一)
"""
说明:
1. 编写一个有2个线程的程序
2. 线程1用来接收数据然后显示.
3. 线程2用来检测键盘数据然后通过udp发送数据.
要求:
- 总结多任务程序的特点.

改进思路:
1. 单独开子线程用于接收消息,以达到收发消息可以同时进行.
2. 接收消息要能够连续接收多次,而不是一次.
3. 设置子线程守护主线程(解决无法正常退出问题)
"""

# 开辟子线程,实现发送消息的同时接收消息.


import socket
import time 
import threading

def send_msg(udpsocket):
    """发送信息的函数"""
    ipaddr = input("请输入接收方的IP地址:")
    portnum = input("请输入接收方的端口号:")
    content = input("请输入要发送的内容:")
    udpsocket.sendto(content.encode(),(ipaddr,int(portnum)))


def recv_msg(udpsocket):
    """接收信息的函数"""
    # while True:
    recvdata,ip_port = udpsocket.recvfrom(1024)
    recvtxt = recvdata.decode()
    print("接收到{m}的消息:{s}".format(m=str(ip_port),s=recvtxt))

    """
    recvdata = udpsocket.recvfrom(1024)
    recvda = recvdata[0].decode("utf-8")
    print(recvda)
    """
        # print("接收到{m}的消息:{s}".format(m=str(ip_port),s=recvtxt))


def main():
    """程序主入口"""
    udpsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udpsocket.bind(("18.18.23.254",2500))

    # 创建子线程,单独接收用户发送的消息
    thread_recvmsg = threading.Thread(target=recv_msg,args=(udpsocket,))
    # 设置子线程守护主线程
    thread_recvmsg.setDaemon(True)
    # 启动子线程.
    thread_recvmsg.start()

    while True:
        print("\n" + "*"*20)
        print("*"*10 + "1.发送信息" + "*"*10)
        print("*"*10 + "2.退出系统" + "*"*10)
        print("*"*20)
        # 接收用户输入的选项:
        sel_num = int(input("请输入选项:"))
        # 判断用户选择,并且调用对应的函数.
        if sel_num == 1:
            print("您选择的是发送信息")
            send_msg(udpsocket)
        elif sel_num == 2:
            print("系统正在退出中...")
            print("系统退出完成.")
            break
    # 关闭套接字
    udpsocket.close()
    

if __name__=="__main__":
    # 程序独立运行时,才去启动聊天器.
    main()
