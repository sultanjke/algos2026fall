### Problem E: Delete the Middle Node

The scoreboard of a relay race is kept as a **singly linked list** of runners, in the order they crossed the finish line.

One of the runners turned out to be a pacemaker who was never part of the competition, and by the rules of this race the pacemaker always finishes exactly in the middle. If the scoreboard holds n runners, numbered 0,1,…,n−1 starting from the head of the list, the pacemaker is the runner with number ⌊n/2⌋.

Remove that runner from the list and print what is left of the scoreboard.

### Input format

The first line contains one integer n — the number of runners on the scoreboard (1≤n≤2⋅105).

The second line contains n integers a1,a2,…,an — the identifiers of the runners, listed from the head of the list to its tail (−109≤ai≤109).

### Output format

Print the n−1 remaining identifiers separated by single spaces, from the head of the list to its tail.

If n\=1, the list becomes empty — print an empty line.

### Examples

#### Input

```
5
10 20 30 40 50
```

#### Output

```
10 20 40 50
```

#### Input

```
4
1 2 3 4
```

#### Output

```
1 2 4
```

#### Input

```
1
42
```

#### Output

### Notes

In the first example n\=5, so the runner to remove is the one with number ⌊5/2⌋\=2, that is the value 30.

In the second example n\=4 and ⌊4/2⌋\=2, so the value 3 is removed. Note that for an even length the node to remove is the **second** of the two middle ones.

In the third example the scoreboard holds a single runner, who is removed, and the output is empty.