# ## Q4 (Easy-Medium) – Special Character Checker

# Return `True` if the string contains **at least one special character**.

# **Example Special Characters**

# ```
# ! @ # $ % ^ & * ( ) _ + - =
# ```

# **Input**

# ```text
# "Hello@123"
# ```

# **Output**

# ```text
# True
# ```

# ---

def isU(st):
    isUp = True
    noUp = False
    for ch in st:
        if  not ch.isalnum():
            return isUp
    return noUp
st = input("Enter Any word:- ")
print(isU(st))
