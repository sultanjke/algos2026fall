## J. Who has a big Family?

Time limit: 1 s · Memory limit: 256 MB

Given a graph without cycles or self loops. In any connected component of the graph, vertex with the lowest value in that component serves as the root. A vertex is _BigFam_ if it is a root or it has more children than its parent. Count the number of BigFam vertices in the given graph.

Input

On the first line there are two separated integers N and M (1≤N,M≤105) and the following M lines consist of two separated integers X and Y meaning that there is an edge between vertices X and Y.

Output

Print the number of BigFam vertices.

Examples

**Input 1**

```
4 3
1 2
2 3
2 4
```

**Output 1**

```
2
```
