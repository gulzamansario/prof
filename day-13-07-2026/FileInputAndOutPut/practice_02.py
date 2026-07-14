# /# # 2. The game() function in a program lets a user play a game and returns the score 
# # score whenever the game() functiaon breaks the Hi-score. 
# # as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# # contains the previous Hi-score. 
# # You need to write a program to update the Hi
# # # 2. The game() function in a program lets a user play a game and returns the score 
# # score whenever the game() functiaon breaks the Hi-score. 
# # as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# # contains the previous Hi-score. 
# # You need to write a program to update the Hi
# from random import randint
from random import randint 
def game():
    score = randint(1, 745843)
    return score

score = game()

try:
    with open("Hi-Score.txt.", "r")as f:
        content = f.read().strip()
        print(content)
        if content == "":
            hi_score = 0
        else:
            hi_score = int(content)
except FileNotFoundError:
    hi_score = 0
if score > hi_score:
    with open("Hi-Score.txt", "w") as f:
        f.write(str(score))
        print("High Score Saved")
else:
    print("No file was not have high score")

