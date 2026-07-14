# # Mehtab and bajaj earns points to save the ship 

# # Farrukh is Calculating the points
# # Mehtab = M
# # Bajaj = B 
# #  Farrukh is wondering how postiive inetger are there that are divisors(common Divisors)
# # to both numbers, M and B. Help him to find the number 

import math 
M, B = map(int, input("Enter the seprate numbers:- ").split())
g = math.gcd(M, B)
count = 0
for i in range(1, int(g ** 0.5) + 1):
    if g % i == 0:
        if i == g//i:
            count+=1
        else:
            count+=2
print(f"Postivie number tht exact divisor is {count}")











# import math

# M, B = map(int, input("Enter two seprate number: ").split())
# g = math.gcd(M, B)

# count = 0

# for i in range(1, int(g ** 0.5) + 1):
#     if g % i == 0:
#         if i == g // i:
#             count += 1
#         else:
#             count += 2

# print(count)
