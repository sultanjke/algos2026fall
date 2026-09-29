### Problem G: 197831. Killua and Hunter exam

While Gon is surviving on the Greed Island, Killua, after the first unsuccessful attempt to pass the hunter exam, decides to test himself again. This time one of his tasks is to find the maximum distance between any two vertices in a binary search tree. Since Killua is pretty bad at algorithms, he asks for your help.

### Input format

In the first line you will be given single number N (1≤N≤20000). Next line consists of N numbers, where ai (1≤ai≤109) represents the i-th number inserted to a binary search tree.

**If ai is already present in the tree, it is not inserted again** — the tree never contains two nodes with equal values.

**Subtasks**

1.  (30%) N≤100.

2.  (30%) N≤1000

3.  (40%) No additional constraints.

Every test is scored separately; the percentages above show the total weight of each group of tests.

### Output format

Print one single number — the maximum distance between any two vertices of the binary search tree. The distance between two vertices is **the number of vertices** on the path between them, so for a tree of one vertex the answer is 1.

### Examples

#### Input

```
9
11 5 3 2 1 7 9 8 13
```

#### Output

```
7
```

#### Input

```
5
1 2 4 3 5
```

#### Output

```
4
```

#### Input

```
7
4 2 6 5 1 3 7
```

#### Output

```
5
```

### Notes

In the first test, the answer is the distance between nodes 1 and 8.
