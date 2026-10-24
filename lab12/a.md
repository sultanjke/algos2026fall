## A. Nugman and Graph

Time limit: 2 s · Memory limit: 256 MB

Nugman has a weighted directed graph, consisting of n vertices. In this graph, any vertex has a directional edge to any other vertex. Nugman loves playing with the graph and now he has invented a new game

-   The game consists of n steps.

-   On the i\-th step Nugman will add vertex xi to the graph. As Nugman add a vertex, he also will add all the edges that go in and out of this vertex.

Nugman wants to know the **longest shortest path** in the graph after adding each vertex.

Input

The first line contains an integer n (1≤n≤500) the number of vertices in the graph. Next n lines contain n integers each — the graph adjacency matrix: the j\-th number in the i\-th line aij (1≤aij≤100000) represents the weight of the edge that goes from vertex i to vertex j. It is guaranteed that aii\=0.

The next line contains n distinct integers: x1,x2,…,xn (1≤xi≤n) the vertices that Nugman deletes.

Output

Print n integers — the i\-th longest shortest path after adding vertex xi.

Examples

**Input 1**

```
2
0 5
4 0
1 2
```

**Output 1**

```
0
5
```

**Input 2**

```
4
0 3 1 1
6 0 400 1
2 4 0 1
1 1 1 0
4 1 2 3
```

**Output 2**

```
0
1
2
2
```
