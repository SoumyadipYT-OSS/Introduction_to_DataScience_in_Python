# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:01:04 2024

@author: HP
"""

# =============================================================================
# Write a program for addition of two numbers using function
    # 1. Arguments with return value
    # 2. Arguments without return value
    # 3. No argument return value
    # 4. No argument no return value
# =============================================================================


n1 = 0
n2 = 0
def add1(x, y):
    return x+y


def add2(x, y):
    res = x+y
    print("Addition: ", res)
    

def add3():
    res = n1+n2
    return res

def add4():
    res = n1+n2
    print("Addition: ", res)



def userInput():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    add1(n1, n2)
    add2(n1, n2)
    add3()
    add4()
    

def main():
    userInput()


if __name__=="__main__":
    main()
    
    