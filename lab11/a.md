## A. Hana Kagerou

Time limit: 2 s · Memory limit: 256 MB

When preparing problems for the next algorithm quiz, Nyaruko created a problem she couldn’t solve herself. Since it was very late she decided to use this problem in a quiz and requested help from you.

You are given a graph with n nodes and m segments with some cost. For each segment \[l,r\] with cost c, add an edge between vertices x and y with cost c for all pairs of vertices such that l≤x<y≤r. Find the cost of the minimum spanning tree in the resulting graph. It’s guaranteed that the graph will be connected.

Input

The first line contains two integers n,m (2≤n,m≤2∗105) - the number of vertices and edges. Each of the next m lines contains three integers l,r,c (1≤l<r≤n,1≤c≤109) - endpoints of the segment and its cost.

Output

Output single integer - the cost of the MST.

Note

The graph in the first example looks like this.

Examples

**Input 1**

```
5 2
1 3 2
3 5 3
```

**Output 1**

```
10
```

**Input 2**

```
10 3
1 5 3
3 10 100
8 10 4
```

**Output 2**

```
320
```
