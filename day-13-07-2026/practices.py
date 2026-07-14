### Write a program to greet a user with “Good day” using functions.

def greet(name):
    print(f"Good Morning {name}")

user = "Gul zaman"
greet(user)


# There are two types of functions in python: 
# • Built in functions (Already present in python) 
# • User defined functions (Defined by the user) 


# RECURSION 
# Recursion is a function which calls itself. 
# It is used to directly use a mathematical formula as function.  
# Example: 
# factorial(n) = n x factorial (n-1) 
# This function can be defined as follows: 
# def factorial(n) 
# if i == 0 or i==1: # base condition which doesn’t call the functi