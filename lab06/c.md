## Submit a solution for C-Points in Proximity

|  |  |
| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem C: Points in Proximity

You are given a list of integer points in a line. Find the pair of points with the least absolute difference. If there are more than one pairs output them all.

### Input format

The first line contains an integer N(2≤N≤2×105), number of points. The next line represents N integer numbers (−107≤points\[i\]≤107) denoting the points in a line.

### Output format

Sort the points. Print all pairs of **neighbouring** points of the sorted sequence whose difference is the smallest one, in non-decreasing order: for every such pair print its two points one after another. All numbers are printed in one line, separated by single spaces.

If several points are equal, each neighbouring pair of them is printed separately.

### Examples

#### Input

```
6
-20 -3916237 -357920 -362060 30 6246457
```

#### Output

```
-20 30
```