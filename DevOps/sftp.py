#!/usr/bin/env python
# -*- coding:utf-8 -*-

import paramiko

#sftp文件传输

#实例化transport对象，并建立连接。
# transport = paramiko.Transport(('18.18.23.102',22))
# transport.connect(username='yuan',password='123.cn')

#实例sftp对象，指定连接对象
# sftp = paramiko.SFTPClient.from_transport(transport)

#上传文件
# sftp.put(localpath='K:\\online.log',remotepath='/home/yuan/online.log')
# sftp.put(localpath='splitonline.py',remotepath='/home/yuan/splitonline.py')

#下载文件
#sftp.get(remotepath='/home/yuan/paramiko.txt',localpath='paramiko.txt')

#关闭连接
# transport.close()


import paramiko,sys,os
hostname = '18.18.23.102'
port = 22
username='yuan'
password='123.cn'
local_path=sys.argv[1]
remote_path=sys.argv[2]

if not os.path.isfile(local_path):
    print(local_path + "file not exists!")
    sys.exit(1)
try:
    s = paramiko.Transport((hostname,port))
    s.connect(username = username,password=password)
except Exception as e:
    print(e)

sftp = paramiko.SFTPClient.from_transport(s)
#使用put()方法将本地文件上传到远程服务器
sftp.put(local_path,remote_path)

#使用get方法下载文件
# sftp.get(remotepath=,localpath=)
#测试是否上传成功。
try:
    #远程主机有这个文件则返回一个对象，否则抛出异常
    sftp.file(remote_path)
    print("上传成功")
except IOError:
    print("上传失败")
finally:
    s.close()

