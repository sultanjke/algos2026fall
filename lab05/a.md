## Submit a solution for A-Optimizing Program

|  |  |
| --- | --- |
| **Time limit:** | 2 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem A: Optimizing Program

The ICPC finals will be held soon, so Yergeldi and his team needs your help. While they were preparing for the competition, they faced an interesting task. You have a list of length N which consists of arrays of given lengths. You have one single operation, you can take any two arrays and merge them into one, the cost of the operation is equal to the sum of their lengths. As a result, you will have a list of N - 1 arrays. The process repeats until there is only one final array left. Find out for what minimum cost it is possible to combine all arrays.

### Input format

The first line contains an integer n (1⩽n⩽2⋅105), the size of the list a. The next line contains n positive integers a1, a2, ..., an (1⩽ai⩽2⋅105), representing the sizes of arrays in the list a.

### Output format

Print a single integer - the minimum cost of operations.

### Examples

#### Input

```
4
6 5 3 9
```

#### Output

```
45
```

#### Input

```
10
42 18 63 26 19 15 11 29 26 24
```

#### Output

```
869
```

### Notes

Explanation for the first test case:

\[6, 5, 3, 9\] –> First, merge arrays of lengths 5 and 3 that will cost 8.

\[6, 8, 9\] –> Next, merge arrys of lengths 6 and 8 that will cost 14.

\[14, 9\] –> Finally, merge the remaining two arrays that will cost 23.

Therefore, the total cost for merging all arrays is 8 + 14 + 23 = 45.