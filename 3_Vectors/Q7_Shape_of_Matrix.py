# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:43:53 2024

@author: HP
"""

# Display the shape of a matrix

def displayMatrix(M1):
    return M1


def displayShapeMatrix(m1):
    row = len(m1)
    col = len(m1[0])
    print(row, " x ", col, "matrix")


def main():
    eg1 = [ 
            [1, 3, 2], 
            [4, 1, 5], 
            [2, 8, 3], 
            [9, 3, 5] 
        ]
    print(displayMatrix(eg1))
    displayShapeMatrix(eg1)


if __name__=="__main__":
    main()