import math

N = 4

total = 0

for i in range(1, N + 1):
    total += math.pow(i, 3)

print(int(total))
