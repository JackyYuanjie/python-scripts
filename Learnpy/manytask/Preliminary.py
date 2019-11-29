# -*- coding:utf-8 -*-

# 多任务介绍
# 同一时间,多个任务同时执行
import time

# 唱歌函数
def sing():
    for i in range(5):
        print("正在唱歌....")
        time.sleep(0.5)

def dance():
    for i in range(5):
        print("正在跳舞...")
        time.sleep(0.5)

# 调用
if __name__=="__main__":
#     sing()
#     dance()
    for i in range(5):
        sing()


