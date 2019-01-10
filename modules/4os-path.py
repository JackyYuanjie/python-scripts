# -*- coding:utf-8 -*-

'''
检查文件或目录是否存在
'''
"""
# 检查文件或目录是否存在
import os.path
from os import path

def main():
    # 使用path.exists()函数来检查文件是否存在
    print("directory exists:"+str(path.exists("./demo")))  # 返回True,表示该目录存在.
    print("file exists:" + str(path.exists('./demo/first.txt')))  # 返回True,表示文件存在.
    print("TWO file exists:" + str(path.exists('two.txt')))  # 返回False,表示文件不存在.
    
if __name__=="__main__":
    main()



# 判断是否是文件? 用path.isfile函数
print("Is it File: " + str(path.isfile('./demo/first.txt')))  #是文件,返回True.
print("Is it File:" + str(path.isfile('./demo')))  # 不是文件,返回False.


# 判断是否是目录? 用path.dir函数.

print("Is it Directory:" + str(path.isdir('./demo/first.txt'))) # 返回False,不是目录.

print("Is it Directory:" + str(path.isdir('./demo')))
# 返回True,是目录.
"""


"""
使用shutil.copy()方法复制文件: shutil.copy(src,dst)
使用shutil.copystat()方法复制元数据信息: shutil.copystat(src,dst)

"""

# 1. 声明变量
# 2. 在变量中使用split函数
import os,shutil
from os import path

def main():

# 1. 获取文件路径和文件名
    # 检查first.txt 文件是否存在
    if path.exists("./demo/first.txt"):
    # 如果文件存在,获取当前文件的路径,并赋值到src变量中.
        src = path.realpath("./demo/first.txt")
    
    # 获得文件路径后,采用split函数分离路径和文件名.
    head,tail = path.split(src)
    print("path:" + head)
    print("filter:" + tail)

# 2. 用Shutil模块创建现有文件的副本
    dst = src + ".bak"  # 添加后缀名称.bak,dst存的是文件副本.
    # 使用copy方法复制文件.
    shutil.copy(src,dst)

# 复制功能仅能复制文件内容.

# 3. 获取文件属性信息,运行程序后，它将创建.txt文件的副本，但这次会包含文件权限，修改时间和元数据信息等所有信息.
    # dst = src + "-bak"
    # shutil.copystat(src,dst)


if __name__=="__main__":
    main()














