# -*- coding: utf-8 -*-

# author: devops_yj@163.com

"""
使用shutil.copy()方法复制文件: shutil.copy(src,dst)
使用shutil.copystat()方法复制元数据信息: shutil.copystat(src,dst)

copy方法: 仅复制文件的内容，但不复制其他信息.
copystat方法:可复制与文件，文件权限和其他信息关联的元数据.
"""

import os,shutil

from os import path

import datetime

import time

from datetime import date,time,timedelta

"""
def main():

# 1. 获取当前目录中原始文件的路径
    # 检查first.txt文件是否存在
    if path.exists("./demo/first.txt"):
        # 文件存在时,将文件路径存储在src变量中,获取当前路径下的文件,
        src = path.realpath("./demo/first.txt")
    
    # 用split函数分离路径和文件名
    head,tail = path.split(src)
    print("path:" + head)
    print("filter:" + tail)


# 2. 使用Shutil模块创建现有文件的副本
    # 创建副本文件并添加后缀
    # dst = src + ".bak"
    # 调用copy方法
    # shutil.copy(src,dst)

# 3. 删除first.txt.bak文件并运行程序后,它将创建.txt文件的副本，但这次会包含文件权限，修改时间和元数据信息等所有信息
    # shutil.copystat(src,dst)


# 4. 获取有关上次修改的first.txt文件的信息

    # 获取上次修改该副本文件的日期,月份,年份和时间. path.getmtime获取文件修改时间的详细信息. time.ctime使用时间类c时间函数将其转换为可读时间.
    t = time.ctime(path.getmtime("./demo/first.txt.bak"))
    print(t)

    # 提供有关文件修改的信息,使用fromtimestamp函数并构建一个日期时间对象
    print(datetime.datetime.fromtimestamp(path.getmtime("./demo/first.txt.bak")))


if __name__=="__main__":
    main()

"""


'''
python使用rename方法重命名文件和目录
语法: os.rename(src,dst)

'''
import os
os.rename('./demo/first.txt','./demo/1-first.txt')





