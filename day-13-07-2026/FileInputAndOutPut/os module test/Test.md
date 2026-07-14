

# ✅ Question 1: Count Files & Folders

```python
import os

path = input("Enter folder path: ")

files = 0
folders = 0

for item in os.listdir(path):
    full_path = os.path.join(path, item)

    if os.path.isfile(full_path):
        files += 1
    elif os.path.isdir(full_path):
        folders += 1

print("Files:", files)
print("Folders:", folders)
```

---

# ✅ Question 2: File Extension Counter

```python
import os

path = input("Enter folder path: ")

py = txt = jpg = others = 0

for file in os.listdir(path):

    ext = os.path.splitext(file)[1]

    if ext == ".py":
        py += 1
    elif ext == ".txt":
        txt += 1
    elif ext == ".jpg":
        jpg += 1
    else:
        others += 1

print("Python Files:", py)
print("Text Files:", txt)
print("Images:", jpg)
print("Others:", others)
```

---

# ✅ Question 3: Automatic Notes Creator

```python
import os

folder = "Notes"

if not os.path.exists(folder):
    os.mkdir(folder)

for i in range(1, 11):

    filename = os.path.join(folder, f"note{i}.txt")

    with open(filename, "w") as f:
        f.write(f"This is note number {i}")

print("10 Notes Created!")
```

---

# ✅ Question 4: Largest File Finder

```python
import os

path = input("Enter folder path: ")

largest = ""
size = 0

for file in os.listdir(path):

    full = os.path.join(path, file)

    if os.path.isfile(full):

        current = os.path.getsize(full)

        if current > size:
            size = current
            largest = file

print("Largest File:", largest)
print("Size:", size, "Bytes")
```

---

# ✅ Question 5: File Merger

```python
import os

path = input("Enter folder path: ")

output = os.path.join(path, "combined.txt")

with open(output, "w") as out:

    for file in os.listdir(path):

        if file.endswith(".txt") and file != "combined.txt":

            with open(os.path.join(path, file), "r") as f:

                out.write(f"----- {file} -----\n")
                out.write(f.read())
                out.write("\n\n")

print("Files merged successfully.")
```

---

# ✅ Question 6: Duplicate File Name Detector

```python
import os

path = input("Enter folder path: ")

names = set()
duplicates = set()

for file in os.listdir(path):

    name = os.path.splitext(file)[0]

    if name in names:
        duplicates.add(name)
    else:
        names.add(name)

print("Duplicate Names:")

for item in duplicates:
    print(item)
```

---

# ✅ Question 7: Python Project Cleaner

```python
import os

path = input("Enter folder path: ")

count = 0

for file in os.listdir(path):

    if file.endswith(".pyc") or file.endswith(".log") or file.endswith(".tmp"):

        os.remove(os.path.join(path, file))
        count += 1

print("Deleted", count, "files")
```

---

# ✅ Question 8: Word Frequency Analyzer

```python
filename = input("Enter file name: ")

with open(filename, "r") as f:

    words = f.read().lower().split()

freq = {}

for word in words:

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for key in freq:
    print(key, ":", freq[key])

most = max(freq, key=freq.get)

print("Most repeated:", most)
```

---

# ✅ Question 9: Folder Backup Utility

```python
import os

folder = input("Enter folder path: ")

backup = os.path.join(folder, "Backup")

if not os.path.exists(backup):
    os.mkdir(backup)

for file in os.listdir(folder):

    if file.endswith(".txt"):

        with open(os.path.join(folder, file), "r") as f:
            data = f.read()

        with open(os.path.join(backup, file), "w") as b:
            b.write(data)

print("Backup completed.")
```

---

# ✅ Question 10: Mini File Search Engine

```python
import os

word = input("Enter word: ")

total = 0

for folder, subfolders, files in os.walk("."):

    for file in files:

        if file.endswith(".txt"):

            path = os.path.join(folder, file)

            with open(path, "r") as f:

                text = f.read()

                if word in text:
                    print(file)

                total += text.count(word)

print("Total occurrences:", total)
```

---

# ⭐ Bonus Challenge (Mini File Manager)

```python
import os

while True:

    print("\n1.List")
    print("2.Create")
    print("3.Delete")
    print("4.Rename")
    print("5.Read")
    print("6.Write")
    print("7.Exit")

    choice = input("Choice: ")

    if choice == "1":

        print(os.listdir())

    elif choice == "2":

        name = input("File Name: ")

        open(name, "w").close()

    elif choice == "3":

        name = input("File Name: ")

        os.remove(name)

    elif choice == "4":

        old = input("Old Name: ")
        new = input("New Name: ")

        os.rename(old, new)

    elif choice == "5":

        name = input("File Name: ")

        with open(name, "r") as f:
            print(f.read())

    elif choice == "6":

        name = input("File Name: ")

        text = input("Write: ")

        with open(name, "w") as f:
            f.write(text)

    elif choice == "7":

        print("Good Bye!")
        break

    else:

        print("Invalid Choice")
```

---

## 💡 Practice Tip

In 10 questions mein ye functions baar-baar use hue hain:

| Function             | Kitni baar use hua |
| -------------------- | ------------------ |
| `os.listdir()`       | ⭐⭐⭐⭐⭐              |
| `os.path.join()`     | ⭐⭐⭐⭐⭐              |
| `os.path.exists()`   | ⭐⭐⭐                |
| `os.mkdir()`         | ⭐⭐⭐                |
| `os.remove()`        | ⭐⭐                 |
| `os.rename()`        | ⭐                  |
| `os.walk()`          | ⭐                  |
| `os.path.splitext()` | ⭐⭐                 |
| `os.path.getsize()`  | ⭐                  |
| `open()`             | ⭐⭐⭐⭐⭐              |


