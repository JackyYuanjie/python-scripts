# -*- coding:utf-8 -*-

import threading
import time 

"""
多个线程方法中可以共用全局变量.
查看work1线程对全局变量的修改,
在work2中能否查看修改后的结果.
"""

"""
# 定义全局变量
num = 0

# work1
def work1():

    # 声明num是一个全局变量
    global num

    for i in range(10):
        num += 1

    print("work1--------",num)


# work2
def work2():
    # num可以在多个线程中共享.
    print("work2=======",num)


if __name__=="__main__":
    # 创建2个子线程
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    # 启动线程
    t1.start()
    t2.start()

    # 判断线程数量不等于1,一直循环睡眠,保证print时,在t1和t2执行结束后,在print主线程.
    while len(threading.enumerate()) != 1:
        time.sleep(1)
    # 在t1和t2,线程执行完毕后再打印num
    print("main-------------",num)
"""


"""
多线程--共享全局变量问题
1.问题:
假设两个线程t1和t2都要对全局变量num(默认是0)进行加1运算,t1和t2都各对num加10次,num的最终结果为20.
但是由于是多线程同时操作,有可能出现下列情况:
1) 在num=0时,t1取得num=0,此时系统把t1调度为"sleeping"状态,把t2转换为"running"状态,t2也获得num=0
2) 然后t2对得到的值进行加1并赋给num,获得num=1.
3) 然后系统又把t2调度为"sleeping",把t2转为"running",线程t1又把它之前得到的0加1后赋值给num.
4) 这样导致虽然t1和t2都对num加1,但结果仍然是num=1
"""


# 定义全局变量
num = 0

# work1
def work1():

    # 声明num是一个全局变量
    global num

    for i in range(1000000):
        num += 1

    print("work1--------",num)


# work2
def work2():

    # 声明num是一个全局变量
    global num

    for i in range(1000000):
        num += 1
    # num可以在多个线程中共享.
    print("work2=======",num)


if __name__=="__main__":
    # 创建2个子线程
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    # 启动线程
    t1.start()
    # 优先让t1线程优先执行,t1执行完毕后,t2才能执行.
    t1.join()
    t2.start()

    # 判断线程数量不等于1,一直循环睡眠,保证print时,在t1和t2执行结束后,在print主线程.
    while len(threading.enumerate()) != 1:
        time.sleep(1)
    # 在t1和t2,线程执行完毕后再打印num
    print("main-------------",num)

# 结论:当多个线程修改同一个资源时,会出现资源竞争,导致计算结果有误.