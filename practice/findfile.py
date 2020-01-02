# -*- coding:utf-8 -*-

import glob

# 获取指定目录下的内容
# yijian = glob.glob(r"F:\*\*\*.docx")
# print(yijian)

"""
   在python中，glob模块是用来查找匹配的文件的
    在查找的条件中，需要用到Unix shell中的匹配规则：

       *    :   匹配所有
       ?    :   匹配一个字符
       *.*  :   匹配如：[hello.txt,cat.xls,xxx234s.doc]
       ?.*  :   匹配如：[1.txt,h.py]
       ?.gif:   匹配如：[x.gif,2.gif]

    如果没有匹配的，glob.glob(path)将返回一个空的list:[]
"""

def get_all():
    """ 获取目录下面所有的文件 """
    return glob.glob(r"F:\PythonProject\*.*")

def get_myfile():
    """获取文件名为6个字符的文件"""
    return glob.glob(r"F:\PythonProject\??????.txt")

def getsubfile():
    """获取子目录下的文件"""
    return glob.glob(r"F:\PythonProject\*\*\**.txt")

def main():
    print("获取F盘PythonProject目录下面所有的文件:")
    Pyfile = get_all()
    print(Pyfile)
    print("\n")
    print("获取F盘PythonProject目录下面文件名为6个字符的文件:")
    myfile = get_myfile()
    print(myfile)

    getfiles = getsubfile()
    print(getfiles)

if __name__=="__main__":
    main()