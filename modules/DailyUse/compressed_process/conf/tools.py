# -*- coding:utf-8 -*-
import os 
import pathlib
# from compressed_process.get_conf import GetConf
from .get_conf import GetConf 

#tools文件中不需要写类，写函数即可，如计算时间这类的方法，可以写到这个文件中方便调用
#如：破解密码rar和zip都用的到，破解密码写到这里 判断文件夹是否存在也写到这里

def rar_path():
    """获取压缩文件路径"""
    readconf = GetConf()
    RARpath = readconf.file_path()["readdict"]["rarpath"]
    # print(RARpath)

def zipfile_exists():
    """
    判断解压zip文件的目录是否存在
    """
    readcon = GetConf()
    ZIPpath = readcon.file_path()["readdict"]["zippath"]
    # print(ZIPpath)

def gzfile_exists():
    """
    判断解压.tar.gz文件的目录是否存在
    """
    gc = GetConf()
    Targzpath = gc.targzpath()["readdict"]["zippath"]
    # print(Targzpath)


