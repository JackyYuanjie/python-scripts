# -*- coding:utf-8 -*-

# 测试简单的0不能做除数异常
"""
try:
    print("Step1")
    a = 3/0 
    print("step2")
except BaseException as e:
    print("Step3")
    print(e)
    print("发生异常,0不能做被除数")

print("step4")
"""

"""
while True:
    x = int(input("请输入一个数字:"))
    print("输入的数字:", x)
    if x == '9' or '0' or '99':
        print("退出程序")
        break
    break
"""

"""
while True:
    try:
        x = int(input("请输入数字:"))
        print("输入的数字:",x)
        if x == int(88):
            print("退出程序")
            break
    except BaseException as e:
        print(e)
        print("异常,输入的不是一个数字")

print("循环数字输入程序结束")
"""


# 多个except结构
"""
try:
    a = input("请输入被除数:")
    b = input("请输入除数:")
    c = float(a)/float(b)
    print(c)

except ZeroDivisionError:
    print("异常: 除数不能为0")
except TypeError:
    print("异常,类型错误")
except ValueError:
    print("异常,不能将字符串转化为数字")
except NameError:
    print("异常,变量不存在")
except BaseException as e:
    print(e)
"""



# try...except..else结构执行测试
"""
try:
    a = input("请输入被除数:")
    b = input("请输入除数:")
    c = float(a)/float(b)
except BaseException as e:
    print(e)
else:
    print("除的结果是:",c)

print("程序结束!")
"""


# try...except..finally结构简单测试
"""
try:
    a = input("请输入一个被除数:")
    b = input("请输入一个除数:")
    c = float(a)/float(b)
except BaseException as e:
    print(e)
else:
    print(c)
finally:
    print("我是finally中的语句,无论发生异常与否,都执行!")

print("程序结束!")
"""






# 测试finally
"""
try:
    f = open("./test.txt","r")
    content = f.readline()
    print(content)
except:
    print("文件未找到")
finally:
    print("run in finally,关闭资源")
    f.close()

print("程序执行结束!")
"""


# return和异常结构的正确处理方式
"""
def test01():
    print("step1")
    try:
        x = 3/0
        # return "a"
    except:
        print("step2")
        print("异常: 0不能做除数")
        # return "b"
    finally:
        print("step4")
        # return "d"

    print("step5")
    return "e"
# 一般不要把return语句放到`try,except,else,finally`块中,会发生一些意想不到的错误,建议放到方法最后
print(test01())
"""



# 使用Traceback模块打印异常信息
"""
import traceback

try:
    print("step1")
    num = 1/0
except:
    traceback.print_exc()
"""


# 自定义异常类
class AgeError(Exception): # 继承Exception
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo
    def __str__(self):
        return str(self.errorInfo)+",年龄错误,应该在1-100之间"
        # return "年龄错误"


if __name__=="__main__":  # 如果为True,则模块是作为独立文件运行.
    age = int(input("输入一个年龄:"))
    if age < 1 or age > 100:
        raise AgeError(age)
    else:
        print("正常的年龄:",age)

