
# 1. Write a program to create a dictionary of Urdu words with values as their English
# translation. Provide user with an option to look it up!
# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).
# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
# 5. s = {}
# What is the type of 's'?
# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
# 7. If the names of 2 friends are same; what will happen to the program in problem
# 6?
# 8. If languages of two friends are same; what will happen to the program in problem
# 6?
# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}



# 1. Write a program to create a dictionary of Urdu words with values as their English

dic = {
    "tum": "you",
    "Kia hall hai?": "how are you?",
    "are you bad?": "Kia aap bury ho "
}
print(dic)

# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).
# e = set()
# for q in range(8):
#     num = int(input("Enter your number: "))
#     e.add(num)
# print(e)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

new = {'hello', 'n', 'v', 't', 'y', 'u', 'i', 'o', 's', 'a', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 12, 2, 34, 45, 56, 67, 78, 89, 45, 34, 12, 23, 45, 67, 78, 89, 89, 45}
print(new)

# yes there is new named set 


# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') 
print(s)
# length will be the 2 because there are diffrent by the type but int float remain same
# # length of s after these operations?

t = {}
# What is the type of 't'?  # type will be the empty dictionary not set
print(type(t))    # output is ===> <class 'dict'>
# 6. Create an empty dictionary. 
# Allow 4 friends to enter their favorite language as
# value and use key as their names.
# Assume that the names are unique.

dt = {}
dt.update(
    {"anwar": "python"}
   

    
    )
dt.update( {"Afsha": "c++" })
dt.update( {"nimra": "arabic"})
dt.update(  {"nimra": "English"})

print(dt)



# 7. If the names of 2 friends are same; 
# what will happen to the program in problem 6?

#  first name is being updated and replaced previous one

sxt = {}
sxt.update(
    {"anwar": "python"}
    )
sxt.update( {"Afsha": "c++" })
sxt.update( {"nimra": "arabic"})
sxt.update(  {"nimra": "English"})
print(sxt)



# 8. If languages of two friends are same; what will happen to the program in problem
# 6?   
#  with no issue and 0 error programs runs in the python

fxt = {}
fxt.update(
    {"anwar": "python"}
    )
fxt.update( {"Afsha": "c++" })
fxt.update( {"nimra": "English"})
fxt.update(  {"rehan": "English"})
print(fxt)




# No

# You cannot change the values inside a list contained in a set because sets can only contain immutable (hashable) objects and a list is mutable (unhashable In fact, this set itself is invalid:

# 
# s = {8, 7, 12, "Harry", [1, 2]}
# 

# It will raise:

# 
# TypeError: unhashable type: 'list'
#

# Simple answer No
