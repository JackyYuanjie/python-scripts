# -*- coding:utf-8 -*-

"""
class Student:  # 类名首字母大写,多个单词采用驼峰原则.

    def __init__(self,name,score):  # self必须位于第一个参数
        self.name = name 
        self.score = score 

    def say_score(self):   # self必须位于第一个参数
        print("{0}的分数是: {1}".format(self.name,self.score))


a = Student("Jacky",98)  # 通过类名()调用构造函数.
a.say_score()

# self指的是对象本身.
a.age = 22
print(a.age)
a.salary = 8000
print(a.salary)

a2 = Student("Benny",80)
a2.say_score()
print('=='*30)
Student.say_score(a2)
print("=="*30)
print(dir(a2))
print("=="*30)
print(a2.__dict__)
print(a2.__class__)
print(isinstance(a2,Student))   # 判断a2是不是Student这个类.
"""



# 类对象
## 测试类对象的生成
"""
class Student:
    pass  # 空语句

print(type(Student))
print(id(Student))

Stu2 = Student
s1 = Stu2()
print(s1)
"""
"""
实际上生成了一个变量名就是类名"Student"的对象. 
通过赋值给新变量Stu2,也能实现相关的调用.说明,确实创建了"类对象".
"""

# print("=="*30)


# 类属性的使用测试
"""
class Student:

    company = "SXT"   # 类属性
    count = 0   # 类属性.

    def __init__(self,name,score):
        self.name = name     # 实例属性.
        self.score = score   
        Student.count = Student.count+1

    def say_score(self):   # 实例方法
        print("我的公司是:",Student.company)
        print(self.name,'的分数是:',self.score)

b5 = Student('Jacky',90)  # b5是实例对象,自动调用__init__()方法.
b5.say_score()
print('一共创建{0}个 Student对象'.format(Student.count))
"""
# print("=="*30)



# 类方法使用测试
"""
class Student:
    company = "The company"   # 类属性

    @classmethod
    def PrintCompany(cls):
        print(cls.company)

Student.PrintCompany()
"""


# 静态方法使用测试
"""
class Student:
    company = "The company"  # 类属性

    @staticmethod
    def add(a,b): # 静态方法
        print("{0}+{1}={2}".format(a,b,(a+b)))
        return a + b 


Student.add(20,30)
"""


# 析构函数
"""
class Person:

    def __del__(self):
        print("销毁对象:{0}".format(self))

p1 = Person()
p2 = Person()
del p2 
print("程序结束")
print(p1)
"""

# call方法和可调用对象
"""
class Salaryccount:
    # 工资计算类

    def __call__(self,salary):
        print("算工资了...")
        yearsalary = salary*12
        daySalary = salary//22.5
        hoursalary = salary//8

        return dict(yearsalary=yearsalary,monthsalary = salary,daySalary=daySalary,hoursalary=hoursalary)


c = Salaryccount()
print(c(9000))
"""




# Python中没有方法的重载.定义多个同名方法,只有最后一个有效.
"""
class Person:

    def say_hi(self):
        print("test")

    def say_hi(self,name):
        print("{0},test1".format(name))

p1 = Person()
# p1.say_hi()  # 不带参,报错: TypeError.
p1.say_hi("Jacky")
"""

# print("=="*30)



# 方法的动态性
"""
class People:

    def work(self):
        print("正在工作中...")

def play_game(s):
    print("{0}正在玩游戏".format(s))

def work2(s):
    print("一切都是对象")

People.play = play_game
p = People()
p.work()
p.play()

People.work = work2 
p.work()
"""


# 私有属性和私有方法
"""
class Employee:

    __company = "The network company"

    def __init__(self,name,age):
        self.name = name 
        # self.age = age 
        self.__age = age   # 私有属性 

    def __work(self):  # 私有方法
        print("上班")
        print("年龄:{0}".format(self.__age))
        print(Employee.__company)

e = Employee("Jacky",27)

print(e.name)
# print(e.age)
print(e._Employee__age)
print(dir(e))
e._Employee__work()  # 调用私有方法

print(Employee._Employee__company)
"""

# print("=="*30)



# @property装饰器
"""
class Employee:

    @property
    def salary(self):
        print("salary run...")
        return 2000

emp1 = Employee()
print(emp1.salary)
# print(type(emp1.salary))
"""


# @property装饰器用法
"""
class Employee:

    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary


emp1 = Employee("Jacky",15000)
print(emp1.salary)
emp1.salary = 30000
print(emp1.salary)
"""

"""
class Employee:

    def __init__(self,name,salary):
        self.__name = name 
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("录入错误,薪资在1000-50000这个范围")

    
emp1 = Employee("Benny",17000)
print(emp1.get_salary())
emp1.set_salary(2000)
print(emp1.get_salary())
"""


"""
class Employee:

    def __init__(self,name,salary):
        self.__name = name 
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if 10000<salary<30000:
            self.__salary = salary
        else:
            print("录入错误!薪资在10000-30000这个范围")

emp1 = Employee("Benny",17000)
print(emp1.salary)
# emp1.salary = 8000
emp1.salary = 15000
print(emp1.salary)
"""

print("=="*30)
