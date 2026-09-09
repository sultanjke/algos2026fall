### Problem H: Ragnarok

Thor keeps a chronicle of the days before Ragnarok. Every day is written down as a number: a good day is a positive number, a bad day is a negative one. The chronicle is stored as a **singly linked list** — each day only knows which day comes after it.

Thor wants to find the best stretch of the chronicle: a non-empty run of **consecutive** days whose numbers add up to the largest possible sum. Print that sum.

### Input format

The first line contains one integer n — the number of days in the chronicle (1≤n≤100).

The second line contains n integers a1,a2,…,an — the days in the order they are stored in the list, from its head to its tail (−104≤ai≤104).

### Output format

Print one integer — the largest sum over all non-empty runs of consecutive days.

### Examples

#### Input

```
5
1 2 -1 4 5
```

#### Output

```
11
```

#### Input

```
3
-1 -1 -1
```

#### Output

```
-1
```

#### Input

```
10
5 1 2 -10 5 3 9 -5 10 10
```

#### Output

```
32
```

### Notes

In the first example the best run is the whole chronicle: 1+2−1+4+5\=11.

In the second example every day is bad, so the best you can do is take a single day: −1. Note that the run must be non-empty — the answer is never 0 here.

In the third example the best run is 5+3+9−5+10+10\=32.