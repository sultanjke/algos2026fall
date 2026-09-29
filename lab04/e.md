### Problem E: 52477. Width

Given a binary tree, write a program to get the width of the given tree.

The level of a node is the number of vertices on the path from this node to the root. The width of a level h is the number of vertices with level h. The width of a tree is the maximal width over the levels.

Vertex number 1 always will be root.

### Input format

The first line contains an integer n (1≤n≤103) — the number of vertices.

Each of the next n−1 lines contains 3 integers x,y,z (1≤x,y≤n, 0≤z≤1) — vertex y is a son of vertex x; if z\=0 it is the left son, if z\=1 it is the right son. Vertex 1 is never a son. Every vertex except vertex 1 is a son of exactly one vertex, a vertex has at most one left and at most one right son, and the edges form a tree rooted at vertex 1. For n\=1 there are no such lines.

The n−1 lines are given in **arbitrary order**: a son may be described before its parent.

### Output format

Print one integer maximum width.

### Examples

#### Input

```
6
1 2 1
1 3 0
3 5 0
3 6 1
2 4 1
```

#### Output

```
3
```

#### Input

```
4
1 2 0
2 3 0
2 4 1
```

#### Output

```
2
```

### Notes

In the first sample the widest level is the third one, it holds 3 vertices (5, 6, 4).

In the second sample the widest level is the third one as well, it holds 2 vertices (3, 4).