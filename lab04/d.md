### Problem D: 105816. Aureole

You are given a permutation of size n. Create an empty BST, and insert into BST values p1,p2,...,pn in this order. You need to find how many levels are there and the sum of values for each level.

### Input format

In the first line there is a single integer 1≤n≤5000 size of permutation. Second line contains n distinct numbers from 1 to n - the permutation.

### Output format

In the first line output k — the number of levels in the resulting BST. In the second line output k integers — the sum of values on each level, in order of increasing level, starting from level 0 (the root).

### Examples

#### Input

```
1
1
```

#### Output

```
1
1
```

#### Input

```
5
4 3 5 1 2
```

#### Output

```
4
4 8 1 2
```

### Notes

Level of vertex is defined as:

Level of root is 0, and level of each non-root vertex is (level of it’s parent) + 1.

In second testcase, BST looks like this.

<img width="600" height="215" alt="a" src="https://github.com/sultanjke/algos2026fall/blob/main/assets/lab04/d.jpg" />

There are 4 levels, and sum for each level is 4, 3 + 5, 1, 2.