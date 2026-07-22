import math

def show(x, n, i=1, path=[]):
    if x == 0:
        print(path)
        return

    if math.pow(i, n) > x:
        return

    show(x - int(math.pow(i, n)), n, i + 1, path + [i])
    show(x, n, i + 1, path)

show(17, 2)
