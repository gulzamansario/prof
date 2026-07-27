# 9. **Diagonal traversal without class, without function**
#    Loop aur stack/list use karke diagonals nikaalo.
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [None, None],
    4: [None, None],
    5: [None, None]
}

root = [1]
while root:
    node = root.pop(0)
    print(node, end="")
    left = tree[node][0]
    right =  tree[node][1]  
    if left:
        root.append(left)
    if right:
        root.append(right)