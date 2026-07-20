# ## Q9 (Hard) – Character Counter

# Given a string, return:

# * Number of uppercase letters
# * Number of lowercase letters
# * Number of digits
# * Number of special characters

# **Input**

# ```text
# "Usman@123"
# ```

# **Output**

# ```text
# Uppercase: 1
# Lowercase: 5
# Digits: 3
# Special: 1
# ```

# ---

def getStr(e):
    Dc = 0
    uLc = 0
    ScC = 0
    Llc = 0


    for ch in e:
        if ch.isdigit():
            Dc+=1
        elif ch.islower():
            Llc+=1
        elif ch.isupper():
            uLc+=1
        elif not ch.isalnum():
            ScC+=1
    return f"Digits are {Dc}\nLower case letters are {Llc}\nUpper case letter are {uLc}\nSpecial characters are {ScC}"


us = "Usman@123"
print(getStr(us))