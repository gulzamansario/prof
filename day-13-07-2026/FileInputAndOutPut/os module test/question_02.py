# files extension counter 
import os 

path = input("Enter your path: ")
txt=py=pdf=other=0
for file in os.listdir(path):
    print(file)
    ext = os.path.splitext(file)[1]
    if ext == ".txt":
        txt+=1
    elif ext == ".py":
        py+=1
    elif ext == ".pdf":
        pdf+=1
    elif ext == "other":
        other+=1
    else:
        continue
print(f"{txt}\n {py} \n {pdf} \n {other} ")