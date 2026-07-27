tree = {
    1: [2, 3],
    2: [4, 5],
    3: [None, None],
    4: [None, None],
    5: [None, None]
}

stack1=[1]
stack2 = []
while stack1:
    node = stack1.pop()
    stack2.append(node)

    left = tree[node][0]
    right = tree[node][1]

    if right:
        stack1.append(right)
    if left:
        stack1.append(left)
while stack2:
    print(stack2.pop(), end="")

