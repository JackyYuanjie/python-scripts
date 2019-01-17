#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import zipfile,os,sys
# os.chdir('G:\\pyscripts')
# a = zipfile.ZipFile(sys.argv[1])
# print(a.namelist())
#
# b = len(a.namelist())
# print(b)
# a.close()
#
#
# c = zipfile.ZipFile(sys.argv[1])
# print(c.extractall())
#
# c.close()





"""modules learning"""
import sys

print('命令行参数:')
for i in sys.argv:
    print(i)

print(sys.path,'\n')

