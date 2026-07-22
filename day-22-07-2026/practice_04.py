import math

X = 64
N = 3

root = round(math.pow(X, 1 / N))

if math.pow(root, N) == X:
    print("Yes")
else:
    print("No")
