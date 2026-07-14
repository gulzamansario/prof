# 3. How do you prevent a python 
# print() function to print a new line at the end. 


# editing built in functions so it should avoid the new line to print 

def my_print(text, end_char=""):
    __builtins__.print(text, end=end_char)


print("hello world ")