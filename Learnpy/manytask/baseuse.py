# -*- coding:utf-8 -*-

import time 
import threading

"""
子线程创建的步骤:
1.导入模块: Threading
2. 使用threading.Thread() 创建对象:子线程对象.
3. 指定子线程执行的分支.
4. 启动子线程,线程对象:.start()
"""
# 定义函数
def sayhello():
    print("hello Beautiful girl")

# 调用函数,单线程方式:
if __name__=="__main__":
    for i in range(3):
        # 创建对象(子线程对象)
        # 指定子线程执行的分支.
        thread_obj = threading.Thread(target=sayhello)
        # 启动子线程,线程对象 start(),线程对象只有调用了start后,子线程才会执行.
        thread_obj.start()

    print("执行结束...")