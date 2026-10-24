## B. Red Riding Hood and Long Journey

Time limit: 1.5 s · Memory limit: 256 MB

Red Riding Hood lives in a small village. Today she received a letter from her grandmother, in which it is written she is ill. Therefore, Little red Riding hood, being a caring girl, wants to bring a basket of fruits and medicine for her grandmother who lives in another village. She knows a village that has medicines and a merchant who sells fresh fruits. The path can be long and therefore, she wants to come as quickly as possible. Help Red Riding Hood find the shortest way to her grandmother so that she can buy all the necessary presents along the way.

Input

In the first line you will be given two numbers N,M (1≤N≤100000,0≤M≤min(2⋅105,N(N−1)/2)), denoting the number of villages and number of paths between two neighboring villages. Next M lines contains three numbers: v,u (1≤v,u≤N) and c (1≤c≤1000). First two numbers represents the path between villages v and u, the third is the distance between them. Last line contains four numbers: s,a,b,f (1≤s,a,b,f≤N), denoting the Red Riding Hood, merchant, pharmacy, and grandmother’s villages.

Output

Print one single number - the shortest distance to grandmother’s village so that Red Riding Hood can buy all the necessary presents along the way. If there is no such path then print -1.

Note

Everyone who presented in the task are not necessarily located in different villages. It is also worth to clarify that path between two neighboring villages is available for both directions and guaranteed that there is no more than one direct path between any two villages.

Examples

**Input 1**

```
4 5
1 2 3
3 4 7
1 3 1
3 2 1
2 4 6
1 2 3 4
```

**Output 1**

```
8
```

**Input 2**

```
4 2
1 3 10
2 4 15
2 2 3 4
```

**Output 2**

```
-1
```

**Input 3**

```
6 9
1 2 5
1 3 6
2 4 4
2 5 1
3 4 4
3 6 6
4 5 3
4 6 2
5 6 3
1 3 3 3
```

**Output 3**

```
6
```
