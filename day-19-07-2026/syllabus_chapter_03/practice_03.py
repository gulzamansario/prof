# ## Q3 (Easy)

# Return the index of the character to remove.

# ```
# Input:
# "baa"

# Output:
# 0
# ```

def s_r_index(s):
    def c_index(left, right):
        while left < right:
            if s[left] != s[right]:
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
        if c_index(left+1, right):
            return left
        if c_index(left, right-1):
            return right
        else:
            return -1
    return -1

st = "baa"
st2 = s_r_index(st)
print(st2)
