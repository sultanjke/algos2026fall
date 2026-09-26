### Problem C: Debugging

Jonathan almost finished his project by Object-Oriented Programing course. His code consists of N consecutive blocks, each of them consists of a certain amount of lines. Unfortunately, Jonathan made a lot of mistakes. Compiler showed that Jonathan made M mistakes, each of them is described by the number of line where this mistake was made. To debug his project faster, Jonathan wants to define number of block in which he made a mistake. Please, help Jonathan debug his project before deadline will expire.

### Input format

First line consists of integers N and M - number of blocks and mistakes (1 ⩽ N, M ⩽ 2 ⋅ 105).

The second line contains N integers ai - number of lines in the ith block (1 ⩽ ai ⩽ 104).

Each of the next M lines contains one integer bi - number of line where the ith mistake was made (1 ⩽ bi ⩽ a1+a2+…+aN). In other words, every mistake is guaranteed to fall inside the code, so the answer always exists.

### Output format

Print M lines, the ith line must contain the number of block in which the ith mistake was made.

### Examples

#### Input

```
2 1
3 4
5
```

#### Output

```
2
```

#### Input

```
3 3
5 7 6
5
10
15
```

#### Output

```
1
2
3
```

### Notes

In the first sample lines \[1, 3\] belong to the first block and lines \[4, 7\] to the second. So, Jonathan will find mistake at the fifth line at the second block.

In the second sample lines \[1, 5\], \[6, 12\], \[13, 18\] belong to the first, second and third blocks respectively. So, the fifth line is inside first block, the tenth line is inside second block and the fifteenth line is inside third block.

**Hint**: Think about inplementing binary search function to solve this problem.

**Hint**: Build a new array P, where Pi is the line at which ith block ends. You can notice, that this array is sorted.

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab03/c.py)