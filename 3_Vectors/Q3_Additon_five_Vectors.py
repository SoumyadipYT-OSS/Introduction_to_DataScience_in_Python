# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:27:02 2024

@author: HP
"""

# Addition of 5 vectors


def addFiveVectors(vec1, vec2, vec3, vec4, vec5):
    return [v1 + v2 + v3 + v4 + v5 for v1, v2, v3, v4, v5 in zip(vec1, vec2, vec3, vec4, vec5)]


def main():
    eg1 = [1, 2]
    eg2 = [3, 5]
    eg3 = [4, 5]
    eg4 = [2, 3]
    eg5 = [1, 3]
    
    print(addFiveVectors(eg1, eg2, eg3, eg4, eg5))


if __name__=="__main__":
    main()