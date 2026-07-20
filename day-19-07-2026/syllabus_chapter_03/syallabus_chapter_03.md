Perfect! Agar tum **Two Pointers** aur **Palindrome Index** ko master karna chahte ho, to neeche 10 exercises diye hain. Maine inhe **easy → medium → hard** order me arrange kiya hai. **Solutions mat dekhna**, pehle khud solve karna.

---

# Palindrome by Removing One Character - Practice Test

## Q1 (Easy)

Write a function that checks whether a string is a palindrome using the **two-pointer** approach.

### Example

```
Input:
"madam"

Output:
True
```

---

## Q2 (Easy)

Return the index of the character to remove to make the string a palindrome.

```
Input:
"aaab"

Output:
3
```

---

## Q3 (Easy)

Return the index of the character to remove.

```
Input:
"baa"

Output:
0
```

---

## Q4 (Medium)

The string is already a palindrome.

```
Input:
"racecar"

Output:
-1
```

---

## Q5 (Medium)

One character in the middle is wrong.

```
Input:
"abca"

Expected:
Return the correct index.
```

---

## Q6 (Medium)

A mismatch occurs near the end.

```
Input:
"radayr"

Expected:
Return the correct index.
```

---

## Q7 (Medium)

No single character removal can make the string a palindrome.

```
Input:
"abcdef"

Expected:
Return -1
```

---

## Q8 (Hard)

Write your own `is_palindrome(left, right)` helper function **without using**:

* `[::-1]`
* `reversed()`

Use only:

* `left`
* `right`
* `while`

Test it with:

```
"level"
"python"
"noon"
"abcd"
```

---

## Q9 (Hard)

Implement the complete `palindrome_index()` function **without looking at any previous code**.

Requirements:

* Use two pointers.
* Use a helper function.
* Time Complexity: **O(n)**
* Extra Space: **O(1)**

Test it on:

```
racecar
abca
aaab
baa
radayr
abcdef
madam
abecbea
```

---

## Q10 (Interview Challenge)

Modify the problem.

Instead of returning the **index**, return the **character** that should be removed.

### Example

```
Input:
"abca"

Output:
'b'
```

```
Input:
"radayr"

Output:
'y'
```

```
Input:
"racecar"

Output:
None
```

---

# Bonus Challenge (Very Hard ⭐⭐⭐⭐⭐)

Suppose you are allowed to remove **at most one character**.

Write a function that returns only:

* `True` if the string can become a palindrome after removing **zero or one** character.
* `False` otherwise.

### Examples

```
"abca"     → True
"racecar"  → True
"abcdef"   → False
"deeee"    → True
```

---

# Practice Rules

1. ❌ Do not use `s[::-1]`.
2. ✅ Use only two pointers.
3. ✅ Make a helper function.
4. ✅ Dry-run your code on paper before running it.
5. ✅ After each question, write its **time complexity** and **space complexity**.

Ye 10 questions complete kar loge, to **Palindrome Index**, **Two Pointers**, aur interview-level palindrome problems ka concept kaafi mazboot ho jayega.
