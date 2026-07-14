# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 



with open("poems.txt", "r") as f:
    textContent = f.read()
    print(textContent)
    if "twinkle" in textContent:
        print("Yes Twinkle exist")
    else:
        print("Twinkle is not there")
    
