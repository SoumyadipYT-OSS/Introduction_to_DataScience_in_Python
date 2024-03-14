# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:42:53 2024

@author: HP
"""

# Find magnitude of a vector

import math

def magnitude(vector):
    return math.sqrt(sum(v**2 for v in vector))


def main():
    eg = [1, 2, 3]
    print("Magnitude: ", magnitude(eg))


if __name__=="__main__":
    main()