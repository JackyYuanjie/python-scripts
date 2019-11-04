# -*- coding:utf-8 -*-

"""
说明:
写程序,有3个功能.
1. 获取键盘数据,并发送给对方.
2. 接收数据并解码.
3. 关闭程序.

聊天器功能
1. 发送信息
2.接收信息
3.退出系统

二.架构设计
1. 发送信息(send_msg())
2. 接收信息(recv_msg())
3. 程序主入口: main()
4. 当程序独立运行时,才启动聊天器.
实现步骤:
1.发送信息
- 定义变量接收用户与输入的接收方的IP地址
- 定义变量接收用户与输入的接收方的端口号
- 定义变量接收用户输入的接收方的内容
- 使用socket的sendto() 发送信息.

2.接收信息recv_msg()
- 使用socket,接收数据.
- 解码数据
- 输出显示

3.主入口main()
- 创建套接字
- 绑定端口
- 打印菜单.
- 接收用户输入的选项
- 判断用户选择,并且调用对应的函数.
"""

import socket

def send_msg(udpsocket):
    """发送信息的函数"""
    ipaddr = input("请输入接收方的IP地址:")
    
    # 
    if len(ipaddr) == 0:
        ipaddr = "18.18.23.108"
        print("当前接收方默认为:{}".format(ipaddr))
    portnum = input("请输入接收方的端口号:")
    if len(portnum) == 0:
        portnum = "8899"
        print("当前接收方端口为:{}".format(portnum))
        content = input("请输入要发送的内容:")
        udpsocket.sendto(content.encode(),(ipaddr,int(portnum)))

def recv_msg(udpsocket):
    """接收信息的函数"""
    recvdata,ip_port = udpsocket.recvfrom(1024)
    recvtxt = recvdata.decode()
    """
    recvdata = udpsocket.recvfrom(1024)
    recvda = recvdata[0].decode("utf-8")
    print(recvda)
    """
    print("接收到{m}的消息:{s}".format(m=str(ip_port),s=recvtxt))


def main():
    """程序主入口"""
    udpsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udpsocket.bind((" ",2300))
    while True:
        print("\n" + "*"*20)
        print("*"*10 + "1.发送信息" + "*"*10)
        print("*"*10 + "2.接收信息" + "*"*10)
        print("*"*10 + "3.退出系统" + "*"*10)
        print("*"*20)
        # 接收用户输入的选项:
        sel_num = int(input("请输入选项:"))
        # 判断用户选择,并且调用对应的函数.
        if sel_num == 1:
            print("您选择的是发送信息")
            send_msg(udpsocket)
        elif sel_num == 2:
            print("您选择的是接收信息")
            recv_msg(udpsocket)
        elif sel_num == 3:
            print("系统正在退出中...")
            print("系统退出完成.")
            break
    # 关闭套接字
    udpsocket.close()
    

if __name__=="__main__":
    # 程序独立运行时,才去启动聊天器.
    main()

