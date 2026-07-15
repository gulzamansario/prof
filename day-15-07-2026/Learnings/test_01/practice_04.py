# ## Q4. Make String Alternating

# Given only A and B characters, remove minimum characters so that no adjacent characters are same.

# Example:

# ```
# Input:

# AAABBBA

# Output:

# ABABA
# ```

# ---

st = "AAABBBA"

result = st[0]
for i in range (1, len(st)):
    if st[i] != st[i - 1]:
        result += st[i]
print(result)

# stack = []
# for ch in st:
#     if stack and stack[-1] == ch:
#         stack.pop()
#     else:
#         stack.append(ch)
# print("".join(stack))

# st = "AAABBBA"
# len_str = len(st)

# stack = ""
# for a in range(0, len_str, 1):
#     if len(stack) == 0:
#         stack+=st[a]
#     if a <= len_str:







#   f stack[-1]== st[a-1]:

#         pass
#     elif stack[-1] == st[a+1]:
#         pass
#     else:
#         stack+=st[a]
# print(stack)
       
#     ch = st[a]
#     if stack != ch:
#         stack += ch
# print(stack)










#     # str_stack= "".join(stack)
#     if str_stack and ch[-1] == chr:
#         stack.pop()
#     else:
#         stack.append(chr)
# result = "".join(stack)
# print(result)