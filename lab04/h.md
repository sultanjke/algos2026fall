### Problem H: 111743. Greater Sum Tree

Given the root of a **binary search** tree with distinct keys. Replace the key of each node with the sum of the keys over the nodes that has greater than or equal key. Print new keys in increasing order.

As a reminder, a binary search tree is a tree that satisfies these constraints:

-   The left subtree of a node contains only nodes with keys less than the node’s key.

-   The right subtree of a node contains only nodes with keys greater than the node’s key.

-   Both the left and right subtrees must also be binary search trees.

### Input format

The first line contains a single integer n (1≤n≤100) — the number of nodes.

The second line contains n pairwise distinct integers ai (0≤ai≤1000) — the keys, inserted one by one, in this order, into an initially empty binary search tree.

### Output format

In a single line print n integers — the new keys in increasing order, separated by single spaces.

### Examples

#### Input

```
9
4 1 6 0 2 3 5 7 8
```

#### Output

```
8 15 21 26 30 33 35 36 36
```

### Notes

NOTE: Solve with **BST**! ![image](https://ejudge.kz/new-client?SID=f3fb9c64ddc021b2&prob_id=8&action=194&file=1.png)