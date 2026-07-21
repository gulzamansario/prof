# ### Q2. Find the Greatest Common Divisor (Without Built-in Function)

# Write a function that takes two integers and returns their Greatest Common Divisor (GCD).

# **Restriction:**
# Do not use `math.gcd()`.

# **Example**

# ```
# Input:
# 24 36

# Output:
# 12
# ```

# ---

def gcd(M, B):
    while B != 0:
        M, B = B, M % B
    return M
print(gcd(24, 36))