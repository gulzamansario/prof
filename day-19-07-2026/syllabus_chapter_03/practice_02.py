# Return the index of the character to remove to make the string a palindrome.

def g_index(s):
    def is_p_i(left, right):
        while left < right:
            if s[left]!= s[right]:
                return False 
            left+=1
            right-=left
        return True
    left = 0
    right = len(s)-1
    while left < right:
        if s[left]==s[right]:
            left += 1
            right-= 1
        if is_p_i(left+1, right):
            return left 
        if is_p_i(left, right-1):
            return right
        else:
            return f"No index possible or already palindrome"
    return f"No any index possibe"
st = "aaab"
st2 = g_index(st)
print(st2)