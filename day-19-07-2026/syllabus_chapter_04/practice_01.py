def strong(p):
    return (15 <= len(p) <= 30 and any(c.islower() for c in p) and any(c.isupper() for c in p) and any(c.isdigit() for c in p) and any(c.isalnum() for c in p) )
print(strong("Usman@123456789"))      # True
print(strong("password"))             # False
print(strong("PASSWORD123"))          # False