# -*- coding:utf-8 -*-

import zipfile
import os 
import shutil
from threading import Thread

def password(passpath,filename):
    """
    passpath: 密码txt存放路径.
    filename: 密码txt文件的文件名称.
    生成10位数字密码
    """
    try:
        with open(passpath + "\\" + filename,"w+",encoding="utf-8") as f:
            for i  in range(10000000000):
                password = str(i).zfill(10)+'\n'
                f.write(password)
    except Exception as e:
        return e


def Unzip(zipdir,zipname,unzippath,password):
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
                print("如果存放目录已存在,就删除存放目录")
            else:
                os.makedirs(unzippath + "\\" + zipname + "_files")
                print("解压后的存放目录已成功创建.")
            
        else:
            print("解压失败或没有找到zip压缩包")
        r.close()
        return "已经将zip文件解压完成."
    except Exception as e:
        return e 

    try:
        # 破解密码:   
        # for fil in r.namelist(): #读取该路径下的所有zip文件
        r.extractall(pwd= bytes(password,"utf8"))
        print("password is:{}".format(password))
    except:
        pass

def main():
    zipdir = r"F:\PythonProject\python-scripts\practice"
    zipname = "filecompross.zip"
    unzippath = r"F:\PythonProject\python-scripts\practice"
    password(zipdir,"passdict.txt")
    # 读入所有密码
    Pwdlists = open(zipdir + "\\" + passdict.txt)
    unzip = Unzip(zipdir,zipname,unzippath,Pwd)
    # 写入密码        
    for line in Pwdlists.readlines():
        Pwd = line.strip('\n')
        t = Thread(target=Unzip,args=(zipdir,zipname,unzippath,Pwd))
        t.start()

if __name__=="__main__":
    main()

