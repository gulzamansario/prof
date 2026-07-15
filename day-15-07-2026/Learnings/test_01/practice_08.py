# ## Q9. Remove Duplicate Characters

# Example:

# ```
# Input:

# programming

# Output:

# progamin
# ```

st = "programming"
stack=[]
for chr in st:
    if chr not in st:
        stack.append(chr)
    else:
        stack.pop()
result = "".join(stack)
print(result)
