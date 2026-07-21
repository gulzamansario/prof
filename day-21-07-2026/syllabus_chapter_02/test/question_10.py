# Mentah and Balaj both participated in five different contests.

# Their scores are stored in two lists.

# ```
# Mentah = [12, 18, 24, 30, 36]

# Balaj  = [18, 24, 30, 42, 48]
# ```

# For every pair of scores at the same index, calculate the number of common divisors and return the result in a new list.

# **Example Output**

# ```
# [4, 8, 8, 4, 6]

from math import gcd
def common_divisor(a, b):
    g = gcd(a, b)
    count = 0
    for i in range(1, g +1):
        if g % i == 0:
            count+=1
    return count

Mentah = [12, 18, 24, 30, 36]
Balaj  = [18, 24, 30, 42, 48] 
result = []
for a, b in zip(Mentah, Balaj):
    result.append(common_divisor(a, b))
print(result)

