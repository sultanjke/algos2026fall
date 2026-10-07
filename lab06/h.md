## Submit a solution for H

|  |  |
| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem H

You have one letter. Your task is to find "balanced" char in array. "Balanced" char is the smallest in array, but more than your letter.

### Input format

The first line contains one integer n (2≤n≤2⋅105) — the number of letters in the array.

The second line contains n lowercase Latin letters separated by single spaces, given in non-decreasing order.

The third line contains one lowercase Latin letter k.

### Output format

Print the “balanced” letter — the smallest letter of the array that is greater than k.

If the array contains no letter greater than k, the search wraps around and the answer is the first (that is, the smallest) letter of the array.

### Examples

#### Input

```
3
c f g
a
```

#### Output

```
c
```

### Notes

Size of array should be more than 1;