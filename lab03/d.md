### Problem D: Win me if you can!

Mark is going to fight for Fight Club. There were N competitors with powers. There will be P rounds to fight and in each round Mark’s power will be changed. With power M, Mark can kill all the competitors whose power is equal to or less than his.  Round by round, all the competitors who are dead in the previous round will be reborn. Such that in each round there will be N competitors to fight. As Mark is tired, please, help him to count the number of competitors that he can win in each round and the total sum of their powers.

### Input format

The first line contains an integer N (1 ⩽ N ⩽ 2⋅105) - the number of competitors without Mark. Next line contains N integers ai (1 ⩽ ai ⩽ 103) - powers of these competitors. The third line contains one integer P (1 ⩽ P ⩽ 2⋅105) — the number of rounds. Each of the next P lines contains an integer pi (1 ⩽ pi ⩽ 103) — power of Mark at each round.

### Output format

On each of the P lines print two integers — how many competitors Mark beats in this round and the total sum of their powers.

### Examples

#### Input

```
7
7 9 1 8 2 6 2
2
4
8
```

#### Output

```
3 5
6 26
```

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab03/d.py)