# -*- coding:utf-8 -*-

# 继承
"""
class Person:
    
    def __init__(self,name,age):
        self.name = name 
        self.__age = age  # 私有属性.

    def say_age(self):
        print(self.name,"的年龄是:",self.__age)


class Student(Person):
    def __init__(self,name,age,score):
        self.score = score 

        #  构造函数中包含调用父类构造函数.根据需要. 
        # 子类并不会自动调用父类的__init__(),必须显式的调用它.
        Person.__init__(self,name,age)  

s1 = Student("Jacky",27,90)
s1.say_age()
print(dir(s1))
print(s1.name)
# print(s1.age)  # AttributeError: 'Student' object has no attribute 'age'
print(s1._Person__age)

"""



# 类成员的继承和重写案例
"""
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    def say_age(self):
        print(self.name,"的年龄是:",self.age)

    def say_name(self):
        print("我的名字是{0}".format(self.name))

    
class Student(Person):

    def __init__(self,name,age,score):
        # 必须显式的调用父类初始化方法,不然解释器不会调用.
        Person.__init__(self,name,age)
        self.score = score 

    def say_name(self):
        '''重写父类方法'''
        print("报告老师,我的名字是: {0}".format(self.name))


s = Student("Benny",27,90)  
s.say_age()
s.say_name()
"""



# 查看类的继承层次结构
"""
class A: pass 
class B(A): pass
class C(B): pass 

print(C.mro())
"""




# 查看对象所有属性和object进行比对.
"""
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    def say_age(self):
        print(self.name, "的年龄是:",self.age)


obj = object()
print(dir(obj))
print("=="*30)
c1 = Person("Dannllie",35)
print(dir(c1))
"""




# # 重写__str__()方法
"""
class Person:   # 默认继承object类
    def __init__(self,name):
        self.name = name 

    def __str__(self):
        return "名字是: {0}".format(self.name)

p = Person("Nacy")
print(p)
"""



# 多重继承
"""
class A:
    def aa(self):
        print("aa")
    
class B:
    def bb(self):
        print("bb")

class C(B,A):
    def cc(self):
        print("cc")

c = C()
c.cc()
c.bb()
c.aa()
print(C.mro())
"""



# mro函数
"""
class A:
    def aa(self):
        print("aa")
    
    def say(self):
        print("say AAA!")

class B:
    def bb(self):
        print("bb")
    
    def say(self):
        print("say BBB!")

class C(B,A):
    def cc(self):
        print("CC")


c = C()
c.cc()
c.bb()
c.aa()
print(C.mro())  # 打印类的层次结构
c.say()    # 解释器寻找方法是:"从左到右"的方式寻找. 会执行B的say()
"""

    


#  super()获得父类的定义, 而不是父类的对象
"""
class A:

    def say(self):
        print("A",self)

class B(A):
    
    def say(self):
        # A.say(self)
        super().say()
        print("B:",self)


B().say()
"""



# 多态
"""
class Man:
    
    def eat(self):
        print("开始吃饭了")

class Chinese(Man):
    
    def eat(self):
        print("中国人用筷子吃饭")

class English(Man):
    
    def eat(self):
        print("美国人用叉子吃饭")

class Indian(Man):
    
    def eat(self):
        print("印度人用手吃饭")

def manEat(m):
    if isinstance(m,Man):
        m.eat()  # 多态,一个方法调用,根据对象不同调用不同的方法.
    else:
        print("不能吃饭")

manEat(Chinese())
manEat(English())
"""



# 特殊方法和运算符重载
"""
a = 20
b = 30
c = a+b 
d = a.__add__(b)
print("c=",c)
print("d=",d)
"""

"""
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.__age = age 
    
    def __str__(self):
        '''将对象转化成一个字符串,一般用于print方法'''
        return "名字是:{0},年龄是{1}".format(self.name,self.__age)

    def __add__(self,other):
        if isinstance(other,Person):
            return "{0}===={1}".format(self.name, other.name) 
        else:
            return "不是同类对象,不能相加"

    def __mul__(self,other):
        if isinstance(other,int):
            return self.name*other
        else:
            return "不是同类对象,不能相乘"

p = Person("Marco",29)
q = Person("Sofi",35)
print(p)
x = p + q 
print(x)
print(x*30)
"""




# 测试对象的浅拷贝和深拷贝
"""
import copy 

class MobilePhone:

    def __init__(self,cpu,screen):
        self.cpu = cpu 
        self.screen = screen

class CPU:
    def calcalate(self):
        print("算123456")
        print("cpu对象:",self)

class Screen:
    def show(self):
        print("显示一个画面,照亮你的美")
        print("screen对象:",self)

# 测试变量赋值
c1 = CPU()
c2 = c1 
print("测试变量赋值")
print(c1)
print(c2)
print("=="*30)

# 测试浅复制
s1 = Screen()
m1 = MobilePhone(c1,s1)
m2 = copy.copy(m1)
# print(m1)
# print(m2)
print("测试浅复制")
print(m1,m1.cpu,m1.screen)
print(m2,m2.cpu,m2.screen)
print("=="*30)

# 测试深复制
m3 = copy.deepcopy(m1)
print(m1,m1.cpu,m1.screen)
print(m3,m3.cpu,m3.screen)
"""




# 测试组合

# 使用继承实现代码的复用
"""
class A1:
    
    def say_al(self):
        print("a1,a1,a1")

class B1(A1):
    pass

b1 = B1()
b1.say_al()


# 使用组合实现代码复用.
class A2:
    def say_a2(self):
        print("a2,a2,a2")

class B2:
    def __init__(self,a):
        self.a = a 

a2 = A2()
b2 = B2(a2)
b2.a.say_a2()

"""

# 测试has-a关系,使用组合
"""
class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu = cpu 
        self.screen = screen

class CPU:
    def calculate(self):
        print("算123456")
        print("cpu对象:",self)

class Screen:
    def show(self):
        print("显示一个好看的画面,照亮你的美")
        print("screen对象:",self)

m = MobilePhone(CPU(),Screen())
m.cpu.calculate()
m.screen.show()
"""



# 工厂模式
class CarFactory:
    def createCar(self,brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌,无法创建."

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass


factory = CarFactory()
c1 = factory.createCar("奔驰")
c2 = factory.createCar("宝马")
print(c1)
print(c2)




print("=="*30)
# 测试单例模式
class MySingleton:

    __obj = None  # 类属性
    __init_flag = True

    def __new__(cls,*args,**kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self,name):
        if MySingleton.__init_flag:
            print("init.....")
            self.name = name 
            MySingleton.__init_flag = False

a = MySingleton("na")
b = MySingleton("bb")
print(a)
print(b)
c = MySingleton("cc")
print(c)
