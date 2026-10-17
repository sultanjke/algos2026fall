## Submit a solution for B-Merge Two Sorted Arrays

|  |  |
| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem B: Merge Two Sorted Arrays

You are given two arrays of integers, a and b. Both of them are already sorted in non-decreasing order.

Merge them into one sorted array that contains all elements of a and all elements of b.

### Input format

The first line contains one integer n (1≤n≤105) — the size of a.

The second line contains n integers a1,a2,…,an (1≤ai≤105) separated by single spaces. The array is sorted: ai≤ai+1.

The third line contains one integer m (1≤m≤105) — the size of b.

The fourth line contains m integers b1,b2,…,bm (1≤bi≤105) separated by single spaces. The array is sorted: bi≤bi+1.

### Output format

Print n+m integers separated by single spaces — all elements of both arrays in non-decreasing order.

### Examples

#### Input

```
5
4 5 6 7 10
5
2 4 6 7 8
```

#### Output

```
2 4 4 5 6 6 7 7 8 10
```

#### Input

```
3
1 4 7
1
6
```

#### Output

```
1 4 6 7
```

### Notes

Both arrays are already sorted, so there is no need to sort anything. Walk along the two arrays with two indices and always take the smaller of the two current elements. This is exactly the **merge** step of merge sort, and it works in O(n+m).

Do not forget the tail: when one array runs out, all remaining elements of the other one still have to be printed.

The answer always contains exactly n+m numbers.

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab07/b.py)
