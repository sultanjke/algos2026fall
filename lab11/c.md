## C. Travelling

Time limit: 1 s · Memory limit: 256 MB

The government allocated money to asphalt roads between n villages in the region. There are m existing roads, and each of them connects two cities. There are two types of asphalt material, the first one is made especially for big vehicles and costs x tenge per kilometer, while the second is made for small cars and costs y tenge per kilometer. For each road government said which type of asphalt should be used (maybe both are appropriate). Akimat wants to renovate roads such that it would be possible to reach any village from another via repaired roads, spending as less money as possible, and fulfilling the government’s requirements. Help akimat to calculate the total cost of the project.

Input

The first line contains two integers n, m (1≤n,m≤1000) - the number of cities and the number of roads between cities The next line contains two integers x and y (1≤x,y≤100) - the price of asphalt for big and small vehicles. The next m lines contain one string - type of asphalt that should be used, and three integers a, b, c (1≤a,b≤n;1≤c≤100) denoting the road between cities a and b is c kilometers long.

Output

Print the only integer - the total cost of the project.

Examples

**Input 1**

```
7 6
4 3
both 2 7 4
both 1 7 2
big 4 6 1
big 3 7 3
small 5 6 1
both 5 7 10
```

**Output 1**

```
67
```
