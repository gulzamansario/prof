import os
import glob

# Delete existing practice_*.py files
for file in glob.glob("practice_*.py"):
    os.remove(file)
    print(f"Deleted: {file}")

solutions = {
    "practice_01.py": '''import math

N = 5

total = 0

for i in range(1, N + 1):
    total += math.pow(i, 2)

print(int(total))
''',

    "practice_02.py": '''import math

N = 4

total = 0

for i in range(1, N + 1):
    total += math.pow(i, 3)

print(int(total))
''',

    "practice_03.py": '''import math

X = 30
N = 2

i = 1

while math.pow(i, N) <= X:
    print(i, end=" ")
    i += 1
''',

    "practice_04.py": '''import math

X = 64
N = 3

root = round(math.pow(X, 1 / N))

if math.pow(root, N) == X:
    print("Yes")
else:
    print("No")
''',

    "practice_05.py": '''import math

def solve(x, n, i=1):
    if x == 0:
        return True

    if math.pow(i, n) > x:
        return False

    return solve(x - int(math.pow(i, n)), n, i + 1) or solve(x, n, i + 1)

print(solve(17, 2))
''',

    "practice_06.py": '''import math

def ways(x, n, i=1):
    if x == 0:
        return 1

    if math.pow(i, n) > x:
        return 0

    return ways(x - int(math.pow(i, n)), n, i + 1) + ways(x, n, i + 1)

print(ways(100, 2))
''',

    "practice_07.py": '''import math

def show(x, n, i=1, path=[]):
    if x == 0:
        print(path)
        return

    if math.pow(i, n) > x:
        return

    show(x - int(math.pow(i, n)), n, i + 1, path + [i])
    show(x, n, i + 1, path)

show(17, 2)
''',

    "practice_08.py": '''import math

best = None

def solve(x, n, i=1, path=[]):
    global best

    if x == 0:
        if best is None or len(path) < len(best):
            best = path
        return

    if math.pow(i, n) > x:
        return

    solve(x - int(math.pow(i, n)), n, i + 1, path + [i])
    solve(x, n, i + 1, path)

solve(100, 2)

print(best)
''',

    "practice_09.py": '''import math

best = []

def solve(x, n, i=1, path=[]):
    global best

    if x == 0:
        if len(path) > len(best):
            best = path
        return

    if math.pow(i, n) > x:
        return

    solve(x - int(math.pow(i, n)), n, i + 1, path + [i])
    solve(x, n, i + 1, path)

solve(100, 2)

print(best)
''',

    "practice_10.py": '''import math

def ways(x, n, i=1):
    if x == 0:
        return 1

    if math.pow(i, n) > x:
        return 0

    return ways(x - int(math.pow(i, n)), n, i + 1) + ways(x, n, i + 1)

X = 100
N = 2

print(ways(X, N))
'''
}

for filename, code in solutions.items():
    with open(filename, "w", encoding="utf-8") as file:
        file.write(code)
    print(f"Created: {filename}")

print("\n✅ All 10 practice files created successfully.")