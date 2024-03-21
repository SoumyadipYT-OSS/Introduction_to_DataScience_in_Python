# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:05:19 2024

@author: HP
"""


# Write a python code to find the co-variance of two lists

def mean(lst):
    return sum(lst) / len(lst)

def dot(v, w):
    assert len(v) == len(w), "vectors must be same length"
    return sum(v_i * w_i  for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

def de_mean(xs):
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(lst):
    m = mean(lst)
    x = [i-m for i in lst]
    return sum_of_squares(x)/(len(lst)-1)



import math

def standard_deviation(lst):
    return math.sqrt(variance(lst))


def co_variance(x, y):
    assert len(x) == len(y)
    return dot(de_mean(x), de_mean(y)) / (len(x) - 1)