# -*- coding:utf-8 -*-

from pathlib import Path
import pathlib

# 列出子目录
p = Path(".")
a = [x for x in p.iterdir() if x.is_dir()]
# print(a)

# 列出当前f盘的所有py文件
abc = list(p.glob("**\*.py"))
# print(abc)

# 查看快捷方式
p = Path(r"C:\Users\Administrator\Desktop\Everything.exe")
# print(p)
# print("="*30)
# print(p.resolve())


# 查询路径属性
q = Path(r'F:\PythonProject')
# print(q.exists())
# print(q.is_dir())

# 拼接路径
pin = pathlib.PurePath("test","abc/dfa","tes")
# print(pin)
# print(pathlib.PurePath(Path("目录1"),Path("子目录1")))

# 使用当前目录
# currentpath = pathlib.PurePath()

