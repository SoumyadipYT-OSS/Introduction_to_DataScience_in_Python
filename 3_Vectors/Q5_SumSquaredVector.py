# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:42:51 2024

@author: HP
"""

# Find the sum of square of Vector

def sum_of_squares(vector1):
    return [v**v for v in vector1]


def main():
    print("Sum of square vector")
    eg1 = [1,2,3]
    print(sum_of_squares(eg1))

if __name__=="__main__":
    main()