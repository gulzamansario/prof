# # def binary_search(arr, number):
# #     arr = [2, 3, 4, 6, 7, 8, 9]
# #     left = 0
# #     right = len(arr)-1
# #     middle = (left + right) //2 
# #     if arr[middle] == number:
# #         return f"index: {middle} value: {arr[middle]}"
# #     elif number < left:
# #         middle += right+1
# #     elif number > left:
# #         middle += left+1
# #     return f"{number} not found in {arr}"

# # li = [12, 34, 4, 5, 6, 89, 0]
# # target=34
# # print(binary_search(li, target))


# def binary_search(arr, number):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         middle = (left + right) // 2

#         if arr[middle] == number:
#             return middle

#         elif arr[middle] < number:
#             left = middle + 1

#         else:
#             right = middle - 1
#     return f"{number } not Found in {arr}"
# li = [12, 34, 4, 5, 6, 89, 0]
# target=34
# print(binary_search(li, target))



















# binary search algoriths

def binary_s(arr, target):
    left = 0 # list ka sab se pehla word means ndex 0 left me 
    right = len(arr)-1 # right me list ka sab se bara word means index last one
    while left <= right: #  agar list empty nhe hai to loop chalao 
        middle = (left + right) // 2
        if arr[middle] == target:  # agar middle index ka value target ki barabar hai to hamy wohy middle index do 
            return middle  #middle ko pass kar dena hum khud kise memory me daly gy 
        elif arr[middle] < target:  # agar middle ki value target se chuty hai 
            left = middle + 1      # left ko avoid karo aur usko bhe right ki pass leAao
        else:
            right = middle -1 # agar chuty hai to right ko khatam kardo
    return f"{target} not found in the {arr}" # jo word aap search kr rahe hai wo array main nahe hai 
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = 8
print(binary_s(li, number))


# code is working jab bhe apko value chayea to apko variable array main pass karna hoga example 
print(li[binary_s(li, number)])




# same operations with in build methods 
import bisect 

