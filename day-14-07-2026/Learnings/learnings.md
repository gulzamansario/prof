# Sorting Algorithms
### bubble sort
**Bubble sort sort the numbers one by one**
```markdown

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
```

**ASCENDING**
**DESCENDING**

# Insertion Sort
```markdown
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
```