from random import randint
while True:
    print(" 1. SNAKE \n 2. WATER \n 3. GUN")
    robot = randint(1,3)
    try:
        user = int(input("Enter a Number: "))
    except KeyError as k:
        print(f"something went wrong {k}")
        break
    dict = {
        1: "Snake",
        2: "Water",
        3: "Gun"
        }
    userNum = dict[user]
    robotNum = dict[robot]
    print(f"Your choice is {userNum} robot choice is {robotNum}")
    if userNum == robotNum:
        print("Game Got Draw!")
        continue
    elif userNum == "Gun" and robotNum =="Snake":
        print("User win the Game")
        break
    elif userNum == "Snake" and robotNum =="Gun":
        print("Robot win the Game")
        break
    elif userNum == "water" and robotNum =="Snake":
        print("Robot win the Game")
        break
    elif userNum == "Snake" and robotNum =="Water":
        print("User win the Game")
        break
    elif userNum == "Gun" and robotNum =="Water":
        print("User win the Game")
        break
    elif userNum == "Water" and robotNum =="Gun":
        print("Robot win the Game")
        break
    else:
        print("Something went Wrong")
        continue
    
     
    
