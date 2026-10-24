## A. Marios War

Time limit: 2 s · Memory limit: 256 MB

Here is the field, where each cell can have one of three values:

-   "0" - an empty cell;

-   "1" - a cell with the brown mushroom;

-   "2" - a cell with Mario.

Every minute, Mario crushes any brown mushroom that is adjacent to his position (up, down, top, bottom) and new Mario appears instead of mushroom, Mario does not move to the empty cell.

How many minutes will it take for Mario to kill all brown mushrooms in each cell? The number of Marios can be more than one. If this is impossible, return -1.

Input

The first line contains two integers, m - number of rows of a field, n - number of columns of a field (1≤m,n≤1000). The following m lines contain n values (0, 1, or 2).

Output

Print the minimum time (in minutes) that must elapse until no cell will contain a brown mushroom. If any mushroom is unreachable for every Mario in a field print -1.

Note

The picture illustrates the procedure of the first example.

In the second example, the mushroom at (3, 1) is unreachable, because Mario can move 4-directionally. So, the output is -1.

In the last example, there are no brown mushrooms, there is nothing to kill, so the answer is 0.

Examples

**Input 1**

```
3 3
2 1 1
1 1 0
0 1 1
```

**Output 1**

```
4
```

**Input 2**

```
3 3
2 1 1
0 1 1
1 0 1
```

**Output 2**

```
-1
```

**Input 3**

```
1 3
0 2 0
```

**Output 3**

```
0
```
