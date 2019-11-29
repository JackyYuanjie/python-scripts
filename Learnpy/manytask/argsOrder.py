# -*- coding:utf-8 -*-

"""
目标:
- 能够向线程函数传递多个参数.
- 多线程执行的顺序特点.
"""

import time 
import threading


def sing(a,b,c):
    print("参数:",a,b,c)
    for i in range(5):
        print("running sing")
        time.sleep(0.5)

def dance():
    for i in range(5):
        print("running to dance ...")
        time.sleep(0.5)

if __name__=="__main__":
    # 创建线程对象: threading.Thread
    # 在线程中,传递参数有三种方法:
    # 1.使用元组传递
    # thread_sing = threading.Thread(target=sing,args=(10,100,1000))
    # 2.使用字典传递
    # thread_sing = threading.Thread(target=sing,kwargs={"a": 10,"c": 100,"b": 1000})
    # 3. 混合使用元组和字典
    thread_sing = threading.Thread(target=sing,args=(10,),kwargs={"c": 1000,"b": 100})
    thread_dance = threading.Thread(target=dance)
    # 启动子线程
    thread_sing.start()
    thread_dance.start()


