# -*- coding:utf-8 -*-

import threading



# 定义获取列表值的函数,参数为索引值.
def get_value(index):
    # 定义列表
    data_list = [1,3,5,7,9]
    # 上锁
    lock.acquire()
    # 输出内容
    if index >= len(data_list):
        print("{}下标越界".format(index))
        # 释放锁
        lock.release()
        return
    print(data_list[index])

    # 解锁
    lock.release()

# 创建10个线程,观察资源的等待状态
if __name__=="__main__":
    # 创建锁
    lock = threading.Lock()
    # 循环创建子线程访问列表
    for i in range(10):
        t1 = threading.Thread(target=get_value,args=(i,))
        t1.start()
