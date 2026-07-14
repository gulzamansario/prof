# 1. Write a program to store seven fruits in a list entered by the user.
# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner.
# 3. Check that a tuple type cannot be changed in python.
# 4. Write a program to sum a list with 4 numbers.
# 5. Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)



# 1. Write a program to store seven fruits in a list entered by the user.
# array = []
# for i in range(7):
#     fruit =input("Enter your fruit name : ")
#     array.append(fruit)
#     print(array)



# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner.
# stuData = []
# for s in range(6):
#     student_name = float(input(f"{s+1} student marks: "))
#     stuData.append(student_name)
# stuData.sort()
# print(stuData)


# 3. Check that a tuple type cannot be changed in python.

# tup = (12,12,34,45,67)
# tup[3] = 123
# print(new_tup)    yes outPut is actually TypeError so avoid it's immutable
#```out put was ```
'''  File "d:\Gul softwares\day-10-07-2026\exercise_3.py", line 33, in <module>
    tup[3] = 123
    ~~~^^^
TypeError: 'tuple' object does not support item assignment '''



# 4. Write a program to sum a list with 4 numbers.
numbers = [1, 2, 2, 2]
print(sum(numbers))


# 5. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
