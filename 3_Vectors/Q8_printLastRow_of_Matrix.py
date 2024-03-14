# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:43:56 2024

@author: HP
"""

# Print the last now of the matrix

def displayMatrix(m1):
    return m1


def printLastRowMatrix(M1):
    lastRowCount = len(M1)
    print(M1[lastRowCount - 1])


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
    
    print("\nLast row of the matrix:")
    printLastRowMatrix(eg1)


if __name__=="__main__":
    main()