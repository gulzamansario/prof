# Q8 (Medium-Hard) – Password Strength Checker
# A password is valid if it contains:

# 12–20 characters
# One uppercase
# One lowercase
# One digit
# One special character
# Return True or False.

def st_check(p):
    if (12 <= len(p) <= 30 and any(c.islower() for c in p ) and any(c.isupper() for c in p) and any(c.isdigit() for c in p) and any(not c.isalnum() for c in p) ):
        return True
    else:
        return False

p = input("Please Enter the password: ")
passw = st_check(p)
print(passw)