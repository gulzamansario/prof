# given a string of lowercase character in the range([a-z]) 
# find the index of the character 

#  that can be removed to make the strings a palindrome. 

# if word already a plaindrome or there is no solutions return -1
# finding charcter and remove that will not be palindrome
main = "abcdefghijklmnopqrstuvwxyz"
new_str = ""
for i in main:
    m = i
    if i == m[::-1]:
        new_str += i
    else:
        main -= i
print(f"Yes Palindrome str is {new_str} while non palindrome is {main}")





#  after many testing it is proven that all the charcters a-z are the palindrome