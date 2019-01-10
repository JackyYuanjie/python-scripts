# -*- coding:utf-8 -*-


#1.如何使用Date和DateTime 类

# 导入date和time模块
from datetime import date
from datetime import time
from datetime import datetime

# 2. 创建一个date对象的实例

def main():
    # date 对象
    #用date类的today方法,获取今天的日期,
    today = date.today()
    
    # 打印并运行代码
    print("Today's date is",today)

if __name__=="__main__":
    main()

# 输出结果为: Today's date is 2019-01-08

## * 使用date.today()打印日期
today = date.today()
print("date components:",today.day,today.month,today.year)

# 输出结果为date components: 8 1 2019

## * 星期序号
'''
对应星期的序号:
星期             星期序号
星期一(Monday)　 　　0
星期二(Tuesday)　　  1
星期三(Wednesday)　　2
星期四(Thursday)　 　3
星期五(Friday) 　　　4
星期六(Saturday) 　　5
星期日(Sunday) 　　　6
'''
# 返回今天的星期序号:
print("Today's Weekday Number:",today.weekday())
# 输出结果: Today's Weekday Number: 1


## * 当前日期和时间方法: now() today()
# 1. datetime对象,方法有hours,minutes,seconds 和milliseconds等.
#　从datetime类中,获取今天的日期
today = datetime.now()
print("当前日期和时间是:",today)
# 输出结果:当前日期和时间是: 2019-01-08 08:42:20.359371

# 2.使用datetime对象,返回time类型
# 仅打印当前时间,不打印日期
t = datetime.time(datetime.now())
print("当前时间是:",t)
# 输出结果: 当前时间是: 08:42:20.359382


# 3.打印星期和对应星期的序号
wd = date.weekday(today)
# 日期从0(星期一)开始
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print("今天的星期序号是: {}".format(wd))
print("今天是:" + days[wd])

'''
输出结果为:
今天的星期序号是: 1
今天是:Tuesday
'''


## * 如何用strftime方法格式化日期和时间
# 1. 如何格式化年
## 详细的输出格式化年: %Y. 简写的输出格式化年: %y
# 获取当前日期和时间

day = datetime.now()
# %y或者%Y　格式化年
print("今年是:",day.strftime("%Y"),"年")
'''
输出结果为: 今年是: 2019 年
说明:
使用了strftime函数来格式化输出
'''
# 只输出19不输出2019年
print("只输出了",day.strftime("%y"))
'''
输出结果为: 只输出了 19
说明:
    strftime函数可以分别声明日期、日期、月份和年份
    也可以格式化文本样式．
'''

# 3. 格式化文本样式
## 详细的输出格式化星期几: %A,简写的输出格式化星期几: %a

# 获取当前日期和时间
now = datetime.now()
print("今天是哪年几月几号:",now.strftime("%a,%d %b,%y"))
# %a　星期几, %d 日期, %B 月份, %Y 年份

print("今天是哪年几月几号:",now.strftime("%A,%D %B,%Y"))
'''
输出结果为:
今天是哪年几月几号: Tue,08 Jan,19
今天是哪年几月几号: Tuesday,01/08/19 January,2019
'''


# 4. 使用help(strftime)获取本地系统时间和日期
'''
%c 获取本地日期和时间
%x 获取本地日期
％X 获取本地时间
'''

now = datetime.now()
print("本地日期和时间是:",now.strftime("%c"))
print("本地日期是:",now.strftime("%x"))
print("本地时间是:",now.strftime("%X"))
'''
本地日期和时间是: Tue Jan  8 09:32:30 2019
本地日期是: 01/08/19
本地时间是: 09:32:30
'''


# 5. strftime函数可以格式化24小时制或者12小时制
'''
%I/%H - 12/24小时制,%M - 分钟, %S - 秒,%P - 本地的 am/pm(上午和下午) 
'''
# 12小时制, am和pm组成
print("12小时制是:",now.strftime("%I:%M:%S %P"))
# 24小时制
print("24小时制是:",now.strftime("%H:%M"))
'''
输出结果为:
12小时制是: 09:32:30 AM
24小时制是: 09:32
'''


## * 如何使用Timedelta 对象
# 使用TimeDelta对象，估计未来和过去的时间
# 用来计算未来或过去的事情

#　1. 导入timedelta对象
from datetime import timedelta

print(timedelta(days=365,hours=10,minutes=15))
# 输出结果为: 365 days, 10:15:00


# 2. 获取今天的日期和时间
print("today is:" + str(datetime.now()))
# 输出结果为:today is:2019-01-08 10:10:58.631157

# 3. 如何通过delta对象检索一年后的日期
print("one year from now it will be:" + str(datetime.now() + timedelta(days=365)))
#  输出结果为: one year from now it will be:2020-01-08 10:13:21.483079

# 4. 时间增量如何用于从当前日期和时间计算未来日期
print("in one week and 4 days it will be:" + str(datetime.now() + timedelta(weeks=1,days=4)))
# 输出结果为: in one week and 4 days it will be:2019-01-19 10:20:26.433204


# 5. 例子: 确定新年过去多少天
'''
使用today=date.today() 获取今天的日期
新年在1月1日,存储在nyd变量中.nyd=date(today.year,1,1)
if nyd<today 比较当前日期是否大于新年
((today-nyd).days)以天为单位给出当前日期和新年之间的差异
'''
# 获取今天的日期
today = date.today()
nyd = date(today.year,1,1) #这里指的是阳历(公历)
if nyd < today:
    print("新年1月1日就在{}天前".format((today - nyd).days))

# 输出结果为: 新年在7天前

"""
datetime模块总结:
对于以简单和复杂的方式操作日期和时间，datetime模块提供不同的类:

　date - 日期(Month, day, year)
　time - 时间(Hour, minute, second, microsecond)
　datetime - 时间和日期(Month, day, year, hour, second, microsecond)
　timedelta - 处理日期的持续时间
　tzinfo - 处理时区的抽象类


使用datetime对象:
　执行代码前,导入datetime对象: import datetime
　使用date.today函数打印单个日期/月/年以及当天
　使用date.time对象获取小时,分钟,秒和毫秒的时间

格式化时间的函数:
  使用strftime函数更改年份样式.
  分别打印日期,月份和年份．
  分别输出12小时制和24小时制的时间.

Timedelta 对象:
  使用timedelta对象，可以估计未来和过去的时间
  计算从当前时间开始的特殊日期(生日)剩余的总天数
  计算从当前时间开始的特殊日期(生日)的总天数
"""





