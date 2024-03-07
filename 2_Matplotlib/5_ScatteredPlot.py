# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:39:08 2024

@author: HP
"""


from matplotlib import pyplot as plt

users = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
website = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(users, minutes)

for label, friend_count, minute_count in zip(website, users, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),
                 xytext=(5, -5),
                 textcoords='offset points')