def isU(st):
    isUp = True
    noUp = False
    for ch in st:
        if ch.islower():
            return isUp
        else:
            return noUp
st = input("Enter Any word:- ")
print(isU(st))