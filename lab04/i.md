### Problem I: More One Night

You are given a permutation of size n. Create an empty BST, and insert the values p1,p2,…,pn into it in this order, one by one, using the usual binary search tree insertion (no balancing). Find the number of leaves in the resulting BST.

### Input format

The first line contains a single integer n (1≤n≤5000) — the size of the permutation.

The second line contains n distinct integers from 1 to n — the permutation p1,p2,…,pn.

### Output format

Output one integer — the number of leaves in the BST after all n insertions.

### Examples

#### Input

```
1
1
```

#### Output

```
1
```

#### Input

```
5
4 3 5 1 2
```

#### Output

```
2
```

### Notes

A vertex is called a leaf if it has no children.

In the second sample the BST looks like this.

<img width="600" height="215" alt="a" src="assets/i.jpg" />

The answer is 2 (vertices 2 and 5).