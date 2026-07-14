# 1. Write a program to print multiplication table of a given number using for loop.


# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]


# 3. Attempt problem 1 using while loop.


# 4. Write a program to find whether a given number is prime or not.


# 5. Write a program to find the sum of first n natural numbers using while loop.


# 6. Write a program to calculate the factorial of a given number using for loop.


# 7. Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3


# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3


# 9. Write a program to print the following star pattern.
# * * *
# * * for n = 3
# * * *


# 10. Write a program to print multiplication table of n using for loops in reversed
# order.



# 1. Write a program to print multiplication table of a given number using for loop.


for i in range(1, 11):
    print(f"{i} * 5 = {i*5}")

# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Gul zaman", "Nimra", "Sahil", "Afsha", "Sadam"] 

for q in l:
    if q.startswith("s") or q.startswith("S"):
        print(f"Good Morning: {q}")


# 3. Attempt problem 1 using while loop.


s = 1
while s <= 10:
    print(f"{s} * 5 = {s*5}")
    s += 1  # ending condition is important to add in the code 


# 4. Write a program to find whether a given number is prime or not.




n = int(input("Enter a number: "))

# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")
    

# if n <= 1:
#     print(f"No {n} n is not a prime number")
# else:
#     is_Prime = True

#     for i in range(2, int(n**0.5)+1):
#         if i%2 == 0:
#             is_Prime = False
#             break
       
             
#     if is_Prime:
#         print(f"Yes! {n} is a prime number.")
#     else:
#         print(f"No! {n} is not a prime number.")

# 5. Write a program to find the sum of first n natural numbers using while loop.
# sum = 0
# i = 1
# while i <= n:
#     sum+=i
#     i+=1

# print(sum)
    
    
# 6. Write a program to calculate the factorial of a given number using for loop.    

fact = 1 
for i in range(1, n+1):
    fact*=i

print("factorial", fact)

# 7. Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3


for i in range(1, n+1):
    print("*" * (2 * i - 1))


print("|||=======|||")
# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

for i in range(1, n+1):
    print("*" * (1 * i -1))
print("|||=======|||")
# 9. Write a program to print the following star pattern.
# * * *
# * * for n = 3
# * * *

for i in range(1, n+1):
    if i == 2:

        print("*" * i)
    else:
        print("*" *3 )
print("|||=======|||")


# 10. Write a program to print multiplication table of n using for loops in reversed
# order.

for i in range(n, 0, -1):
    print(f"Issue is what {i*n}")