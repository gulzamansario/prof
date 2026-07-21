# ### Q5. Largest Common Divisor

# Write a program that returns the largest positive integer that divides both numbers.

# **Restriction**

# Do not use `math.gcd()`.

def lcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(lcd(12, 58))