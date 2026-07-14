import os 

path = input("Enter Your file path: ")

largest = "" 
size = 0

for file in os.listdir(path):
    if os.path.isfile(file):
        full = os.path.join(path, file)
        current = os.path.getsize(full)
        if current > size:
            size = current
            largest = file
print(f"The larget file is {largest}")
print(f"the largest size is {size}")
