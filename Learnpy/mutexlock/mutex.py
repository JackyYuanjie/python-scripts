# -*- coding:utf-8 -*-

import threading
import time 

# 定义全局变量
num = 0

# work1
def work1():

    # 声明num是一个全局变量
    global num
    # 上锁
    lock1.acquire()

    for i in range(1000000):

        num += 1
    # 解锁
    lock1.release()
    print("work1--------",num)


# work2
def work2():

    # 声明num是一个全局变量
    global num

    for i in range(1000000):
        lock1.acquire()
        num += 1
        # 解锁
        lock1.release()
    # num可以在多个线程中共享.
    print("work2=======",num)


if __name__=="__main__":
    # 1. 创建一把互斥锁
    lock1 = threading.Lock()

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


