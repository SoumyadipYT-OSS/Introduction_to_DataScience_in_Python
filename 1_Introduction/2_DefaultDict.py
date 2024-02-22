# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:56:01 2024

@author: HP
"""


# Program to count each character in a string
name = "Padmaja"
d = {}
for c in name:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
print(d)


# Default Dict
