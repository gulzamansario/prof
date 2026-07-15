# Q2. Remove Adjacent Same Characters Until Stable

st = "aaabccddd"

stack = []
for chr in st:
    right =st.__len__()


    if stack and stack[-1]  == chr:
        stack.pop()
    else:
        stack.append(chr)
result = "".join(chr)
print(result)