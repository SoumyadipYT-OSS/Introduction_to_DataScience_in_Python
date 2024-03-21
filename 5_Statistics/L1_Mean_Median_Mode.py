# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:20:08 2024

@author: HP
"""


# Write code to find mean, median and mode

print("_Mean of List_")
def mean(lst):
    return sum(lst) / len(lst)





def find_median(lst):
    sorted_lst = sorted(lst)
    lst_len = len(lst)

    index = (lst_len - 1) // 2

    if (lst_len % 2):
        return sorted_lst[index]
    else:
        return (sorted_lst[index] + sorted_lst[index + 1])/2.0





from collections import Counter
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]