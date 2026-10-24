## E. Nugman and Graph 2

Time limit: 5 s · Memory limit: 256 MB

Nugman has an undirected graph, consisting of n vertices and m edges. Nugman loves playing with the graph and now he has invented a new game:

-   The game consists of n steps.

-   On the ith step Nugman will remove vertex i from the graph. As Nugman removes a vertex, he also removes all the edges that go in and out of this vertex.

Nugman wants to know the number of connected components after deleting each vertex.

Input

The first line contains two numbers n,m (1≤n≤2⋅105,0≤m≤min(2⋅105,n⋅(n+1)2)), denoting the number of vertices and number of edges. Each of the next m lines contains two integers v,u (1≤v,u≤n) denoting the edge between vertices v and u.

Output

Print n lines. The ith line should contain number of connected components after first i operations.

Examples

**Input 1**

```
8 7
7 8
3 4
5 6
5 7
5 8
6 7
6 8
```

**Output 1**

```
3
2
2
1
1
1
1
0
```

**Input 2**

```
5 5
1 2
1 4
1 3
4 5
2 4
```

**Output 2**

```
2
2
1
1
0
```
