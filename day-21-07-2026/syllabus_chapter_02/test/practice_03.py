# ### Q3. Count Common Divisors

# Two students scored **M** and **B** points in a competition.

# Write a function that returns how many positive integers divide **both** scores.

# **Example**

# ```
# Input:
# 12 18

# Output:
# 4
# ```
from math import gcd
def common_divisor(a, b):
    g = gcd(a, b)
    count = 0
    for i in range(1, g+1):
        if g % i == 0:
            count += 1 
    return count

def cm(a, b):
    return sum(gcd(a,b)%i == 0 for i in range(1, gcd(a,b)+1))
print(cm(12,18))

        