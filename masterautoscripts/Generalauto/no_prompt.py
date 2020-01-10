# -*- coding:utf-8 -*-
import getpass

# 1. 在运行时和验证时弹出密码输入
"""
getpass()模块弹出让用户输入密码并不进行打印.
getpass模块用于终端中程序需要处理密码弹出的用户交互.
"""
"""
try:
    p = getpass.getpass("Enter your password:")
except Exception as error:
    print('ERROR',error)
else:
    print('Password entered:',p)
"""


passwd = getpass.getpass(prompt='Enter your password:')
if passwd == 'xxx':
    print("input password successful")
else:
    print('input password is incorrect!!')
