# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 15:25:29 2024

@author: HP
"""

import random


print("__Example 1__")
print(random.randrange(3, 6))  # This will give any random number from [3, 4, 5]


print("__Example 2__")
lst1 = [10,20,30,40,50]
random.shuffle(lst1)
print(lst1)


print("__Example 3__")
friend = ['Ram', 'Sita', 'Laxman']
best_friend = random.choice(friend)
print(best_friend)


print("__Example 4__")
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 10)
print(winning_numbers)