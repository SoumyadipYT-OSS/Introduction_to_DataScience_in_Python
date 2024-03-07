# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:44:23 2024

@author: HP
"""

# Bar Chart
from matplotlib import pyplot as plt

games = ["Call of Duty", "E-Football", "Modern-Warfare 3", "Prince of Persia", "Need for Speed"]
studio_ratings = [3.8, 4.8, 4.9, 4.0, 3.6]
plt.bar(games, studio_ratings, color='Teal', edgecolor='Violet')
plt.xlabel('Games')
plt.ylabel('Ratings (? out of 5)')
plt.yticks(range(6))
plt.show()