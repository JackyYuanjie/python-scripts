# -*- coding:utf-8 -*-

import time 
import threading


def sing():
    for i in range(5):
        print("running sing")
        time.sleep(0.5)

def dance():
    for i in range(5):
        print("running to dance ...")
        time.sleep(0.5)

if __name__=="__main__":
    # 创建线程对象: threading.Thread
    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)
    # 启动子线程
    thread_sing.start()
    thread_dance.start()
