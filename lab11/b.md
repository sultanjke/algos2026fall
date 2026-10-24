## B. Duck Islands

Time limit: 1 s · Memory limit: 256 MB

Jonathan became a king of Duck Islands recently. He is very happy now, but being a king impose a lot of obligations on him. One of them is to connect all initially disconnected islands with bridges, such that for every pair of islands in his kingdom there is a path between them. The cost of the bridge between islands i and j is di + dj, where di and dj are the number of ducks in the islands i and j respectively. Jonathan wants to minimize the total expence of bridge building. He is not good at math, so he asked your help to find amount of money he will spend.

Input

The first line of the input contains the only integer n - number of islands in Jonathan’s Duck Kingdom (1 ⩽ n ⩽ 500).

The next line contains n integers di - the number of ducks in the ith island (1 ⩽ di ⩽ 105).

Output

Print the only integer c - amount of money that Jonathan will spend to connect islands in his kingdom.

Note

In the first example you can construct four bridges between islands 1 and 2, 3 and 4, 4 and 5, 1 and 4.

In the second sample you can construct any bridges you want.

Examples

**Input 1**

```
5
2 5 4 2 8
```

**Output 1**

```
27
```

**Input 2**

```
5
5 5 5 5 5
```

**Output 2**

```
40
```
