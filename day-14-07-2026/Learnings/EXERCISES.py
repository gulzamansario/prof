# 1. Second Smallest Distinct Number

def secondSmallest(arr):

    smallest = float('inf')
    second = float('inf')
    # arr = [12, 45, 2, 3, 4, 1, 9, 0]
    for num in arr:
    # 12 45 2 3 4 1 9 0 
        if num < smallest:
            second = smallest
            smallest = num

        elif num != smallest and num < second:
            second = num
            print(second)
            break

    if second == float('inf'):
        return "No Second Smallest"

    return second


arr = [5,2,8,1,3]
print(secondSmallest(arr))

# 2. Move All Zeros to End
def moveZeros(arr):

    result = []

    for num in arr:
        if num != 0:
            result.append(num)

    zeroCount = len(arr) - len(result)

    result.extend([0] * zeroCount)

    return result


arr = [0,1,0,3,12]

print(moveZeros(arr))


# 3. Left Rotate Array

def leftRotate(arr, d):

    n = len(arr)

    d = d % n

    return arr[d:] + arr[:d]


arr = [1,2,3,4,5]

print(leftRotate(arr,2))

# 4. Missing Number

# Formula Method

def missingNumber(arr):

    n = len(arr) + 1

    expected = n * (n + 1) // 2

    actual = sum(arr)

    return expected - actual


arr = [1,2,3,5,6]

print(missingNumber(arr))