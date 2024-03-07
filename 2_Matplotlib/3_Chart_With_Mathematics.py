# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:57:43 2024

@author: HP
"""


# Bar Chart with mathematics
from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
lst = [min(grade // 10 * 10, 90) for grade in grades]
print(lst)
histogram = Counter(lst)
print(histogram)

plt.bar([x+5 for x in histogram.keys()], histogram.values(), color='orange', width=9.8)
plt.xticks([10*i for i in range(11)])