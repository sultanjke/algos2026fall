## Submit a solution for C-Sorter

|  |  |
| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem C: Sorter

Almas loves to sort numbers with specific rules that he comes up with himself. Today he wants to sort rows, each row contain m integer elements. He decided to sort rows in decreasing order of their sum, i.e. the row with larger sum will be the first. In case the sums are equal, then he order rows lexicographically, i.e. The row with least first element will be the first, if first elements are equal, then compare second element, third element, etc. He successfully finished sorting. He wanted to put the result in the closet, but accidentally put it in the shredder and divided everything into rows again. Help him sort it again.

### Input format

The first line contains two numbers, n and m the number of rows and number of elements in a row. The next n lines contain m numbers, elements of each row.

-   1≤n,m≤500

-   0≤row\[i\]≤5000

### Output format

Print rows in desired sorted order.

### Examples

#### Input

```
5 3
1 2 3
1 2 4
1 3 2
6 0 0
2 3 2
```

#### Output

```
1 2 4
2 3 2
1 2 3
1 3 2
6 0 0
```

#### Input

```
2 3
16 3 18
5 10 8
```

#### Output

```
16 3 18
5 10 8
```

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab07/c.py)
