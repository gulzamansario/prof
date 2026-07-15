Aapke diye hue problem ko pehle analyze karte hain, phir isi **pattern (String + Stack + Greedy + Adjacent Removal)** ke around ek **DSA practice paper** banata hoon.

---

# Problem Analysis

## Problem:

**String with A & B - Remove Adjacent Matches**

Input:

```
String containing only A and B
```

Example:

```
Input:
AABABB

Need:
Remove adjacent same characters

Output:
ABAB
```

---

## Core Concept

Yeh problem actually **String Manipulation + Stack Pattern** hai.

Kyun?

Kyuki hume:

* Adjacent characters compare karne hain.
* Agar same hain → remove karna hai.
* Agar different hain → rakhna hai.

Example:

```
AABB

Step 1:
AA remove

BB remove

Answer:
""
```

---

## Important Pattern

### "Adjacent Duplicate Removal"

Ye same pattern hai:

```
current character == previous character
```

Toh stack use hota hai.

---

## Stack Approach

Example:

```
Input:

AABABB

Stack:

A

A same mila
remove A

B

A

B

B same mila
remove B


Result:

AB
```

---

## Complexity

Time:

```
O(n)
```

Space:

```
O(n)
```

---

# Related Concepts Tested

Is question se interviewer ye concepts check karta hai:

✅ String traversal
✅ Stack implementation
✅ Greedy thinking
✅ Two pointer approach
✅ Character frequency
✅ Pattern matching

---

# DSA Practice Paper

## Topic:

**Strings + Stack + Adjacent Characters**

Level:
Easy → Medium

---

# Section A: Basic String Problems

## Q1. Remove Adjacent Duplicate Characters

Given a string, remove adjacent duplicate characters.

Example:

```
Input:
abbaca

Output:
ca
```

Explanation:

```
abbaca

bb remove

aaca

aa remove

ca
```

---

## Q2. Remove Adjacent Same Characters Until Stable

Example:

```
Input:

aaabccddd

Output:

b
```

Because:

```
aaa remove
ccc remove
ddd remove
```

---

## Q3. Check If String Has Adjacent Same Characters

Return True if any adjacent characters are same.

Example:

```
Input:

ABBA

Output:

True
```

---

## Q4. Make String Alternating

Given only A and B characters, remove minimum characters so that no adjacent characters are same.

Example:

```
Input:

AAABBBA

Output:

ABABA
```

---

# Section B: Stack Based Problems

## Q5. Valid Parentheses

Given:

```
()
{}
[]
```

Check if brackets are balanced.

Example:

```
Input:

{[()]}

Output:

True
```

Concept:

Stack

---

## Q6. Remove K Adjacent Same Characters

Given string and k.

Remove k consecutive same characters.

Example:

```
Input:

deeedbbcccbdaa

k=3


Output:

aa
```

---

## Q7. Simplify File Path

Example:

Input:

```
/home/user/../docs
```

Output:

```
/home/docs
```

Concept:

Stack

---

# Section C: Two Pointer String Problems

## Q8. Reverse Only Vowels

Example:

```
Input:

hello

Output:

holle
```

---

## Q9. Remove Duplicate Characters

Example:

```
Input:

programming

Output:

progamin
```

---

## Q10. Move All A's To End

Example:

```
Input:

ABABAA

Output:

BBBAAA
```

Condition:

Order of B should remain same.

---

# Section D: Medium Level Problems

## Q11. Longest Substring Without Repeating Characters

Example:

```
Input:

abcabcbb

Output:

3
```

Explanation:

Longest:

```
abc
```

---

## Q12. Longest Valid Parentheses

Example:

```
Input:

(())

Output:

2
```

---

## Q13. Minimum Deletion To Make String Balanced

String contains:

```
a and b
```

Remove minimum characters.

Example:

```
Input:

aababbab

Output:

2
```

---

## Q14. Check If Two Strings Are Anagrams

Example:

```
listen

silent

Output:

True
```

---

# Section E: Interview Level Problems

## Q15. Decode String

Input:

```
3[a2[c]]
```

Output:

```
accaccacc
```

Concept:

Stack

---

## Q16. String Compression

Input:

```
aaabbcccc

Output:

a3b2c4
```

---

## Q17. Minimum Remove To Make Parentheses Valid

Example:

```
Input:

lee(t(c)o)de)

Output:

lee(t(c)o)de
```

---

## Q18. Partition Labels

Example:

```
Input:

ababcbacadefegdehijhklij


Output:

[9,7,8]
```

---

# Section F: Same Pattern As Your Given Question

## Q19. Remove Adjacent Opposite Pairs

Rules:

```
AB remove

BA remove
```

Example:

```
Input:

ABBA

Process:

AB remove

BA remove


Output:

Empty
```

---

## Q20. Make String Alternating With Minimum Deletions

Only:

```
A B
```

Allowed.

Example:

```
Input:

AAAA

Output:

3
```

Because only:

```
A
```

can remain.

---

# Recommended Solving Order

Agar aap is type ke questions master karna chahte ho:

```
1. Remove Adjacent Duplicates
        ↓
2. Valid Parentheses
        ↓
3. Remove K Adjacent Characters
        ↓
4. Longest Substring Without Repeat
        ↓
5. Minimum Deletion Problems
        ↓
6. Decode String
```

---

## Important Interview Pattern Name

Is type ke questions ko yaad rakho:

**"When you see adjacent characters and removal/replacement is involved → Think Stack."**

Ye pattern companies mein bohot poocha jata hai:

* Google
* Amazon
* Microsoft
* Meta

Aapka given question **LeetCode 1047 (Remove All Adjacent Duplicates In String)** ke pattern ka hai. Iske variations solve kar loge to String Stack problems ka 80% cover ho jayega.
