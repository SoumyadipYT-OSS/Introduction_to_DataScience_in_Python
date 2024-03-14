# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:26:16 2024

@author: HP
"""

# Substraction 2 vectors

def sub_vectors(vector1, vector2):
    return [v1 - v2 for v1, v2 in zip(vector1,vector2)]

def main():
    eg1 = [8,10,12]
    eg2 = [2,4,6]
    
    print(sub_vectors(eg1, eg2))

if __name__=="__main__":
    main()