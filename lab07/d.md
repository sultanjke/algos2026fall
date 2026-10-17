## Submit a solution for D-Count the Inversions

|  |  |
| --- | --- |
| **Time limit:** | 2 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem D: Count the Inversions

Aidana is checking how messy a list of numbers is.

She calls a pair of positions (i,j) an **inversion** if i<j and ai\>aj — that is, a larger number stands before a smaller one.

A sorted array has no inversions at all, and the more inversions an array has, the further it is from being sorted. Help Aidana count them.

### Input format

The first line contains one integer n (1≤n≤105) — the length of the array.

The second line contains n integers a1,a2,…,an (1≤ai≤109) separated by single spaces.

### Output format

Print one integer — the number of inversions in the array.

### Examples

#### Input

```
2
2 1
```

#### Output

```
1
```

#### Input

```
5
3 1 4 1 5
```

#### Output

```
3
```

### Notes

In the first example the pair (1,2) is an inversion, because 2\>1.

In the second example the array is \[3,1,4,1,5\] and the inversions are (1,2), (1,4) and (3,4).

Note that equal elements do **not** form an inversion: the condition is strictly ai\>aj.

The intended solution is merge sort: while merging two sorted halves, every element taken from the right half is smaller than all remaining elements of the left half, which gives the number of inversions in O(nlog⁡n). A straightforward double loop over all pairs is O(n2) and will not fit into the time limit.

The answer can be as large as n(n−1)/2≈5⋅109, so a 32-bit integer type is **not** enough.

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab07/d.py)
