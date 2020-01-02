# -*- coding:utf-8 -*-

import zipfile
import os
import shutil
import time 

def Un_zip(zipdir,zipname,unzippath):
    """
    解压zip文件
    zipdir: 压缩包的存放路径
    zipname: 压缩文件名
    unzippath: 解压缩后的存放路径
    """
    
    try:
        zippath = os.path.join(zipdir,zipname)
        r = zipfile.ZipFile(zippath)

        if r:
            unzipat = os.path.join(unzippath + "\\" + zipname + "_files")
            if os.path.isdir(unzipat):
                shutil.rmtree(unzipat)
                # os.rmdir(os.path.join(unzipat))
                print("如果存放目录已存在,就删除存放目录.")
            else:
                os.makedirs(unzippath + "\\" + zipname + "_files")
                print("解压后的存放目录已成功创建.")    
            for file in r.namelist():
                r.extract(file,unzipat)
        else:
            print("没有找到该zip压缩包.")
        time.sleep(10)
        r.close()    
        return "已经将zip文件解压完成."
    except Exception as e:
        return e


if __name__=="__main__":
    zipdir = r"G:\softwarepackages\unzipsoft"
    zipname = "好压.zip"
    unzippath = r"G:\softwarepackages\unzipsoft"
    unzip = Un_zip(zipdir,zipname,unzippath)
    print(unzip)