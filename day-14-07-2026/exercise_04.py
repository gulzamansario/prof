# Salman joined the network site to stay touch in them 
# Authentications [name, password]
# We have to set the criteria of the password folloeings 

#1. Length should be 15-30
#2. at least one digit
#3. at least one lower English character 
#4. at least one upper English character
#5. it contains at least one special character


# Defining requirements variables
chrt1= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chrt2 = chrt1.lower()
digi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
spcl = "!@#$%^&*()?|><"

# getting iterations
for Uch in chrt1:
    pass
for Lch in chrt2:
    pass
for n in digi:
    pass
for spl in spcl:
    pass

password = input("Enter your password: ")
print(len(password))
if len(password) != 15 and Uch not in password and Lch not in password and str(n) not in password and spl not in password:
    print("Password Criteria mathced Congrats")
    print(f"Uch: {Uch} Lch: {Lch} Len: {len(password)} number: {n} spl: {spl}")
    
    
else:
    print("Done Criteria not matched the password Try Again")


   
