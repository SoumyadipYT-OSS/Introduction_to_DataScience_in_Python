# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 14:25:53 2024

@author: HP
"""


'''*args: Non-keyword arguments'''
print("__Example 1 (Non-Keyword arguments) looks as tuple()__")
def f(*args):
    print(type(args))
    print(*args)
    print(args)
    for i in args:
        print(i)
f(10,20,30,40,60,70)



print("__Example 2 (Non-Keyword argument) looks as tuple()__")
def f1(arg1, *args):
    print('Normal Argument: ', arg1)
    print(args)
print("--test case 1--")
f1(10,20,30,40,50,60,70)
print("--test case 2--")
f1((10,20),30,40,50,60,70)



print("__Example 3 (Keyword arguments) looks as dictionary__")
'''**kwargs: Keyword arguments'''
def f2(**kwargs):
    print(kwargs)
f2(First_name='Soumyadip', Last_name='Majumder')