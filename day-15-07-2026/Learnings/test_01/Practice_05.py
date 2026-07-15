rows = 11
for i in range (rows):
    if i <= rows // 2:
        stars = i + 1
    else:
        stars = rows - i

    spaces = abs(rows // 2 - i)

    print(" " * spaces, end="")

    for j in range(stars):
        print("*", end=" ")
    
    print()