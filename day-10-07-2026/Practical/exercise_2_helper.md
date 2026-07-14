
### 1. `upper()` — String ko uppercase mein convert karta hai

```python
name = "ali"
print(name.upper())
```

Output:

```
ALI
```

---

### 2. `lower()` — String ko lowercase mein convert karta hai

```python
text = "HELLO"
print(text.lower())
```

Output:

```
hello
```

---

### 3. `capitalize()` — Pehla letter capital karta hai

```python
text = "python"
print(text.capitalize())
```

Output:

```
Python
```

---

### 4. `title()` — Har word ka first letter capital karta hai

```python
text = "python programming"
print(text.title())
```

Output:

```
Python Programming
```

---

### 5. `strip()` — Starting aur ending ke spaces remove karta hai

```python
text = "   hello   "
print(text.strip())
```

Output:

```
hello
```

---

### 6. `replace()` — Text ko replace karta hai

```python
text = "I like Java"
print(text.replace("Java", "Python"))
```

Output:

```
I like Python
```

---

### 7. `split()` — String ko list mein divide karta hai

```python
text = "apple banana mango"
print(text.split())
```

Output:

```
['apple', 'banana', 'mango']
```

---

### 8. `join()` — List ko string mein join karta hai

```python
words = ["Hello", "World"]

print(" ".join(words))
```

Output:

```
Hello World
```

---

### 9. `find()` — Kisi word ka index return karta hai

```python
text = "Python"

print(text.find("t"))
```

Output:

```
2
```

Agar nahi mile:

```
-1
```

---

### 10. `count()` — Kisi character/word ki quantity count karta hai

```python
text = "banana"

print(text.count("a"))
```

Output:

```
3
```

---

### 11. `startswith()` — Check karta hai string kis se start hoti hai

```python
text = "Python"

print(text.startswith("Py"))
```

Output:

```
True
```

---

### 12. `endswith()` — Check karta hai string kis se end hoti hai

```python
text = "hello.py"

print(text.endswith(".py"))
```

Output:

```
True
```

---

### 13. `isdigit()` — Check karta hai sirf digits hain ya nahi

```python
text = "123"

print(text.isdigit())
```

Output:

```
True
```

---

### 14. `isalpha()` — Check karta hai sirf alphabets hain ya nahi

```python
text = "Python"

print(text.isalpha())
```

Output:

```
True
```

---

### 15. `islower()` / `isupper()` — Case check karte hain

```python
text = "hello"

print(text.islower())
print(text.isupper())
```

Output:

```
True
False
```

---

### Quick list yaad rakhne ke liye:

| Method         | Kaam                 |
| -------------- | -------------------- |
| `upper()`      | Capital letters      |
| `lower()`      | Small letters        |
| `capitalize()` | First letter capital |
| `title()`      | Har word capital     |
| `strip()`      | Spaces remove        |
| `replace()`    | Replace text         |
| `split()`      | String → List        |
| `join()`       | List → String        |
| `find()`       | Position find        |
| `count()`      | Count occurrences    |
| `startswith()` | Starting check       |
| `endswith()`   | Ending check         |
| `isdigit()`    | Number check         |
| `isalpha()`    | Alphabet check       |

