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


def add_without_return(a, b):
    print(f"The sum of {a} and {b} is {a + b}")
    

def add_no_args_return():
    num1 = 10
    num2 = 20
    return num1 + num2


def add_no_args_no_return():
    num1 = 5
    num2 = 7
    print(f"The sum of predefined numbers is {num1 + num2}")





def userInput():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    add1(n1, n2)
    add2(n1, n2)
    

def main():
    # part 1
    userInput()
    # part 2
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    add_without_return(num1, num2)
    # part 3
    result = add_no_args_return()
    print(f"The sum of predefined numbers is {result}")
    # part 4
    add_no_args_no_return()


if __name__=="__main__":
    main()
    
    