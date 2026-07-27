20. Absolute Difference of Diagonal Sums

Problem Understanding:
Given a square matrix, calculate the absolute difference between the sum of the primary diagonal and the secondary diagonal.

Primary Diagonal:

· Elements where row index = column index
· Matrix[i][i] for i from 0 to n-1

Secondary Diagonal:

· Elements where row index + column index = n-1
· Matrix[i][n-1-i] for i from 0 to n-1

Example:

```
Matrix: [1, 2, 3]
        [4, 5, 6]
        [7, 8, 9]

Primary sum: 1 + 5 + 9 = 15
Secondary sum: 3 + 5 + 7 = 15
Difference: |15 - 15| = 0
```

Edge Cases:

· For odd n, the center element is counted in both diagonals
· This is correct as it appears in both diagonal definitions

---