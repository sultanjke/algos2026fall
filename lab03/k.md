### Problem K: Snake

Write a program that, for several given values, prints their coordinates in a _snake_ array of size n×m.

A snake array is filled like this:

-   every column strictly decreases from top to bottom: aij\>a(i+1)j;

-   every **even** row strictly decreases from left to right: aij\>aik for j<k;

-   every **odd** row strictly increases from left to right: aij<aik for j<k.

Rows are numbered from 0 to n−1 from top to bottom, columns from 0 to m−1 from left to right.

Here is an example of 3×4 Snake array

25 23 20 19

13 15 17 18

12 10 9 8

### Input format

The first line of input contains a single integer t — the number of values whose coordinates you must find (1≤t≤104).

The next line contains t integers — the values themselves (−107≤ each value ≤107).

The next line contains two integers n and m — the number of rows and the number of columns (1≤n,m≤800).

Each of the next n lines contains m integers — the snake array itself (−107≤aij≤107, 0≤i<n, 0≤j<m). It is guaranteed that the array really is a snake array.

### Output format

Print t lines, one per requested value, in the order the values are given.

For a value that occurs in the array print two integers — the number of its row and the number of its column. **Rows and columns are numbered from zero.** If the value does not occur in the array, print −1 instead.

### Examples

#### Input

```
5
10 15 13 8 23
3 4
25 23 20 19
13 15 17 18
12 10 9 8
```

#### Output

```
2 1
1 1
1 0
2 3
0 1
```

#### Input

```
8
1 7 17 12 6 15 18 20
5 5
25 24 23 22 21
16 17 18 19 20
15 14 13 12 11
6 7 8 9 10
5 4 3 2 1
```

#### Output

```
4 4
3 1
1 1
2 3
3 0
2 0
1 2
1 4
```

#### Input

```
4
-2 7 8 4
2 3
9 8 5
-1 3 4
```

#### Output

```
-1
-1
0 1
1 2
```

### Notes

In the third example, the elements -2 and 7 is do not exist. Therefore, you should print -1.

In the first example the value 10 stands in row 2 and column 1: rows and columns are numbered from zero, so the top-left corner is (0,0).

### Scoring

Group 1 (40 points): small arrays.

Group 2 (40 points): larger arrays.

Group 3 (20 points): the smallest array 1×1 and the largest array 800×800.