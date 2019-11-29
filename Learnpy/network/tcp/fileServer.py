# -*- coding:utf-8 -*-

"""
1. 导入模块
2. 创建套接字
3. 绑定端口
4. 设置监听, 设置套接字由主动为被动.
5. 接受客户端连接
6. 接收客户端发送的文件名
7. 根据文件名读取文件内容
8. 把读取的内容发送给客户端(循环)
9. 关闭和客户端的连接.
10. 关闭套接字
"""

import socket


Filesocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Filesocket.bind(("18.18.23.108",8888))
Filesocket.listen()

while True:
    new_client_socket,ip_port = Filesocket.accept()
    print("欢迎新客户端:",ip_port)
    recvdata = new_client_socket.recv(1024)
    file_name = recvdata.decode()
    print(file_name)

    try:
        with open(file_name,"rb") as fil:
            while True:
                filedata = fil.read(1024)
                # 判断是否读取到了文件的末尾.
                if filedata:
                    new_client_socket.send(filedata)
                else:
                    break
    except Exception as e:
        print("文件:{}下载失败".format(file_name))
        break
    else:
        print("文件:{}下载成功.".format(file_name))
        break
        
new_client_socket.close()
Filesocket.close()