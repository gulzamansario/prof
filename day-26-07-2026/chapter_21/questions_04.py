tree = {
    1: [2, 3],
    2: [4, 5],
    3: [None, None],
    4: [None, None],
    5: [None, None]
}

find= int(input("Enter the number: "))
for tr in tree:

    if find == tr:
        print(f"Digit Found! {tr}")
        break
    else:
        pass

