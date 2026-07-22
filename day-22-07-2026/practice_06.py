import math

def ways(x, n, i=1):
    if x == 0:
        return 1

    if math.pow(i, n) > x:
        return 0

    return ways(x - int(math.pow(i, n)), n, i + 1) + ways(x, n, i + 1)

print(ways(100, 2))
