# 10. Pangram Checker

# Problem Understanding:
# Determine if a string contains every letter of the English alphabet (26 letters), ignoring case.

# Approach:

# · Convert string to lowercase (or uppercase)
# · Create a set of letters in the string
# · Check if the set contains all 26 letters


st = '''"How Does the Print Function Work?
Every programming language has some way to output data to the terminal with a built-in method, function, property, or keyword. In Python, you can use the print function to print data to the terminal. Let's take a closer look at the print function so you can start using it with confidence.

One of the first things you do when you're learning any programming language is to write a simple Hello world! program. You can do that really easily in Python with just the print function.

To do that, you just need to put the string Hello world! in between the opening and closing parentheses you use to call the print function:

print('Hello world!') # Hello world!
You will learn more about strings and functions in Python in future lessons. For now, just consider strings as a sequence of characters surrounded by either single (') or double (") quotation marks.

In the print('Hello world!') example, the string 'Hello world!' is an argument passed to the print function. You can also use the print function to show multiple values, or arguments, at once by separating them with commas. For example:

print('My favorite colors are', 'blue', 'green', 'red')

# Output: My favorite colors are blue green red
Python automatically adds a space between each item when you separate them with commas. This is helpful when you want to print several pieces of information together.

Questions

Why does the following code print all the values on the same line with spaces?

print('My favorite colors are', 'blue', 'green', 'red')

Because separating values with commas in print() adds spaces between them.

Because strings are automatically joined together with no separator.

Because each call to print() adds a space by default.

Because Python automatically converts all strings to uppercase in output.

What would the output of the following code be?

print('Hello', 'world!')

Hello world!

Helloworld!

Hello, world!

Hello\nworld!

What is the purpose of the quotation marks around Hello world! in the following code?

print('Hello world!')

They define a string to be printed by the print() function.

They are used to call a function named Hello world!.

They are required only if the string contains spaces.

They let Python know to print a variable named Hello world!.
Check your answer
Ask for Help'''
az = "abcdefghijklmnopqrstuvwxyz"
new_st = st.lower()
chr_arr = []
for ch in new_st:
    if ch in az:

        chr_arr.append(ch)
        new_tup = set(chr_arr)
if len(new_tup) == 26:
    print(len(new_tup))
    print("Yes Strings contains A-Z characters ")
else:
    print(len(new_tup), sorted(new_tup))
    print("Not strings didn't cotains A_Z")
