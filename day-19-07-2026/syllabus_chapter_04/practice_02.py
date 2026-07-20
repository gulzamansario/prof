# Write a function that returns True if a string contains at least one digit, otherwise False.

st = input("Enter any string:- ")
def isDi(st):
    for i, ch in enumerate(st):
        hasDigit = False
        if ch.isdigit():
            hasDigit = True
        else:
            hasDigit = False 
    return hasDigit
    
print(isDi(st))