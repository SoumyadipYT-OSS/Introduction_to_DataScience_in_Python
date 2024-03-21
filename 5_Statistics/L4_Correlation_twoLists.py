# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:34:54 2024

@author: HP
"""

# Write co-relation between two lists

def mean(lst):
    return sum(lst) / len(lst)

def de_mean(xs):
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def dot(v, w):
    assert len(v) == len(w), "vectors must be same length"
    return sum(v_i * w_i  for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)


def variance(lst):
    m = mean(lst)
    x = [i-m for i in lst]
    return sum_of_squares(x)/(len(lst)-1)


def co_variance(x, y):
    assert len(x) == len(y)
    return dot(de_mean(x), de_mean(y)) / (len(x) - 1)

import math

def standard_deviation(lst):
    return math.sqrt(variance(lst))


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0  and  stdev_y > 0:
        return co_variance(x, y) / (stdev_x * stdev_y)
    else:
        return 0
    
    
c = correlation([10,20,30,40,50], [11,8,6,4,2])
print(c)

from matplotlib import pyplot as plt
plt.plot([10,20,30,40,50], [11,8,6,4,2], marker='o')