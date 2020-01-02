# -*- coding:utf-8 -*-
import pathlib
import os 

"""
- pathlib库: 跨平台的、面向对象的路径操作库.
- pathlib(面向对象的文件系统路径)内置库.
- pathlib提供表示文件系统路径的类.
"""

"""
os.path.expanduser() --> pathlib.Path.home()
os.path.expanduser() --> pathlib.Path.expanduser()
os.stat() --> pathlib.Path.stat()
os.chmod() --> pathlib.Path.chmod()
"""

"""
- 获取当前文件路径:
  - os.getcwd()方法
  - pathlib.Path.cwd()方法
"""
# print(pathlib.Path.cwd())

"""
- 获取上层/上层目录
- 获取某一个文件的父目录:
  - os.path.dirname(os.path.dirname(os.getcwd()))
  - pathlib.Path.cwd().parent
"""
# print(pathlib.Path.cwd().parent)

"""
- 路径拼接
  - 在父目录中拼接路径: os.path.join(os.path.dirname(os.getcwd()),'目录名','文件名')
"""

# paths = ('python-scripts\modules\modemore')
# print(pathlib.Path.cwd().joinpath(paths))


# 2. pathlib.PurePath使用
"""
- PurePath是一个纯路径对象,纯路径对象提供了实际上不访问文件系统的路径处理操作.
"""
# print(pathlib.PurePath(__file__))
# print(pathlib.PurePath(__file__).match('*.py')) # 输出为True



# 3. PurePosixPath
os_path = os.path.dirname(__file__)
print(os_path)
# 通过pathlib.PurePath则获得了一个PurePosixPath对象
pure_path = pathlib.PurePath(__file__)
print(pure_path)
