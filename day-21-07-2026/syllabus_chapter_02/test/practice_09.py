# ### Q9. HCF of Multiple Numbers

# Write a function that accepts **three integers** and returns their Highest Common Factor (HCF).

# **Example**

# ```
# Input:
# 24 36 60

# Output:
# 12
# ```
# from math import gcd
# def hcf_three(a, b, c, ):
#     return gcd(gcd(a, b), c)
# print(hcf_three(24, 36, 60))



from math import gcd
def m_r(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result
print(m_r(12,34, 56, 78, 90, 45, 57, 34, 23, 26,))