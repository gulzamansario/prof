## Question Overview: **Check If String Has Adjacent Same Characters**

### Problem ka matlab:

Tumhe ek string di jayegi aur tumhe check karna hai ke **kisi bhi do paas paas (adjacent) characters ki value same hai ya nahi**.

Agar same characters mil jayein:

```text
True
```

return karo.

Agar koi adjacent same character nahi hai:

```text
False
```

return karo.

---

## Example 1:

Input:

```python
st = "ABBA"
```

String ko dekho:

```
A B B A
  ↑ ↑
same
```

`B` aur `B` adjacent hain aur same hain.

Output:

```
True
```

---

## Example 2:

Input:

```python
st = "ABCD"
```

Check:

```
A B C D
```

Koi bhi paas wala character same nahi hai.

Output:

```
False
```

---

# Is question ka main concept:

Yahan **Stack zaroori nahi hai**.

Kyuki hume sirf **previous character** yaad rakhna hai.

Pattern:

```
Current character
        |
        ↓
Previous character se compare karo
```

---

## Logic:

Start:

```
previous = None
```

Loop chalega:

```
A B B A
```

### Step 1:

Current:

```
A
```

Previous nahi hai, to save kar do:

```
previous = A
```

---

### Step 2:

Current:

```
B
```

Compare:

```
B == A ❌
```

Update:

```
previous = B
```

---

### Step 3:

Current:

```
B
```

Compare:

```
B == B ✅
```

Mil gaya adjacent duplicate.

Return:

```
True
```

---

# Tumhare code ka issue:

Tumne likha:

```python
if chr and chr[-1][0] == chr:
```

Yahan problem ye hai:

`chr` ek **single character** hai.

Example:

```python
for chr in "ABBA":
```

Pehli iteration:

```python
chr = "A"
```

Ab:

```python
chr[-1]
```

ka matlab:

```
"A" ka last character
```

hai.

Lekin tum string ke previous character ko access karna chah rahe ho, jo alag variable mein hona chahiye.

---

# Is question ke related variations:

### 1. Simple Check

Input:

```
AABB
```

Output:

```
True
```

---

### 2. No Duplicate

Input:

```
ABCDE
```

Output:

```
False
```

---

### 3. Return Character Also

Input:

```
ABCCDE
```

Output:

```
C
```

(Konsa character repeat hua?)

---

### 4. Count Adjacent Pairs

Input:

```
AABBCC
```

Output:

```
3
```

---

### Yaad rakhne wala pattern:

```
Current character
        |
        ↓
Compare with previous character
        |
        ↓
Same hai?
   /       \
 Yes       No
 True    Continue
```

Is question ka difficulty level **Easy** hai aur iska main skill hai:
**String Traversal + Previous Value Tracking**.
