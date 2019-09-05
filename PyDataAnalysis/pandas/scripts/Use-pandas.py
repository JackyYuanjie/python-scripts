#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 安装pandas
# pip install Pandas

# 运行测试套件
# 运行前需要安装: hypothesis和pytest
import pandas as pd 
# pd.test()


# In[5]:


# 对象创建
# 传入一些值的列表来创建一个Series,pandas会自动创建一个默认的整数索引.
import pandas as pd 
import numpy as np 
import pprint

s = pd.Series([1,3,5,np.nan,6,8])
print(s)
print('-'*30)
# 传递带有日期时间索引和带标签列的NumPy数组来创建DataFrame
dates = pd.date_range('20190815',periods=6)
pprint.pprint(dates)


# In[8]:


df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
# df.to_excel('./output.xlsx')
pprint.pprint(df)


# In[9]:


# 转化为类似Series的dict对象来创建DataFrame
df2 = pd.DataFrame({'A': 1.,
                   'B': pd.Timestamp('20190820'),
                   'C': pd.Series(1,index=list(range(4)),dtype='float32'),
                   'D': np.array([3] * 4,dtype='int32'),
                   'E': pd.Categorical(["test","train","test1","train2"]),
                   'F': 'foo'})
print(df2)
# DataFrame的列具有不同的数据类型
print(df2.dtypes)


# In[10]:


### 查看数据
# 查看DataFrame顶部数据
print(df.head(3))
print('+='*30)
# 查看DataFrame尾部数据
print(df.tail(3))
print('--+'*30)
# 显示索引,列和底层NumPy数据.
print(df.index)
print('-='*30)
print(df.columns)
print('-|'*30)
# DataFrame.to_numpy() 会给出Numpy对象. 输出时不包含行索引和列索引.
print(df.to_numpy())


# In[11]:


# describe()方法显示数据的快速统计摘要
print(df.describe())
print('--'*30)
# 转置数据
print(df.T)
print('=='*30)
# 按轴排序
print(df.sort_index(axis=1,ascending=False))
print('-='*30)
# 按值排序
print(df.sort_values(by='B'))


# In[12]:


### 获取
print(df['A'])
# 对行进行切片
print(df[0:])
print(df[0:2])
print('-=='*30)
print(df['20190816':'20190818'])


# In[13]:


### 按标签选择
# 通过标签获取一行数据
print(df.loc[dates[0]])
print(df.loc[dates[1]])
print('=='*30)
# 通过标签在多个轴上选择数据
print('通过标签在多个轴上选择数据')
print(df.loc[:,['A','B']])
print('--'*30)
print(df.loc[:,['C']])


# In[14]:


# 通过标签同时在两个轴上切片
print('通过标签同时在两个轴上切片')
print(df.loc['20190817':'20190819',['A','B']])


# In[15]:


# 减小返回对象的大小
print(df.loc['20190820',['A','B']])


# In[16]:


# 获取标量值
print(df.loc[dates[0],'A'])


# In[17]:


# 快速访问标量
print(df.at[dates[0],'A'])


# In[18]:


### 布尔索引
# 使用单个列的值来选择数据
print(df[df.A > 0])   # 会输出为True的内容.
print(df.A > 0) # 将True和False都打印出来.


# In[19]:


# 从满足布尔条件的DataFrame中选择值:
print(df[df > 0])


# In[20]:


# 使用isin()方法过滤
df3 = df.copy()
# print(df3)
# df3['E'] = ['one','one','two','three','four','three']
df3['E'] = ['one','two','three','four','five','six']

# print(df3)
print('-='*30)
print(df3[df3['E'].isin(['two','four'])])


# In[21]:


### 赋值
# 添加新列将自动根据索引对齐数据.
s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range('20190818',periods=6))
print(s1)
df3['F'] = s1
print(df3['F'])


# In[22]:


# 通过标签赋值
df3.at[dates[0],'A'] = 0
print(df3)


# In[27]:


### 通过位置赋值
df.iat[0,1] = 0 
print(df)


# In[29]:


# 使用NumPy数组赋值
df3.loc[:,'D'] = np.array([5] * len(df))
print(df3) # 前面一系列赋值操作的结果.


