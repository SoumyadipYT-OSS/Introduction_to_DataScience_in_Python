# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:44:59 2024

@author: HP
"""

# create identity matrix

def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def main():
    n = 3
    matrix = identity_matrix(n)
    for row in matrix:
        print(row)


if __name__=="__main__":
    main()