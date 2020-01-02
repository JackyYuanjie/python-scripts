# -*- coding:utf-8 -*-

"""
暴力破解zip压缩包的密码
"""
import itertools
import zipfile
import os 
import shutil
from threading import Thread


def Mkdir(zipname,unzippath,unzipat,r):
    """
    zipdir: 压缩包的存放路径
    zipname: 压缩文件名
    unzippath: 解压缩后的存放路径

    """
    try:
        if r:
            if os.path.isdir(unzipat):
                shutil.rmtree(unzipat)
                print("如果存放目录已存在,就删除存放目录")
            else:
                os.makedirs(unzippath + "\\" + zipname + "_files")
                print("解压后的存放目录已经成功创建.")
        else:
            print("解压失败或没有找到zip压缩包")
        # return "解压后的存放目录已经成功创建."
    except Exception as e:
        return e    

def Unzip(r,unzipat,password):
    """
    解压zip文件
    zipdir: 压缩包的存放路径
    zipname: 压缩文件名
    unzippath: 解压缩后的存放路径
    """   
    try:
        # 破解密码:   
        # for fil in r.namelist(): #读取该路径下的所有zip文件
        r.extractall(path=unzipat,pwd=password)
        print("password is:{}".format(password))

    except:
        pass

def main():
    zipdir = r"F:\PythonProject\python-scripts\practice"
    zipname = "filecompross.zip"
    unzippath = r"F:\PythonProject\python-scripts\practice"
    unzipat = os.path.join(unzippath + "\\" + zipname + "_files")
    zippath = os.path.join(zipdir,zipname)
    r = zipfile.ZipFile(zippath)
    
    mkdirectory = Mkdir(zipname,unzippath,unzipat,r)
    print(mkdirectory)
    print("正在排列组合破解密码,请稍等")
    result = itertools.permutations([0,1,2,3,4,5,6,7,8,9],10)
    pa = list(result)

    for i in list(pa):
        abc = [str(x) for x in list(i)]        
        password = ''.join(abc)
        running = Unzip(r,unzipat,password)
        print(running)
        # t = Thread(target=Unzip,args=(r,unzipat,password))
        # t.start()
        # print(t.name)
        # print(password)

if __name__=="__main__":
    main()