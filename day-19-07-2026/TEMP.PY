
# Given the string "radar", what index can be removed to make it a palindrome? 
# If it is already a palindrome, return -1

st = "level"


def palindrome_index(s):
    def is_palindrome(left, right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) -1
    while left < right:
        if s[left]==s[right]:
            left += 1
            right-= 1
        if is_palindrome(left+1, right):
            return left
        if is_palindrome(left, right-1):
            return right
        else:
            return -1
    return -1

st2 = palindrome_index(st)
print(st2)