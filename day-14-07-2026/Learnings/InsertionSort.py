def InsertionSort(nums):
   
    n= len(nums)
    for i in range(1, n):
         key = nums[i]
         j = i-1
         while j >=0 and nums[j]>key:
              nums[j+1]=nums[j]
              j-=1
         nums[j+1] = key
    return nums


nums = [23, 2344445, 99, 89]
isq = InsertionSort(nums)
print(isq)