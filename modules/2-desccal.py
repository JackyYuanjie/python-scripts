# -*- coding:utf-8 -*-

'''
Python中的日历模块(calendar)具有日历类，允许根据日期，月份和年份计算各种任务。Python中的TextCalendar和HTMLCalendar类允许您编辑日历并根据您的要求使用。
'''
# 1. 使用模块
# 导入该模块的所有类。
import calendar

# 创建文本日历,输出结果的第2行以Tu开头,表示是周二
a = calendar.TextCalendar(calendar.TUESDAY)

# 创建2020年1月的日历
str = a.formatmonth(2020,1)
print(str)

# 2. 以HTML格式打印日历
ht = calendar.HTMLCalendar(calendar.WEDNESDAY)
str = ht.formatmonth(2020,1)
print(str)


# 3. 使用c.itermonthday(2020,1),它将获取该月的总天数
# 循环遍历,获取2020年1月份的总天数
for i in ht.itermonthdays(2020,1):
    print(i)
'''
 输出中的零表示星期几是重叠的月份，这意味着它不属于该月份。
 除了日期1-31之外，上个月和后月的所有日期将在输出中显示为零。
'''

# 4. 从本地系统获取数据,
# 获取所有月份的名称:
for name in calendar.month_name:
    print(name)

# 获取所有星期名称:
for day in calendar.day_name:
    print(day)

# 5.获取整年特定日期的列表
for month in range(1,13):
    # 将2020年的每个月的总天数存入mycar变量中.
    mycar = calendar.monthcalendar(2020,month)

    week1 = mycar[0]　# 设置week1为日历的第一周
    week2 = mycar[1]　# 设置week2为日历的第二周    　

    if week1[calendar.MONDAY] != 0:
        auditday = week1[calendar.MONDAY]
    else:
        # 输出第一个月的第一个星期
        auditday = week2[calendar.MONDAY]
'''
检查第1周是否包含星期一,设置审核日,否则将审核日设置为第2周的第一个星期一. 输出显示该月的第一个星期一的日期.

如果在第一周，由星期一常量表示的日期不等于0，请记住零表示属于另一个月的日期。因此，在这种情况下，如果它为零，则它将是属于上个月的星期一。但如果第一个星期一不等于0，那意味着我的审计日将在第一周内。否则，如果它是0，那么第一个星期一不在该月的第一周，它必须在第二个星期。

将我的审计日变量设置为第二周代表的星期一.
'''

    print("{} {}".format(calendar.month_name[month],auditday))

'''
按照自己的方式更改日历,可更改当月日期.
以html格式打印日历
从本地系统获取数据
获取整年特定日期的列表.
'''









