# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:31:18 2024

@author: HP
"""

# function as an argument
def double(x):
    return x*2

def apply(f):
    return f(1)

my_double = double

x = apply(my_double)
print(x)