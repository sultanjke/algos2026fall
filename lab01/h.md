### Problem H: Nugman and Stack

One day Nugman was solving the problems of LAB1 and managed to finish almost all of them. Only one problem was left, and it would not give in — so Nugman asks for your help.

There are N people standing in a queue, and the i\-th of them is ai years old. The queue starts at position 1. Every person wants to know the age of the closest person standing before them who is **strictly younger** — that is, the nearest position to the left holding a strictly smaller age. If there is no such person, the answer is −1.

### Input format

The first line contains a single integer N (1≤N≤105) — the number of people in the queue.

The second line contains N integers a1,a2,…,aN (1≤ai≤109) — the ages of the people, listed from the front of the queue to the back.

### Output format

Print N integers separated by spaces, where the i\-th of them is the answer for the i\-th person.

### Examples

#### Input

```
5
2 1 5 8 3
```

#### Output

```
-1 -1 1 5 1
```

#### Input

```
5
1 2 3 4 5
```

#### Output

```
-1 1 2 3 4
```

### Notes

In the first example the queue is \[2,1,5,8,3\]. The first two people have nobody strictly younger before them. For the third person (age 5) the nearest smaller age to the left is 1; for the fourth (age 8) it is 5; for the fifth (age 3) the ages 8 and 5 are too large, so the answer is 1 again.

In the second example the ages increase, so every person sees the one standing directly in front of them.

Equal ages do not count. For the queue \[3,1,2,2\] the answer is \[−1,−1,1,1\]: for the fourth person the third one has the same age, not a smaller one.