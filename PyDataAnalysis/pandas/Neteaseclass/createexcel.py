#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd 

filepath = 'F:/PythonProject/python-scripts/PyDataAnalysis/pandas/Neteaseclass/excelfiles/'
df = pd.DataFrame()  # 创建一个空的excel文件
df.to_excel(filepath + 'nullexcel.xlsx')

df = pd.DataFrame({'ID':[1,2,3],'Name':['numpy','matplotlib','pandas']})
print(df)
df = df.set_index('ID')  # 设置第一列为ID
df.to_excel(filepath + '三剑客.xlsx',sheet_name='Py数据分析三剑客')
print('Ok')


