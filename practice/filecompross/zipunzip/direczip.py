# -*- coding:utf-8 -*-

import zipfile
import os 
import sys 

def WriteFileZip(rootdir,zipname):
    """ 
    递归读取rootdir文件夹中所有文件,
    rootdir: 压缩文件的绝对路径
    zipname: 压缩文件名称.
    """
    try:
        for d in os.listdir(rootdir):
            # 子文件的绝对路径
            rootfile = os.path.join(rootdir,d)
            # 判断是否是文件夹
            if os.path.isdir(rootfile): 
                # 改成相对路径.
                relFile = rootdir
                # 在zip文件中创建文件夹
                zipname.write(relFile) 
                # 递归压缩文件
                WriteFileZip(rootfile,zipname)
            else: # 判断是普通文件,写入zip文件中.
                relFile=rootfile # 改成相对路径
                zipname.write(relFile)

        return "已经将所有需要压缩的文件压缩成功"
    except Exception as e:
        print("压缩报错了")
        return e

if __name__=="__main__":
    zipFilePath = os.path.join(r"G:\softwarepackages","test.zip")
    zipname = zipfile.ZipFile(zipFilePath,"w",zipfile.ZIP_DEFLATED)
    rootdir = os.path.join("G:\\","softwarepackages")
    WriteFileZip(rootdir,zipname)

