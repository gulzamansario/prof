# finding the one
var1 = "we are preparing1 for proficiency"
#defining the varible where we will store the target character 
text = ""
number = ""
# target character that we want to apply 
ch = "1"
if ch in var1:
    #adding this because character is int
    if ch.isdigit():
        number += ch
    else:
        text += ch
print(text)
print(number)
   
