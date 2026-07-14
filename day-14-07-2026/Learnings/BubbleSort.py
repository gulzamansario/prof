# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n = [2, 0, 9, 6, 7,]
#         n = len(nums)

#         for i in range(n):
#             isSwap = False
#             for j in range(n-i-1):
#                 if nums[j]>nums[j+1]:
#                     #swap 
#                     temp = nums[j]
#                     nums[j]=nums[j+1]
#                     nums[j+1]=temp
#                     isSwap = True
#             if not isSwap:
#                 break
#         return nums
# new_main = Solution()
# nums = [2, 0, 9, 6, 7,]
# sort_num = new_main.sortArray(nums)
# print(sort_num)

# # def swap(a, b):
# #     temp = b
# #     b = a
# #     a = temp
# #     return a, b 
# # sw = swap(3,4)
# print(sw)




def sortArray(nums):
    n = len(nums)
   
    for i in range(n):
        isSwap = False
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                isSwap = True
        if not isSwap:
            break
    return nums

list1 = [23, 56, 45, 453, 534, 123, 456456, 564564, 0, 35, ]
list2 = sortArray(list1)


print(f"Builtin Result {sorted(list1)}\n Custome Result {list2}")