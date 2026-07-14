





smallest = float('inf')
second = float('inf')
arr = [12, 45, 2, 3, 4, 1, 9, 0]
for num in arr:
    print(num)
   # 12 45 2 3 4 1 9 0 
    if num < smallest:
        print(num)
        second = smallest
        smallest = num
    elif num != smallest and num < second:
        second = num
        print(second)
        break
    # if second == float('inf'):
    #     return "No Second Smallest"
