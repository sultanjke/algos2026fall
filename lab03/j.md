### Problem J: Jonathan the Farmer

Jonathan is the Farmer whose household was damaged by a huge hurricane. He lost majority of his cattle. One day he walked near his farm and observed that there are N sheeps on the field. Each sheep is always grazing inside some rectangular area. Jonathan remembered such areas for each sheep. When he came home, he decided to build a paddock to catch at least K sheeps (to catch a sheep Jonathan must cover sheep’s pasture fully). Jonathan prefers squares rather than usual rectangles, therefore he want to build square paddock with the corner at point (0,0). Material for paddock costs money, so Jonathan wants to minimize the length of paddock side. He is not very good at math, please help him find this length.

### Input format

The first line of the input contains two integers N and K (1⩽K⩽N⩽2⋅105) - number of sheeps grazing in the field and the number of sheeps Jonathan wants to catch.

Each of the next N lines contain four integers xi,1, yi,1, xi,2, yi,2 (1⩽xi,1<xi,2⩽109, 1⩽yi,1<yi,2⩽109) - coordinates of bottom-left and top-right corners of the ith sheep’s pasture.

### Output format

Print one integer — the minimum length of the side of the square paddock such that at least K pastures fit inside it completely.

### Examples

#### Input

```
10 7
5 1 7 8
1 3 5 4
5 8 8 10
7 1 8 5
9 1 10 5
4 4 7 5
1 6 7 7
5 7 9 10
4 8 5 9
4 2 5 3
```

#### Output

```
9
```

#### Input

```
10 2
7 4 8 9
7 7 8 8
4 3 6 7
4 1 8 6
4 2 10 5
1 3 2 10
6 8 7 9
7 5 8 6
4 4 8 5
4 1 5 2
```

#### Output

```
7
```

### Notes

In the first example a square with side 9 covers 7 pastures completely, which is exactly what Jonathan needs. A square with side 8 covers only 6 of them.

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab03/j.py)