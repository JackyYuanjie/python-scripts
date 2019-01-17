#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tarfile,os

#uncompress method
# def un_tarfile(file_name):
#     tar = tarfile.open(file_name)
#     names = tar.getnames()
#
#     if os.path.isdir(file_name + "_files"):
#         pass
#     else:
#         os.mkdir(file_name + "_files")
#
#     for name in names:
#         tar.extract(name,file_name + "_files/")
#
#
#
#
# un_tarfile('pyscripts.tar.gz')


#compress zip
import zipfile,tarfile,os
#compress method

def deco_zip(file_deco_name):
    zip_file_name = zipfile.ZipFile(file_deco_name)

    if os.path.isdir(file_deco_name):
        pass
    else:
        os.mkdir(file_deco_name)

    for names in zip_file_name.namelist():
        zip_file_name.extract(names,file_deco_name)



deco_zip('pyscripts.tar.gz_files')

