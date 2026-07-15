
def li_search(arr, number):
    li = len(arr)
    for i in range(li):
        if arr[i]==number:
            return arr[i]
    
    return f"Number: {number} Not found in {arr}"
li = [12, 34, 4, 5, 6, 89, 0]
target=34
print(li_search(li, target))