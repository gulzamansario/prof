# 1. Write a program using functions to find greatest of three numbers. 

def gN3(a, b, c):
    if a > b and a > c:
        print(f"{a} is greater than {b}, and {c}")
    elif b >a and b >c:
        print(f"{b} is greater than {a}, and {c}")
    elif c > a and c > b:
        print(f"{c} is greater than {a}, and {b}")
    else:
        print("Something Went Wrong ")
        return

gN3(12.1, 12.9, 12.09899)
