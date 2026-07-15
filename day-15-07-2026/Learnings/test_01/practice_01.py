# remove adject buplicate character 

st = "abbaca"
arr = []
for char in st:
    if arr and arr[-1] == char:
        arr.pop()
    else:
        arr.append(char)
result = "".join(arr)
print(result)



# (()()())   barckets check karo agar ( aye to add karo ) aye to remvoe karo 

st = "a(b(c)d)"

new_arr = []
for chr in st:
    if "(" in chr:
        new_arr.append(chr)
    else:
        pass
n_r = "".join(new_arr)
print(n_r)