## Submit a solution for B-House of love

|  |  |
| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem B: House of love

Once upon a time, in one university, created a one organization called "House of love" in which friendship is the main value. So they created one test to know level of their friendship. Two person write some numbers and gives it to you, to check common numbers.

### Input format

The first line contains two integers n and m (0≤n,m≤105) — the sizes of the two arrays.

The second line contains n integers — the numbers of the first person, and the third line contains m integers — the numbers of the second person (|ai|≤109). If an array is empty, the corresponding line is empty or absent.

### Output format

Print the numbers that occur in both arrays, **in non-decreasing order**, separated by spaces.

A number that occurs x times in the first array and y times in the second one must be printed exactly min(x,y) times. If there are no common numbers, print an empty line.

### Examples

#### Input

```
4 2
1 2 2 1
2 2
```

#### Output

```
2 2
```

#### Input

```
3 5
4 9 5
4 3 2 1 9
```

#### Output

```
4 9
```

#### Input

```
0 1
1
```

#### Output

```
```