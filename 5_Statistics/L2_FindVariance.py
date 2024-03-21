# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:45:34 2024

@author: HP
"""

# Write a code to find the variance

# =============================================================================
# Variance: A more complex measure of dispersion is the variance, which is computed as:
# =============================================================================


def mean(lst):
    return sum(lst) / len(lst)


def dot(v, w):
    assert len(v) == len(w), "vectors must be same length"
    return sum(v_i * w_i  for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

def variance(lst):
    m = mean(lst)
    x = [i-m for i in lst]
    return sum_of_squares(x)/(len(lst)-1)

ex1 = variance([10,15,22,25,34])
print(ex1)