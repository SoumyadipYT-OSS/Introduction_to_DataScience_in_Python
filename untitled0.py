# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 14:25:53 2024

@author: HP
"""


'''*args: Non-keyword arguments'''
def f(*args):
    print(type(args))
    print(*args)
    print(args)
    for i in args:
        print(i)
f(10,20,30,40,60,70)