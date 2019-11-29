# -*- coding:utf-8 -*-

import threading
import time

def work():
    for i in range(10):
        print("正在执行work1....",i)
        time.sleep(0.5)

if __name__ == "__main__":
    # 创建子线程
    # 创建线程对象
    thread_work = threading.Thread(target=work)
    # 线程守护:表示子线程守护主线程(主线程结束后,子线程也结束.)
    thread_work.setDaemon(True)
    # 启动子线程
    thread_work.start()

    # 睡眠
    time.sleep(2)
    print("Game Over!!")
    # 让程序退出,主线程主动结束.
    exit()
    