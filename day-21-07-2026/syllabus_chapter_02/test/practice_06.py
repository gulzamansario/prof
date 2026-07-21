# ### Q6. Are They Co-prime?

# Two numbers are called **co-prime** if their GCD is **1**.

# Write a function that returns:

# ```
# True
# ```

# if the numbers are co-prime, otherwise

# ```
# False
# ```

# **Example**

# ```
# Input:
# 8 15

# Output:
# True
# ```

# ---
from math import gcd
def isCprime(a, b):
    g = gcd(a, b)
    if g == 1:
        return True
    else:
        return False
print(isCprime(12, 6))
    

    
