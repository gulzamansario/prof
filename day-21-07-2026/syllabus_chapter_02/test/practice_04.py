# ### Q4. Print Common Divisors

# Instead of counting them, print all common divisors of two numbers in ascending order.

# **Example**

# ```
# Input:
# 20 30

# Output:
# 1
# 2
# 5
# 10
# ```

# ---

from math import gcd
def common_divisor(a, b):
    g = gcd(a, b)
    
    for i in range(1, g+1):
        if g % i == 0:
            print(sorted(i))
print(common_divisor(12, 48))