# In[41]:


# 带有where条件的赋值操作.
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)


# In[42]:


### 缺失值
# pandas主要使用值np.nan来表示缺失的数据.
# 重建索引允许更改/添加/删除指定轴上的索引.这个操作会返回一个副本.
df5 = df.reindex(index=dates[0:4],columns=list(df.columns) + ['E'])
df5.loc[dates[0]:dates[1],'E'] = 1
print(df5)


# In[45]:


# 删除任何带有缺失值的行
print(df5.dropna(how='any'))


# In[46]:


# 填充缺失值
print(df5.fillna(value=5))


# In[47]:


# 获取值为nan的掩码
print(pd.isna(df5))


# In[49]:


### 统计
# 进行描述性统计
print(df5.mean())
print('-='*30)
# 在其它轴上进行同样的操作:
print(df5.mean(1))


# In[51]:


# 使用具有不同维度且需要对齐的对象进行操作. pandas会自动沿指定维度进行广播.
s = pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)
print(s)

print(df5.sub(s,axis='index'))


# In[53]:


### 应用
# 将函数应用于数据
print(df5.apply(np.cumsum))

print(df5.apply(lambda x: x.max() - x.min()))


# In[56]:


### 直方图化
s1 = pd.Series(np.random.randint(0,7,size=10))
print(s1)
print('=+'*30)
print(s1.value_counts())


# In[57]:


### 字符串方法
# Series在str属性中有一组字符串处理方法,可对数组的每个元素进行操作.
s2 = pd.Series(['A','B','C','Aaba','Baca',np.nan,'CABA','dog','cat'])
print(s2.str.lower())


# In[60]:


## 合并
### 连接
# 使用concat()连接pandas对象.
df6 = pd.DataFrame(np.random.randn(10,4))
print(df6)
print('---'*30)
pieces = [df6[:3],df6[3:7],df6[7:]]
print(pd.concat(pieces))


# In[62]:


### Join
# SQL风格的合并
left = pd.DataFrame({'key': ['foo','foo'],'lval':[1,2]})
right = pd.DataFrame({'key': ['foo','foo'],'rval': [4,5]})
print(left)
print('='*30)
print(right)
print('='*30)
print(pd.merge(left,right,on='key'))


# In[63]:


# 另一个例子
left = pd.DataFrame({'key': ['foo','bar'],'lval': [1,2]})
right = pd.DataFrame({'key': ['foo','bar'],'rval':[4,5]})
print(left)
print('-'*30)
print(right)
print(pd.merge(left,right,on='key'))


# In[66]:


### 追加
df7 = pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
print(df7)
print('=='*30)
s3 = df7.iloc[3]
print(df7.append(s3,ignore_index=True))


# In[68]:


