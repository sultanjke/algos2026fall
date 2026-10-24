## G. Fly Me to the Moon

Time limit: 1 s · Memory limit: 256 MB

_Giving up halfway is worse than never trying at all_

— Misato Katsuragi, _Evangelion_

I think you’ve all heard about Keqing and her love for solving puzzles. But it’s time for you to find out about her friend Ganyu, who also loves to solve various problems. Unlike Keqing, Ganyu likes graph problems more. This time she has a directed graph of n vertices and m edges. She is very interested to know if she can turn her primordial graph into an acyclic graph. Moreover, she set herself an additional condition — she can delete only one edge from the graph. Unfortunately, Ganyu has a lot to do at work, so she didn’t have time to solve this problem. Therefore, she asked you to help her. Try your best for this problem because she believes in you!

Input

The first line contains n and m — the number of vertices and the number of edges. Then m lines follow. Each line contains two integers x and y denoting a directed edge going from vertex x to vertex y. Each ordered pair (x,y) is listed at most once. However, loops for the vertex itself in the graph are possible. (2≤n≤500,1≤m≤min(n(n−1),105)).

Output

Print the answer. YES — if it is possible. NO — otherwise.

Note

Acyclic graph - each edge directed from one vertex to another, such that following those directions will never form a closed loop.

Good Luck & Have Fun!

Examples

**Input 1**

```
5 6
1 3
2 1
3 5
4 3
5 4
3 2
```

**Output 1**

```
NO
```

**Input 2**

```
2 2
1 2
2 1
```

**Output 2**

```
YES
```

**Input 3**

```
2 2
1 1
1 2
```

**Output 3**

```
YES
```
