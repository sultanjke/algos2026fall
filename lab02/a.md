### Problem A: One-time guests

Jojo is watching a stream of lowercase Latin letters arrive one by one.

After every single letter that arrives, he wants to know the **first** letter of the stream so far that has occurred exactly once — “first” meaning the leftmost one among all letters that are still unique. If at that moment every letter seen so far has occurred more than once, the answer is −1.

Help Jojo answer this after each arrival.

### Input format

The first line contains one integer T — the number of test cases (1≤T≤200).

Each test case is given on two lines. The first of them contains one integer N — the length of the stream (1≤N≤500). The second contains N lowercase Latin letters separated by single spaces — the letters in the order they arrive.

### Output format

For each test case print one line with N answers separated by single spaces: the i\-th of them is the first non-repeating letter of the stream after the first i letters have arrived, or −1 if at that moment there is no such letter.

### Examples

#### Input

```
2
4
a a b c
3
a a c
```

#### Output

```
a -1 b b
a -1 c
```

#### Input

```
1
6
a d b c a a
```

#### Output

```
a a a a d d
```

### Notes

In the first test case the stream is a,a,b,c:

-   after “a” the only letter is a and it is unique — the answer is a;

-   after the second “a” the letter a has occurred twice, and there is nothing else — the answer is −1;

-   after “b” the unique letters are b only — the answer is b;

-   after “c” the unique letters are b and c, and b came first — the answer is b.

In the second test case the stream is a,d,b,c,a,a, and the answers are a, a, a, a, d, d.
