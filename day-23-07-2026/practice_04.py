# Problem Understanding:
# Given two arrays, find which elements in the second array are NOT present in the first array.


# · Array1: [1, 2, 3, 4, 5]
# · Array2: [2, 4, 6, 8]
# · Missing: [6, 8]

arr1 = [1, 2, 3, 4, 5, 6, 34,  7, 8,]
arr2 = [4, 6, 7, 34, 56, 78, ]
new_arr = []
for n in arr2:
    if n not in arr1:
        new_arr.append(n)
print(new_arr)