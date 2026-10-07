### Problem B: 105587. Get subtree

You are given Binary Search Tree. Your task is to calculate the size of the subtree of the node X.

Remember, that the subtree of node X is the set of all nodes whose ancestor is node X, including it. The size of the subtree is the size of such set.

### Input format

The first line of the input contains an integer N — number of nodes in Binary Search Tree (1≤N≤103).

The second line contains N pairwise distinct integers ai (1≤ai≤109) — values of nodes in order of insertion to the Binary Search Tree.

The third line contains a single integer X (1≤X≤109) — the value of the node whose subtree size you must calculate. It is guaranteed that X occurs among a1,a2,…,aN.

### Output format

Print the size of the subtree of the given node.

### Examples

#### Input

```
7
4 2 6 1 3 5 7
4
```

#### Output

```
7
```

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab04/b.py)
