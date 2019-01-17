# -*- coding: utf-8 -*-

# author: firstoney
#author: devops_yj@163.com

"""
python有压缩软件的模块,
压缩整个目录的方法: shutil.make_archive(output_filename, 'zip', dir_name)
使用以下命令可以控制要归档的文件: ZipFile.write(filename)
"""

# 1. 创建归档文件,导入模块

import shutil,os

from os import path

from zipfile import ZipFile

from shutil import make_archive

'''
1. 从模块shutil导入make_archive类
2. 使用split函数将目录和文件名从路径分割到文本文件的位置
3. 调用shutil.make_archive方法创建归档文件.
4. 传入你想要压缩的文件的根目录
5. 已经创建好归档文件.
'''

"""
def main():
    if path.exists("./demo/first.txt.bak"):
        src = path.realpath("./demo/first.txt.bak")
        print(src)
    # root_dir,tail = path.split(src)

    # 压缩整个目录,请使用下面的命令:
    # shutil.make_archive("first","zip",root_dir)




# 可以定义要归档的特定文件.
with ZipFile("testfirst.zip","w") as newzip:
    newzip.write("./demo/1-first.txt")
    newzip.write("./demo/first.txt.bak")
'''
1. 从zipfile模块导入Zipfile类。 该模块控制创建zip文件
2. 创建一个名为testfirst.zip的压缩文件.
3. 创建一个新的Zipfile类，需要传入权限，因为它是一个文件，所以你需要将信息作为newzip写入文件
4. 使用变量“newzip”来引用我们创建的zip文件
5. 使用write函数,将两个文件添加到归档文件中.

使用“With”范围锁，所以当程序超出此范围时，文件将被清理并自动关闭。
'''

if __name__=="__main__":
    main()
"""

"""
总结:
1. 压缩整个目录,请使用下面的命令:
   shutil.make_archive("name","zip",root_dir)
2. 要选择要压缩的文件，请使用命令"ZipFile.write(filename)"
"""


"""
urllib是一个可用于打开URL的Python模块。 它定义了有助于URL操作的函数和类。
可以访问和检索来自Internet的数据，如XML，HTML，JSON等。可以直接处理此数据.
"""

# 使用urllib打开URL网址

# 导入urllib库:
import urllib.request

# 声明变量,调用urllib库上的urlopen函数
url = urllib.request.urlopen("http://www.baidu.com")

# 获取返回结果并打印: 打印返回状态吗(200,301,404,502)
print("result code:" + str(url.getcode()))


# 如何从URL中获取HTML文件
# 使用read函数读取HTML文件,并将结果输出在控制台:
data = url.read().decode('utf-8')
print(data)


