# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 14:25:53 2024

@author: HP
"""


'''*args: Non-keyword arguments'''
print("__Example 1__")
def f(*args):
    print(type(args))
    print(*args)
    print(args)
    for i in args:
        print(i)
f(10,20,30,40,60,70)


print("__Example 2__")
def f1(arg1, *args):
    print('Normal Argument: ', arg1)
    print(args)
f1(10,20,30,40,50,60,70)