## Submit a solution for E-Squares of a Sorted Array

|  |  |
| --- | --- |
| **Time limit:** | 2 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem E: Squares of a Sorted Array

Nurlan has an array of integers sorted in **non-decreasing** order. Some of the numbers may be negative.

He squares every element and wants to see the result sorted in non-decreasing order as well. Squaring breaks the order: −4 stands before 3, but 16 is greater than 9.

Print the squares of all elements in non-decreasing order.

### Input format

The first line contains one integer n (1≤n≤2⋅105) — the length of the array.

The second line contains n integers a1,a2,…,an (−104≤ai≤104) separated by single spaces. The array is sorted: ai≤ai+1 for every i.

### Output format

Print n integers separated by single spaces — the squares of the elements in non-decreasing order.

### Examples

#### Input

```
5
-4 -1 0 3 10
```

#### Output

```
0 1 9 16 100
```

#### Input

```
4
-7 -3 2 11
```

#### Output

```
4 9 49 121
```

### Notes

In the first example the array is \[−4,−1,0,3,10\], the squares are \[16,1,0,9,100\], and sorted they give \[0,1,9,16,100\].

Sorting the squares directly would work, but there is a faster way that uses **merging**. Split the array at the point where the sign changes. Squares of the negative part decrease from left to right, squares of the non-negative part increase. These are two sorted sequences, so they can be merged in O(n) — the same merge step that merge sort is built from. It is convenient to take the largest square at each step, comparing the two ends of the array, and to fill the answer from the end.

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab07/e.py)
