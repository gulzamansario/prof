# 4. **Preorder traversal likho**
#    Same tree ka preorder output nikaalo.
# Preorder = root ==> left ===> right 
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}


stack = [1]

while stack:
    node =stack.pop()
    print(node, end="")

    if len(tree[node])>0:
        left = tree[node][0]
    else:
        left = None
    if len(tree[node]) > 1:
        right = tree[node][1]
    else:
        right = None
   
    if left:
        stack.append(left)
    if right:
        stack.append(right)