# -*- coding:utf-8 -*-
import sys 
import paramiko
import time 

# 脚本中运行时密码处理.
ip_address = "18.18.23.2"
username = "root"
password = "yibot8"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()
ssh_client.connect(hostname=ip_address,username=username,password=password)
print("Successful connected",ip_address)
ssh_client.invoke_shell()
remote_connected = ssh_client.exec_command('ls\n')
remote_connected = ssh_client.exec_command("cd /home ; mkdir yuan\n")
print(remote_connected)
ssh_client.close()
