# -*- coding:utf-8 -*-

# 测试递归算法

num = 1

def a1():
    global num # 如果要在函数内改变全局变量的值,增加global关键字声明
    num += 1
    print("a1")
    if num < 3:
        a1()

def b1():
    print("b1")

a1()


# 使用递归求n!
def factorial(n):
    if n == 1:
        return n  
    else:
        return n*factorial(n-1)


a = factorial(10)
print(a)



