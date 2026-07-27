tree = {
    1: [2, 3],
    2: [4, 5],
    3: [None, None],
    4: [None, None],
    5: [None, None]
}


queue = [1]
while queue:
    node = queue.pop()
    print(node, end="")

    left = tree[node][0]
    right = tree[node][1]

    if left:
        queue.append(left)
    if right:
        queue.append(right)