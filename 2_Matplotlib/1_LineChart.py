# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:32:44 2024

@author: HP
"""

from matplotlib import pyplot as plt
# Line chart
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1074.9, 2862.5, 5979.6, 10289.7, 14958.3]
# plt.plot(years, gdp, color = "Blue")

plt.plot(years, gdp, color='red', marker='P', linestyle='--')
plt.title('Year and GDP')
plt.xlabel('Years')
plt.ylabel('GDP')
plt.show()