# find the Sum of All Palindromic numbers from 1, 100

def is_palindrome_number(num):
    # Negative numbers are not palindromes by definition
    if num < 0:
        return False

    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10               # Get last digit
        reversed_num = reversed_num * 10 + digit
        num //= 10                     # Remove last digit

    return original == reversed_num
lis = []
for i in range(1, 101, 1):
    if is_palindrome_number(i) ==True:
        lis.append(i)
    else:
        pass

sum_of_palindrome_is = sum(lis)
print(sum_of_palindrome_is)
