## C. Nugman and Graph 3

Time limit: 1 s · Memory limit: 256 MB

Nugman and Olzhas are stuck in a magical world called ADS, and they want to return to KBTU. To return, they must walk together to their destination. There are n cities (numbered from 1 to n) and m two-way airlines for each pair of different cities x and y, there is a two-way road between cities x and y if and only if there is no airline between them. The trip between the cities takes exactly one hour.

Nugman is afraid of heights and therefore walks, and Olzhas knows how to fly in this world. They start their journey in city 1 and end in city n. Nugman and Olzhas **cannot intersect**, with the exception of cities 1 and n.

In what is the smallest number of hours both will get to the city n?

Input

The first line of the input contains two integers n and m (2≤n≤400, 0≤m≤79800) — the number of towns and the number of railways respectively.

Each of the next m lines contains two integers u and v, denoting a railway between towns u and v (1≤u,v≤n).

You may assume that there is at most one railway connecting any two towns.

**Subtasks**

Output

In a single line print a single integer — the answer to the problem. If it’s impossible print −1.

Examples

**Input 1**

```
3 1
1 3
```

**Output 1**

```
2
```

**Input 2**

```
3 3
1 2
2 3
3 1
```

**Output 2**

```
-1
```