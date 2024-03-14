# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:25:10 2024

@author: HP
"""

# Addition of 2 vectors

def add_vectors(vector1, vector2):
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]


def main():
    eg_v1 = [1,2,3]
    eg_v2 = [4,5,6]
    
    add_vectors(eg_v1, eg_v2)


if __name__=="__main__":
    main()