# -*- coding:utf-8 -*-

# 获取活跃的线程数量和获取线程名称
"""
threading.enumerate()获取当前所有活跃的线程对象列表,
使用len()对列表求长度可以看到当前活跃的线程的个数.
"""

import time 
import threading


def sing():
    for i in range(5):
        print("running sing",threading.current_thread())
        time.sleep(0.5)

def dance():
    for i in range(5):
        print("running to dance ...",threading.current_thread())
        time.sleep(0.5)

if __name__=="__main__":

    # 线程的名称,获取当前的线程对象.
    print(threading.current_thread())

    # 获取当前所有活跃的线程对象列表
    thread_list = threading.enumerate()
    print("1当前线程数量",len(thread_list))
    # 创建线程对象: threading.Thread
    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)

    thread_list = threading.enumerate()
    print("2当前线程数量",len(thread_list))

    # 启动子线程
    thread_sing.start()
    thread_dance.start()
    while True:    
        thread_num = len(threading.enumerate())
        print("3当前线程数量",thread_num)

        # 如果只剩下主线程就停止
        if thread_num <= 1:
            break

        time.sleep(0.5)


