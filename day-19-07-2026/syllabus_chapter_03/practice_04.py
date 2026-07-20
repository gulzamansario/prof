# ## Q4 (Medium)

# The string is already a palindrome.

# ```
# Input:
# "racecar"

# Output:
# -1
# ``

# st = "radarr"
# if st[::-1]==st:
#     print(f"{st} is a palindrome")
# else:
#     print(f"{st} not a palindrome")


def is_palim(st):
    left = 0
    right = len(st)-1
    while left < right:
        if st[left]==st[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

st = "ra4dar"
print(is_palim(st))