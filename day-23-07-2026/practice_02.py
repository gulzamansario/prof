# 9. Count Words in Camel Case String

st = "Every programming language has some way to output data to the terminal with a built-in method, function, property, or keyword. In Python, you can use the print function to print data to the terminal. Let's take a closer look at the print function so you can start using it with confidence."
count = 0
for i, ch in enumerate(st):
    if ch.isupper():
        count+=1
    else:
        pass
print(count)