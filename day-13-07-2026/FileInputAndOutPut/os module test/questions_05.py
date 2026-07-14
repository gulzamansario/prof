import os
path = input("Enter Your path = ")
output = os.path.join(path, "combine.txt") 
with open(output, "w") as out:
    for files in os.listdir(path):
        if files.endswith(".txt") and files != "combine.txt":
            full = os.path.join(path, files )
            with open(full, "r") as f:
                       out.write(f"------{files}----\n")
                       out.write(f.read())
                       out.write("\n\n")
print("files merged successfully")


          
          
    