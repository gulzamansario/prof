next_node = {
    1: 2,
    2: 3,
    3: 4,
    4: 5
}

head = 1
slow = head
fast = head

found = False

while fast in next_node and next_node[next_node[fast]] in next_node:
    slow = next_node[slow]
    fast = next_node[next_node[fast]]

    if slow == fast:
        found = True
        break
if found:
    print("Loop found")
else:
    print("Not Found!")