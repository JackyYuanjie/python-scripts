# -*- coding:utf-8 -*-

import os 
import tarfile
import shutil
import time 

def MkTgz(outpath,outfilename,sourcedir):
    """
    打包目录为tar.gz
    outpath: 压缩后存放的目录.
    outfilename: 压缩后的文件名.
    sourcedir: 需要压缩的目录
    """

    try:
        with tarfile.open(outfilename,"w:gz") as tar:
            tar.add(sourcedir,arcname=os.path.basename(sourcedir))
        time.sleep(10)
        shutil.move(outfilename,outpath + "\\" + outfilename)
        rig = "已经压缩完成了."
        return rig 
    except Exception as e:
        return e
             
if __name__=="__main__":
    destdir = r"G:\softwarepackages"
    outfi = 'nginx14.tar.gz'
    sourdir = r'G:\softwarepackages\nginx-1.14.1'
    make = MkTgz(destdir,outfi,sourdir)
    print(make)
    
