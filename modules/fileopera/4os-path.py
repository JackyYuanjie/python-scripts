# -*- coding:utf-8 -*-

# author: devops_yj@163.com

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




