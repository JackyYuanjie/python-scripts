# -*- coding:utf-8 -*-

import tarfile


def untar(tarname,tardir):
    """
    解压tar.gz文件
    tarname: 压缩文件名
    tardir: 解压缩后的存放路径
    """
    try:
        t = tarfile.open(tarname)
        t.extractall(path=tardir)
        rig = "已经解压完成"
        return rig
    except Exception as e:
        return e

if __name__=="__main__":
    # sourcedir = r"G:\softwarepackages\targzsoft\nginx-1.14.1.tar.gz"
    # destdir = r"G:\softwarepackages"
    sourcedir = r"D:\YiBotSoft\YiBotInstall.tar.gz"
    destdir = r"D:\YiBotSoft\Yibotinstall"
    abc = untar(sourcedir,destdir)
    print(abc)