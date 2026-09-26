### Problem A: Binary search

You are given a sorted array and a number x. Determine whether x occurs in the array.

This is the warm-up for the technique: the array here is small, but write the search so that it halves the range at every step rather than scanning the elements one by one — the same code will be needed later on arrays where scanning is far too slow.

### Input format

The first line contains one integer n — the size of the array (1≤n≤100).

The second line contains n integers a1≤a2≤…≤an — the elements of the array in non-decreasing order (1≤ai≤20000). Equal elements are allowed.

The third line contains one integer x — the number to look for (−20000≤x≤20000).

### Output format

Print `Yes` if x occurs in the array, and `No` otherwise.

### Examples

#### Input

```
5
1 2 3 4 5
1
```

#### Output

```
Yes
```

#### Input

```
5
1 2 3 4 5
2
```

#### Output

```
Yes
```

#### Input

```
5
1 2 3 4 5
7
```

#### Output

```
No
```

#### Input

```
5
1 2 3 4 5
10
```

#### Output

```
No
```

#### Input

```
5
1 2 3 4 5
5
```

#### Output

```
Yes
```

### Notes

In the first example x\=1 is the very first element of the array, so the answer is `Yes`.

In the third example x\=7 is greater than every element, so the answer is `No`.

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab03/a.py)