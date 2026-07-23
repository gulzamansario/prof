# import math

# def getTotalX(a, b):
#     def lcm(x, y):
#         return x * y // math.gcd(x, y)
#     l = a[0]
#     for x in a:
#         l = lcm(l, x)
#     g = b[0]
#     for x in b:
#         g = math.gcd(g, x)
#     count = 0
#     for x in range(l, g+1):
#         if g % x == 0:
#             count += 1
#     return count
import math
array = [1, 2, 3, 4]
lcm = array[0]
for num in array:
    lcm = (lcm * num) // math.gcd(lcm, num)
print(lcm)


ar = [12, 18, 24]

gcd = ar[0]

for num in ar:
    gcd = math.gcd(gcd, num)

print(gcd)