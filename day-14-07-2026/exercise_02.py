# 1. You are given a string containing character  A & B only.

# TASK
# change into strings 
# there should be no matching adjecent character 
# Allowed to Add Zero or more charcter in the strings 


a = "Gul"
b = "zaman"
con = a + b
for i in con:
    li = [c for c in con if c != i]
a = li[0:3]
b = li[3:]
st1 = "".join(b).strip()
st2 = "".join(a).strip()
print(st1, st2)

