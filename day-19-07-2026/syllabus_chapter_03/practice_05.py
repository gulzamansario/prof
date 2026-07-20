# ## Q5 (Medium)

# One character in the middle is wrong.

# ```
# Input:
# "abca"

# Expected:
# Return the correct index.
# ```

# ---

def Wch(s):
    def is_correct(left, right):
        while left < right:
            if s[left]!=s[right]:
                return False 
            left += 1
            right -= 1
        return True
    left = 0
    right = len(s)-1
    while left < right:
        if s[left]==s[right]:
            left += 1
            right -= 1
        else:
            if is_correct(left+1, right):
                return left
            if is_correct(left, right-1):
                return right
            else:
                return -1
    return True
    return -1

st = "radayr"
st2 = Wch(st)
print(st2)