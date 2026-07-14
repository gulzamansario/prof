# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. 
# Place these files in a folder for a 13 – year old. 



import os

# Folder ka naam
folder = "Tables for 13-year old"

# Agar folder nahi hai to bana do
if not os.path.exists(folder):
    os.mkdir(folder)

# 2 se 20 tak tables
for i in range(2, 21):

    filename = os.path.join(folder, f"table_{i}.txt")

    with open(filename, "w") as f:

        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")

print("All tables created successfully!")
       
