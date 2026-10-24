## D. Try Again

Time limit: 5 s · Memory limit: 256 MB

You are given undirected graph with n vertices, m edges, and q queries. Initially all vertices are black. There are two types of queries.

1\. 1 v - Change the color of vertex v to red.

2\. 2 v - Output the distance to the nearest red vertex to v, or -1 is there is no such vertex.

Input

First line contains three integers 1≤n,m≤5000,1≤q≤105. Next m lines contain information about edges. Next q lines contain queries as described in the statement.

Output

Output answer to queries of type 2.

Examples

**Input 1**

```
5 4 7
1 2
2 3
3 4
4 5
2 1
1 1
2 1
2 2
2 5
1 3
2 5
```

**Output 1**

```
-1
0
1
4
2
```
