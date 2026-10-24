## B. Path

Time limit: 1 s · Memory limit: 256 MB

In an undirected graph, you need to find the shortest path between two vertices.

Input

In the first line given one number n, number of vertices (1≤n≤100). In n lines given, and n elements in each line ‘0’ or ‘1’ where 0 indicates the absence of an edge, 1 indicates the presence of an edge. In the next line two numbers are given: start and end of a path.

Output

Print the length of the shortest path. If the path does not exist, print a single number −1.

Examples

**Input 1**

```
5
0 1 0 0 1
1 0 1 0 0
0 1 0 0 0
0 0 0 0 0
1 0 0 0 0
3 5
```

**Output 1**

```
3
```

**Input 2**

```
5
0 1 1 1 1
1 0 0 0 0
1 0 0 0 0
1 0 0 0 0
1 0 0 0 0
3 5
```

**Output 2**

```
2
```
