# 4. Write a recursive function to calculate the sum of first n natural numbers. 
def sOn(n):
    if n == 0 or n == 1:
        return 1
    else:

        return n + sOn(n-1)
sun = sOn(5)
print(sun)
