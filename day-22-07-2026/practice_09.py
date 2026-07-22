import math

best = []

def solve(x, n, i=1, path=[]):
    global best

    if x == 0:
        if len(path) > len(best):
            best = path
        return

    if math.pow(i, n) > x:
        return

    solve(x - int(math.pow(i, n)), n, i + 1, path + [i])
    solve(x, n, i + 1, path)

solve(100, 2)

print(best)
