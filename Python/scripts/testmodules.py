# -*- coding:utf-8 -*-

import math 

# print(id(math))
# print(type(math))
"""
math模块被加载后,会生成一个module类的对象,该对象被math变量引用.
可通过math变量引用模块中所有的内容.
"""

# 使用__import__()动态导入指定的模块
s = "math"
m = __import__(s) # 导入后生成的模块对象的引用给变量m
print(m.pi)


# 需要动态导入,可以使用`importlib`模块
import importlib
a = importlib.import_module("math")
print(a.pi)
