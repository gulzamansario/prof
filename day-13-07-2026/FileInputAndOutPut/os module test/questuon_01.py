# Ek folder ka path user se lo aur us folder mein total kitni files aur kitne folders hain, print karo.

import os 
path = input("Enter your path:")
files = 0
folder = 0
for item in os.listdir(path):
    full_path= os.path.join(path, item)
    if os.path.isdir(full_path):
        folder+=1
    elif os.path.isfile(full_path):
        files+=1
print(folder)
print(files)
