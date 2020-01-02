# -*- coding:utf-8 -*-

"""
安装解压rar文件的插件:  pip install unrar
注意: 这个插件需要rarlib的支持.
安装rarlib: 
    https://www.rarlab.com/rar_add.htm  下载UnRARDLL.exe并安装,然后添加到环境变量中即可.
"""

# 说明:
    # 如果不安装UnRARDLL.exe,运行python脚本会报:LookupError: Couldn't find path to unrar library.错误.
    # 意思是找不到unrar library的路径,这里我们就需要去下载这个unrar library,事实上它就是UnRAR.dll这个东西,下载网址: http://www.rarlab.com/rar/UnRARDLL.exe或者去http://www.rarlab.com/rar_add.htm找到UnRAR.dll下载.

  # 第二步:
    # 安装完后我电脑中的路径为C:\Program Files (x86)\UnrarDLL,win7 32位的朋友可以将它添加到环境变量中，64位的需要将其中的X64文件夹设置为环境变量,因为unrar模块识别的文件是unrar.dll和unrar.lib,所以将文件夹中的UnRAR.dll和UnRAR.lib用小写重命名.

from unrar import rarfile
import os
import shutil


def Un_rar(rardir,rarname,Archiverar):
    """
    解压rar文件
    rardir: 压缩包的存放路径
    rarname: 要解压压缩包的文件名
    Archiverar: 解压缩后的存放路径.
    filestat: 判断文件后缀
    """

    try:
        Unrar_path = os.path.join(rardir,rarname)
        r = rarfile.RarFile(Unrar_path)

        if r:
            if os.path.isdir(Archiverar):
                shutil.rmtree(Archiverar)
                print("如果存放目录已存在,就删除该存放目录.")

                os.mkdir(Archiverar)
                print("解压后的存放目录已经成功创建.")
                
                r.extractall(Archiverar)
                print("解压完成,请查看解压后的存放目录")  

            else:
                os.mkdir(Archiverar)
                print("解压后的存放目录已经成功创建.")
                
                r.extractall(Archiverar)
                print("解压完成,请查看解压后的存放目录")        
    except Exception as e:
        return e



if __name__=="__main__":
    decompress = None
    rarname = ""
    rardir = ""

    if rarname:
        print("已经找到压缩文件名为：{}".format(rarname))
        if rardir:
            print("已经找到压缩文件的目录为:{}".format(rardir))
    else:
        rarname = input("请输入你想要解压的压缩文件名称(file.rar):")
        rarsuf = ".rar"
        zipsuf = ".zip"
        if rarname.endswith(rarsuf):
            rardir = input("请输入解压文件存放的目录(path):")
            if os.path.isdir(rardir):
                unrarpath = r'F:\PythonProject\python-scripts\practice'
                Archiverar = os.path.join(unrarpath + "\\") + "files_" + rarname
                decompress = Un_rar(rardir,rarname,Archiverar)
            else:
                print("没有指定解压文件存放的目录,请重新运行程序输入目录:")
        elif rarname.endswith(zipsuf):
            print("您输入的是zip压缩文件,暂不支持.")
        else:
            print("其他的压缩类型,暂时不支持.")
