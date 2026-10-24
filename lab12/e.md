## E. Cycle.

Time limit: 1 s · Memory limit: 256 MB

Given a directed graph. Determine if it contains a cycle of negative weight, and if so, print it.

Input

The first line contains the number N(1≤N≤100) – the number of graph vertices. The next N lines contain N numbers each – the adjacency matrix of the graph. The absolute value of edge weights is less than 100000. If there is no edge, the corresponding value is 100000.

Output

In the first line print `YES` if the cycle exists, or `NO` otherwise. If there is a cycle, print in the second line the number of vertices in it (starting path from the same vertex as in the end of path), and in the third line print the vertices included in this cycle (path) in the order of traversal. If there are several cycles, then print any of them.

Examples

**Input 1**

```
3
100000 100000 -51
100 100000 100000
100000 -50 100000
```

**Output 1**

```
YES
4
3 2 1 3
```