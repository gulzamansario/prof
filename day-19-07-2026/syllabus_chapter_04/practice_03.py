# Q2 (Easy) – Contains an Uppercase Letter
# Return True if the string contains at least one uppercase letter.

def isU(st):
    isUp = True
    noUp = False
    for ch in st:
        if ch.isupper():
            return isUp
        else:
            return noUp
st = input("Enter Any word:- ")
print(isU(st))