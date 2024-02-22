# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:47:25 2024

@author: HP
"""

# Program on execution handling

print('statement 1')
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)