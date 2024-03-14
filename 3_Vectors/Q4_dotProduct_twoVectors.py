# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:27:20 2024

@author: HP
"""

# Dot product of 2 vectors

def dotProduct(vec1, vec2):
    return [v1 * v2 for v1, v2 in zip(vec1, vec2)]


def main():
    eg1 = [3, 4, 8]
    eg2 = [2, 3, 5]
    
    print(dotProduct(eg1, eg2))


if __name__=="__main__":
    main()