### 分组
"""
group by包括:
分割: 根据一些标准将数据分解成组.
应用: 将函数独立地应用于每个组.
组合: 将结果组合成数据结构.
"""
df8 = pd.DataFrame({'A': ['foo','bar','foo','bar',
                         'foo','bar','foo','foo'],
                   'B': ['one','one','two','three',
                        'two','two','one','three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

print(df8)
# 分组,然后将sum()函数应用于分组结果.
print(df8.groupby('A').sum())
print('=-'*30)
# 按多列分组形成层次索引,用sum函数
print(df8.groupby(['A','B']).sum())


# In[69]:


### 堆叠(Stack)
tuples = list(zip(*[['bar','bar','baz','baz',
                    'foo','foo','qux','qux'],
                   ['one','two','one','two',
                   'one','two','one','two']]))

index = pd.MultiIndex.from_tuples(tuples,names=['first','second'])
df = pd.DataFrame(np.random.randn(8,2),index=index,columns=['A','B'])
df9 = df[:4]
print(df9)


# In[70]:


### stack()方法压缩DataFrame的列
stacked = df9.stack()
print(stacked)


# In[72]:


# stack()的逆操作是unstack(),默认情况下取消最后压缩的哪个级别.
print(stacked.unstack())
print('=='*30)
print(stacked.unstack(1))
print('-='*30)
print(stacked.unstack(0))


# In[75]:


### 数据透视表
df10 = pd.DataFrame({'A': ['one','one','two','three'] * 3,
                    'B': ['A','B','C'] * 4,
                    'C': ['foo','foo','foo','bar','bar','bar'] * 2,
                    'D': np.random.randn(12),
                    'E': np.random.randn(12)})

print(df10)
print('-='*30)
# 从这些数据生成数据透视表
pd.pivot_table(df10,values='D',index=['A','B'],columns=['C'])


# In[76]:


### 时间序列(TimeSeries)
# 用于在频率转换期间执行重采样操作.
rng = pd.date_range('22/08/2019',periods=100,freq='S')
ts = pd.Series(np.random.randint(0,500,len(rng)),index=rng)
print(ts.resample('5Min').sum())


# In[79]:


# 时区代表
rng = pd.date_range('21/08/2019 21:29:30',periods=5,freq='D')
ts = pd.Series(np.random.randn(len(rng)),rng)
print(ts)

print('-='*30)
ts_utc = ts.tz_localize('UTC')
print(ts_utc)

print('-='*30)
# 转换为另一个时区
print(ts_utc.tz_convert('US/Eastern'))


# In[82]:


# 在时间跨度表示之间转换
rng = pd.date_range('22/08/2019',periods=5,freq='M')
ts = pd.Series(np.random.randn(len(rng)),index=rng)
print(ts)
print('-='*30)
ps = ts.to_period()
print(ps)
print('-='*30)
print(ps.to_timestamp())


# In[83]:


# 周期和时间戳之间的转换可以用算术函数. 
# 示例: 以11月为结束年份的季度频率转换为季度结束后一个月末的上午9点.
prng = pd.period_range('2010Q1','2019Q4',freq='Q-NOV')
ts = pd.Series(np.random.randn(len(prng)),prng)
ts.index = (prng.asfreq('M','e') + 1).asfreq('H','s') + 9
print(ts.head())


# In[86]:


### 分类(Categoricals)
# pandas可以在DataFrame中包含分类数据.
df11 = pd.DataFrame({"id": [1,2,3,4,5,6],
                    "raw_grade": ['a','b','b','a','a','e']})
# 将原始成绩转换为category数据类型
df11["grade"] = df11["raw_grade"].astype("category")
print(df11["grade"])
print('-='*30)


# In[87]:


# 将类别重命名为更有意义的名称(通过调用Series.cat.categories来替换)
df11["grade"].cat.categories = ["very good","good","very bad"]
print(df11["grade"].cat.categories)


# In[88]:


# 对categories重新排序并同时添加缺少的category(Series.cat下的方法默认返回一个新的Series)
df11["grade"] = df11["grade"].cat.set_categories(["very bad","bad","medium",
                                                 "good","very good"])
print(df11["grade"])


# In[90]:


# 排序时按categories中的顺序排序,不是按照词汇顺序排序.
print(df11.sort_values(by="grade"))


# In[91]:


# 按分好类的列分组(groupby)可以显示空categories。
print(df11.groupby("grade").size())


# In[92]:


### 绘图
ts = pd.Series(np.random.randn(1000),
              index=pd.date_range('22/08/2019',periods=1000))
ts = ts.cumsum()
ts.plot()


# In[94]:


import matplotlib.pyplot as plt
# 在一个DataFrame中,plot方法绘制带有label的所有列.
df12 = pd.DataFrame(np.random.randn(1000,4),index=ts.index,
                   columns=['A','B','C','D'])

df13 = df12.cumsum()
plt.figure()
df13.plot()
plt.legend(loc='best')


# In[96]:


### 数据输入/输出
# 写入csv文件
df13.to_csv('./best.csv')
# 从csv文件读数据
pd.read_csv('./best.csv')


# In[102]:


### HDF5
# pip install tables
# 写入HDF5
df13.to_hdf('./best.h5','df')
# 从HDF5读数据
pd.read_hdf('./best.h5','df')


# In[103]:


### Excel
# 写入excel文件
df13.to_excel('./best.xlsx',sheet_name='best')
# 从excel文件读取数据
pd.read_excel('./best.xlsx','best',index_col=None,na_values=['NA'])


# In[104]:


# Gotchas 坑
# 异常
if pd.Series([False,True,False]):
    print("I was true")

