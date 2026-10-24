## D. Minimal cost

Time limit: 1 s · Memory limit: 256 MB

An undirected graph without multiple edges and loops is given. It already contains some (possibly zero) number of edges. You can add new edges to it for a fee (the fee is different for each edge). It is required to make the graph connected for the smallest fee.

Input

The first line of input contains a single integer n (1≤n≤50) – the number of vertices in the original graph.

In the next rows an×n matrix is given (0≤aij≤100), zero aij denotes the edge between vertices i and j, while the positive value of aij denotes the fee to connect vertices i and j.

Output

Print a single number - the minimum possible cost to make the graph connected.

Examples

**Input 1**

```
3
0 0 28
0 0 0
28 0 0
```

**Output 1**

```
0
```
