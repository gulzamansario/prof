# 8. Second Smallest Number in Array
arr = [12, 12, 12, 5, 2, 20]
arr = sorted(set(arr))

if len(arr) < 2:
    print("No second smallest")
else:
    print(arr[1])

