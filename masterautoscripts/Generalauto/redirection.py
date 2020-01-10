# -*- coding:utf-8 -*-
import sys 

"""
接收重定向输入,使用stdin.
"""

class Redirection(object):
    def __init__(self,in_obj,out_obj):
        self.input = in_obj
        self.out_obj = out_obj
    
    def read_line(self):
        res = self.input.readline()
        self.output.write(res)
        return res 

if __name__=='__main__':
    if not sys.stdin.isatty():
        sys.stdin = Redirection(in_obj=sys.stdin,out_obj=sys.stdout)
    a = input("Enter a sring:")
    b = input("Enter another string:")
    print('Entered strings are:',repr(a),'and',repr(b))
    
