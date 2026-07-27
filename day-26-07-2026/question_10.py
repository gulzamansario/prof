# 10. **Diagonal traversal ko recursive aur iterative dono way me karo**
#     Same tree ke liye 2 solutions banao aur compare karo.
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

    left, right = tree[node][0], tree[node][1]
    if left:
        root.append(left)
    if right:
        root.append(right)


def Iter_Dig(root):
    diagonal = []
    while root:
        node = root.pop(0)
        diagonal.append(node)

        left, right = tree[node][0], tree[node][1]
        if left:
            root.append(left)
        if right:
            root.append(right)

    for d in diagonal:
        print(d, end="")

Iter_Dig(tree[1])