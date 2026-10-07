### Problem J: K-th element in Binary Search Tree

You are given N integers. Insert them one by one, in the given order, into an initially empty binary search tree, and then print the K\-th smallest element of the tree.

For example, if the values are {20,8,22,4,12,10,14} and K\=3, then the in-order traversal of the tree visits them in sorted order {4,8,10,12,14,20,22}, so the answer is 10; for K\=5 the answer is 14.

### Input format

The first line contains two integers N and K (1≤N≤105, 1≤K≤105).

The second line contains N **pairwise distinct** integers ai (1≤ai≤105) — the values inserted into the tree, in this order.

### Output format

Print the K\-th smallest element of the tree.

If K\>N, print −1.

### Examples

#### Input

```
7 3
20 8 22 4 12 10 14
```

#### Output

```
10
```

#### Input

```
7 5
20 8 22 4 12 10 14
```

#### Output

```
14
```

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab04/j.py)
