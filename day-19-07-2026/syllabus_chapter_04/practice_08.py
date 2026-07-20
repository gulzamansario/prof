# ## Q6 (Medium) – PIN Validator

# A valid PIN:

# * Exactly **6 digits**
# * No letters
# * No special characters

# **Input**

# ```text
# "123456"
# ```

# **Output**

# ```text
# True
# ```

def isValidPin(p):
    for ch in p:
        if not ch.isdigit():
            return False 
    if 6 <= len(p):
        return True
    else:
        return False
pin2 = input("Enter the pin ")

pin = isValidPin(pin2)
print(pin)