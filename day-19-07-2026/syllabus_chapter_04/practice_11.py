
# ## Q10 (Interview Level) – Strongest Password

# Return:

# * `"Weak"`
# * `"Medium"`
# * `"Strong"`

# Rules:

# **Weak**

# * Length < 8

# **Medium**

# * Length ≥ 8
# * Contains letters and digits

# **Strong**

# * Length ≥ 15
# * Uppercase
# * Lowercase
# * Digit
# * Special character

# **Example**

# Input

# ```text
# Python@123456789
# ```

# Output

# ```text
# Strong
# ```

# ---
def check_level(p):
    if 8 > len(p):
        return f"{p}: is Weak"
    elif 8 <= len(p) and p.isalnum():
        return f"{p}: is Medium"
    else:
        return f"{p}: is strongest"
p = input("Enter the password: ")
print(check_level(p))