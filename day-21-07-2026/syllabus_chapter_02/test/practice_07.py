# ### Q7. Sum of Common Divisors

# Write a function that returns the **sum** of all common divisors of two numbers.

# **Example**

# ```
# Input:
# 12 18

# Output:
# 12
# ```

# **Explanation**

# ```
# 1 + 2 + 3 + 6 = 12
# ```

# ---
from math import gcd
def ret_com_div_sum(a, b):
    sum = 0
    g = gcd(a, b)
    for i in range(1, g+1, 1):
        if g % i == 0:
            sum+=i
    return sum
print(ret_com_div_sum(12, 18))
