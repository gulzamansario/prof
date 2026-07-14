def new_fact(n):
    if n == 1 or n ==0:
        return 1 
    else:
        return n * new_fact(n-1)
    

li = [2, 3, 4, 5, 6, 7, 8, 9,]
l = [c * new_fact(c -1) for c in li]
print(l)
total_sum = sum(l)
print(total_sum)