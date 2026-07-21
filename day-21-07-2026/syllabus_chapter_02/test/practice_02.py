import math
def commonDivisors(m, b):
    g = math.gcd(m, b)
    count = 0
    for i in range(1, g+1):
        if g % i == 0:
            count+= 1
    return count
print(commonDivisors(7, 13))


