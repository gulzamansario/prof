# basic 
# questions map
# 1. Write a python program to add two numbers.
# 2. Write a python program to find remainder when a number is divided by z.
# 3. Check the type of variable assigned using input () function.
# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than
# ‘b’ or not. Take a = 34 and b = 80
# 5. Write a python program to find an average of two numbers entered by the user.
# 6. Write a python program to calculate the square of a number entered by the user.

# create a python program to add 2 numbers safely 

def add(a, b):
    return (a+b)
   
    

sum = add(12,34)
print(sum)


# write a python program to find the reminder when it is divided by Z and do the debugging safely

z = 60

def getreminder(i):
    z = 60
    return i%z
ReminderOfZ = getreminder(z)
print(ReminderOfZ)
    

# check the type of the varible assignrdd with the input()
var = input("Enter the word: ")
print(f"Type of the {var} in the memory location is {type(var)}")




# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than
# ‘b’ or not. Take a = 34 and b = 80

a = 34
b = 80
if a > b:
    print(f'yes {a } is greater than {b} ')
else:
    print(f'No! {a} is not greater than {b} ')



# 5. Write a python program to find:
# an average of two numbers entered by the user.

def avg(a, b):
    return (a+b)/2
a = int(input("Enter your number 1: "))
b = int(input("Enter your number 2: "))
avgx = avg(a, b)
print(avgx)


# 6. Write a python program to calculate the square of a number entered by the user.

def sqr(a):
    print(f"Square of the number:=> {a} is => {a*a}")
c = int(input("Enter the number: "))
sqr(c)