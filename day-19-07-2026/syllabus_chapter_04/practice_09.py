# ## Q7 (Medium) – Email Format Checker (Basic)

# Check whether a string contains:

# * One `@`
# * At least one `.` after `@`

# Don't use regex.

# **Input**

# ```text
# "user@gmail.com"
# ```

# **Output**

# ```text
# True
# ```

# ---

def isEmail(e):
    return "." in e and "@" in e
e = input("Enter the mail: ")
print(isEmail(e))