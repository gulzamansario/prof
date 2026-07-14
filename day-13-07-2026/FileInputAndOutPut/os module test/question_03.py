# automatic note creator 
import os 

folder = "notes"

if not os.path.exists(folder):
    os.mkdir(folder)

for i in range(1, 11):
    note = os.path.join(folder, f"notes{i}.txt")

    with open(note, "w") as f:
        f.write(f"This is our note number {i} ")
