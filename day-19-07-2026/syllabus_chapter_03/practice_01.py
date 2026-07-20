# Write a function that checks whether a string is a palindrome using the two-pointer approach.


def is_palim(st):
    left = 0
    right = len(st)-1
    while left < right:
        if st[left]!=st[right]:
            return False
        left += 1
        right -= 1
    return True
st = "radar"
st2 = is_palim(st)
print(st2)