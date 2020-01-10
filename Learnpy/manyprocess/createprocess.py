# -*- coding:utf-8 -*-

"""
目标:
- 使用multiprocessing.Process 类能够创建进程对象.
- 使用multiprocessing.Process的target参数能够指定进程执行的任务函数.

"""

import multiprocessing
import time 

def work1():
    for i in range(10):
        print("running to work1...")


if __name__ == "__main__":
    # 通过模块提供的Process类创建进程对象.
    process_obj = multiprocessing.Process(target=work1)
    # 启动进程
    process_obj.start()

    print("主线程...")