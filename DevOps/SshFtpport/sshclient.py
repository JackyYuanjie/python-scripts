#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
#ssh密码认证远程执行命令:
import os,sys
import paramiko

hostname='18.18.23.102'
port = 22
username = 'yuan'
password = '123.cn'

client = paramiko.SSHClient()  #绑定实例
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname,port,username,password,timeout=10)
stdin,stdout,stderr = client.exec_command('ls')  #执行bash命令
result = stdout.read()
error = stderr.read()
#
# #判断stderr输出是否为空，为空则打印执行结果，不为空打印报错信息。
if not error:
    print(result)
else:
    print(error)
client.close()
#
"""

#通过transport方式登陆:
import paramiko,sys

hostname='18.18.23.102'
port = 22
username = 'yuan'
password = '123.cn'
command=sys.argv[1]

#实例化一个transport对象
transport = paramiko.Transport((hostname,port))

#建立连接
transport.connect(username=username,password=password)

#建立ssh对象
ssh = paramiko.SSHClient()

#绑定transport到ssh对象
ssh._transport = transport

#执行命令
stdin,stdout,stderr=ssh.exec_command(command)

#打印输出
print(stdout.read().decode())

#关闭连接
transport.close()





"""
#实现类似xshell工具的功能，登陆以后输入命令回车后返回结果
import paramiko,os,select,sys

hostname='18.18.23.102'
port = 22
username = 'yuan'
password = '123.cn'

#建立一个socket
trans = paramiko.Transport((hostname,port))

#启动一个客户端
trans.start_client()

#使用用户名和密码登陆:
trans.auth_password(username=username,password=password)

#打开一个通道
channel = trans.open_session()

#获取终端:
channel.get_pty()

#激活终端，登陆到终端，
channel.invoke_shell()
 # 用select实现你的执行操作，
 #    对输入终端sys.stdin和通道进行监控，
 #    用户在终端输入命令，将命令交给channel通道，sys.stdin发生变化。
 #    select感知。
 #    channel的发送命令，获取结果过程就是一个socket的发送和接受信息的过程。


while True:
    readlist,writelist,errlist = select.select([channel,sys.stdin,],[],[])
    #用户输入命令后，sys.stdin发生变化。
    if sys.stdin in readlist:
        #获取输入内容
        input_cmd = sys.stdin.read(1)
        #将命令发送给服务器
        channel.sendall(input_cmd)


    #服务器返回结果，channel通道接受到结果，发生变化，select感知到。
    if channel in readlist:
        #获取结果
        result = channel.recv(1024)
        #断开连接后退出:
        if len(result) == 0:
            print("\r\n***EOF***\r\n")
            break
        #输出到屏幕
        sys.stdout.write(result.decode())
        sys.stdout.flush()

#关闭通道
channel.close()
#关闭连接
trans.close()
"""
