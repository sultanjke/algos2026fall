### Problem F: 106735. Triangle Binary Search Tree

You are given N integers in order of their insertion to Binary Search Tree. You draw a set of horizontal lines, one through all the nodes of the same **depth** (the depth of the root is 0, and the depth of any other node is the depth of its parent plus one). After that you can see triangles with nodes instead of vertices and edges instead of sides. Your task is to calculate the number of the smallest triangles.

### Input format

The first line consists of an integer N - number of nodes in Binary Search Tree (1 ⩽ N ⩽ 10000).

The second line contains N integers ai - value of each node in Binary Search Tree in order of their insertion (1 ⩽ ai ⩽ N).

It is guaranteed that there are no duplicates.

### Output format

Print the number of mini-triangles in resulting Binary Search Tree.

### Examples

#### Input

```
3
2 3 1
```

#### Output

```
1
```

#### Input

```
3
1 2 3
```

#### Output

```
0
```

#### Input

```
16
13 9 3 7 6 16 1 11 12 10 4 2 14 5 8 15
```

#### Output

```
5
```

### Notes

A smallest triangle is formed by a node together with its left and its right son, so a node contributes a triangle exactly when both of its sons are present.

In the first sample the insertion order 2,3,1 makes 2 the root with sons 1 and 3, so there is exactly 1 triangle.

In the second sample the values 1,2,3 are inserted in increasing order, so the tree is a chain and no node has two sons — the answer is 0.

In the third sample the resulting tree contains 5 such triangles.