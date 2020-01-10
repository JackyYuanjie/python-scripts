# -*- coding:utf-8 -*-
import paramiko
import threading
import time 


def ssh_multi(ip,port,username,passwd,cmd):

    """
    1.利用多线程,同时发出登录请求,同时去连接电脑,速度很快. 因为有一些命令执行时间会长一些.
    2. 循环时循环所有ip.
    3. 远程执行命令有交互,用stdin.write('Y')来完成交互.
    4. 把需要执行的命令存放到一个列表.
    5. exec_command为单个会话,执行完成后会回到登录时的默认目录.
    """

    try:
        # 记录paramiko连接时的日志信息
        # paramiko.util.log_to_file('paramiko.log')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,username,passwd,timeout=10)
        for m in cmd:
            stdin,stdout,stderr = ssh.exec_command(m)
            stdin.write("Y") # Simple interaction
            out = stdout.readlines()

            # Screen output
            for o in out:
                print(o)
        print("{}\t login Linux system successful.".format(ip))
        ssh.close()
    except:
        print("{} \t login failed.".format(ip))

def main():
    cmd = ['cal','ls','ifconfig ens37','ifconfig ens38']  # List of executed commands
    username = "yuan"  # username
    passwd = "123.cn"
    threads = []  # multithreads
    print("Begin multi thread...")
    for i in range(1,130):
        ip = '18.18.23.' + str(i)
        port = 22
        a = threading.Thread(target=ssh_multi,args=(ip,port,username,passwd,cmd))
        a.start()

if __name__=="__main__":
    main()