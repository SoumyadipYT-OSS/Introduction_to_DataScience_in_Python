# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:44:26 2024

@author: HP
"""

# print the last column of a matrix

def displayMatrix(m1):
    return m1


def printLastColumnMatrix(matrix):
    last_column = []
    for row in matrix:
        last_column.append(row[-1])
    
    op = last_column
    print("[")
    for i in op:
        print("\t",i)
    print("]")


def main():
    eg1 = [ 
            [1, 3, 2], 
            [4, 1, 5], 
            [2, 8, 3], 
            [9, 3, 5] 
        ]
    
    res = displayMatrix(eg1)
    for i in res:
        print(i)
    
    print("\nLast column of the matrix: ")
    print(printLastColumnMatrix(eg1))


if __name__=="__main__":
    main()
