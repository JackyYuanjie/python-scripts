# -*- coding:utf-8 -*-

# 自定义线程类
"""
1. 让自定义类继承`threading.Thread`.
2. 让自定义类重写`run`方法.
3. 通过实例化自定义类对象`start()`方法启动自定义线程.
"""

import threading
import time 

# 自定义线程类.
class MyThread(threading.Thread):

    def __init__(self,num):
        # 先去调用父类的init方法
        super().__init__()
        self.num = num 

    # 重写父类的run方法
    def run(self):
        for i in range(5):
            # self.name 从父类继承的一个属性.
            print("正在执行子线程run:",i,self.name,self.num)
            time.sleep(0.5)


if __name__=="__main__":
    # 创建对象
    mythread = MyThread(10)
    # 线程对象.start() 启动线程
    # 子类从父类继承了start()方法
    mythread.start()

    print("结束...")