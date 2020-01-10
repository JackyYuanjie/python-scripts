# -*- coding:utf-8 -*-
import subprocess

#1. 执行外部命令并获取输出
"""
使用subprocess,生成新的进程并获取返回码,执行外部命令和启用新的应用.
"""
# subprocess.call(["touch","externalcommand.txt"])
# subprocess.call(["ls"])
# print("externalcommand created")
# subprocess.call(["rm","externalcommand.txt"])
# subprocess.call(["ls"])
# print("externalcommand deleted")
print("="*20)

#2.使用子进程模块捕获输出
"""
传递PIPE作为标准输出stdout的参数来捕获输出.

子进程模块用于创建新的进程. 
连接输入/输出管道并获取返回码. 
subprocess.run()运行作为参数传入的命令.
returncode是子进程的返回状态.
在输出中,如果得到了返回码0,表示成功运行.
"""
res = subprocess.run(["ls","-l"],stdout=subprocess.PIPE,)
print("returncode:",res.returncode)
print('{} bytes in stdout:\n{}'.format(len(res.stdout),res.stdout.decode('utf-8')))
print("="*20)
