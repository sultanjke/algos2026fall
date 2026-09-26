### Problem B: Patchwork Staccato I

You are given array a (1≤ai≤109) of length n (1≤n≤100) and q (1≤q≤100) queries. In query i you are given two pairs of segments l1,r1,l2,r2 (1≤l1≤r1≤109,1≤l2≤r2≤109), find number of indices c (1≤c≤n) for which one of the following conditions is satisfied: l1≤ac≤r1 or l2≤ac≤r2.

### Input format

The first line contains two integers n and q (1≤n≤100, 1≤q≤100).

The second line contains n integers a1,a2,…,an (1≤ai≤109) — the array itself, given in arbitrary order.

Each of the next q lines contains 4 integers l1,r1,l2,r2 (1≤l1≤r1≤109, 1≤l2≤r2≤109) — one query.

### Output format

Output q lines — the answer to each query in the order they are given.

### Examples

#### Input

```
7 3
21 1 2 3 5 8 13
1 5 13 21
1 1 2 3
1 3 2 8
```

#### Output

```
6
3
5
```

### Notes

The array a is given in arbitrary order. Sort it first — after that the answer to a query is found by binary search over the sorted array: you need the position of the first element that is ≥l and the position of the first element that is \>r.

You do not have to implement a sorting algorithm yourself — use the one built into your language:

C++ — `sort(a.begin(), a.end());` (header `algorithm`)

Python — `a.sort()`

Java — `Arrays.sort(a);` (package `java.util`)

Do not forget that both segments are closed: the elements equal to r1 or r2 are counted too, and the elements that fall into both segments are counted only once.

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab03/b.py)