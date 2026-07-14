# 1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.
# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# 3. Write a program to detect double space in a string.
# 4. Replace the double space from problem 3 with single spaces.
# 5. Write a program to format the following letter using escape sequence
# characters.
# letter = "Dear Harry, this python course is nice. Thanks!"


# 1. Write a python program to display a user entered name followed by "Good Afternoon" using input () function.


name = input("what's your name: ")
print(f"Good afternoon {name}")


# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

from datetime import datetime

now = datetime.now().strftime("%d-%m-%Y")
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
letter1 = letter.replace("<|Date|>", now)
letter2 = letter1.replace("<|Name|>", name)
print(letter2)


# 3. Write a program to detect double space in a string.

st = "hello jani how are you is your code working or not bro  "
if st.find("  "):
    print(f"Double space Detected at index {st.find("  ")}")
else:
    print("Still we are finding the spaces")


new_st = st.replace("  ", " ")

print(new_st)



# 5. Write a program to format the following letter using escape sequence
# characters.


letter = "Dear Gul zaman,\n this python course is nice.\n Thanks!"
print(letter)


