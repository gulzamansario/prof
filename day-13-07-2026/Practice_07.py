# 7. Write a python function to remove a given word from a list ad strip it at the same 
# time. 


def rmv(lis, n):
     return [item.strip() for item in lis if item.strip() != n]


lis = ["name", "farhan", "amjad", "faizan", "karan", "kamal"]

li = rmv(lis, "name")
print(li)
