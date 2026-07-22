import math

def solve(x, n, i=1):
    if x == 0:
        return True

    if math.pow(i, n) > x:
        return False

    return solve(x - int(math.pow(i, n)), n, i + 1) or solve(x, n, i + 1)

print(solve(17, 2))
