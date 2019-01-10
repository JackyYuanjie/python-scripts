# -*- coding:utf-8 -*-

'''
python文件操作
创建,打开,添加,读取文件和写入文件等操作.
'''

"""
# 1. 如何创建一个txt文件
def main():
    # 声明变量f来打开一个名为first.txt的文件, open需要一个文件名和一个对文件的模式, w+: 表示写入并且如果文件中不存在则会创建文件
    f = open('./demo/first.txt','w+')  # 如果文件不存在,w会自动创建该文件.
    
    # 写入文件内容:
    for i in range(10):
        f.write('this is firstoneyuan {}\r\n'.format(i+1))
    # for循环,运行范围为10个数字.使用write函数将数据写入到文件中.

    # 关闭first.txt文件的实例
    f.close()



# 2. 如何添加数据到一个文件中

# a+ 表示以追加模式将数据写入文件, + 号表示,该文件不存在就会创建文件.
    f = open('./demo/first.txt','a+')
    for i in range(2):
        f.write('appending two line firstoney {}\r\n'.format(i+1))

    f.close()


# 3. 读取一个文件
# 以读取模式打开一个文件
f = open('./demo/first.txt','r')
# 使用mode函数检查文件是否处于打开模式.如果是打开模式,就读取并打印文件.
if f.mode == 'r':
    contents = f.read()
    print(contents)  # 输出到屏幕.
"""

def main():
# 4. 如何逐行读取文件
    f = open('./demo/first.txt','r')
    f1 = f.readlines()
    for x in f1:
        print(x)
# 逐行读取文件时,它将分隔每一行并以可读格式显示文件


if __name__=="__main__":
    main()

f = open('./demo/one.txt','w')
f.write('this is two')
f.close()

"""
python3的文件读取模式:
'r' : 默认模式为只读模式.
'w' :  打开文件再进行写入,如果文件不存在,会创建新文件,如果文件存在,会覆盖文件内容.
'x' : 创建一个新文件.如果文件已存在,则操作失败.
'a' : 以追加模式打开文件,如果文件不存在，则会创建新文件.
't' : 这是默认模式,以文本模式打开
'b' : 以二进制模式打开.
'+' : 打开一个文件进行读写(更新).

"""