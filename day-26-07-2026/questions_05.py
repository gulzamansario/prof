tree = {
    1: [2, 3],
    2: [4, 5],
    3: [None, None],
    4: [None, None],
    5: [None, None]
}

stack = []
current = 1
while stack or current:
    while current:
        stack.append(current)
        current = tree[current][0]
    current = stack.pop()
    print(current, end="")

    current = tree[current][1]




    