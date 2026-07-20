# ## Q5 (Medium) – Username Validator

# A valid username:

# * Length between **5 and 15**
# * Only letters and digits
# * No spaces
# * No special characters

# Return `True` or `False`.

# **Input**

# ```text
# "Usman123"
# ```

# **Output**

# ```text
# True
# ```

def isvalid(username):
    for ch in username:
        if not ch.isalnum():
            return False
            
    if (5<= len(username) <= 15 and any(c.isalnum() for c in username)):
        return True
    elif username:
        return False
st = input("Enter the userName: ")
st2 = isvalid(st)
print(st2)

