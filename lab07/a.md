## Submit a solution for A-Simple Merge

|  |  |
| --- | --- |
| **Time limit:** | 2 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem A: Simple Merge

You are given T sets of strings. For every set print its strings ordered by length: shorter strings first. If two strings have the same length, they must keep their relative order from the input — the sorting must be **stable**.

### Input format

The first line contains one integer T (1≤T≤1000) — the number of sets.

Each of the next T lines describes one set and contains ki strings separated by single spaces (1≤ki≤105). Every string consists of lowercase Latin letters and has length between 1 and 50 inclusive.

The total number of strings over all sets does not exceed 2⋅105, and the total length of all strings does not exceed 106.

### Output format

Print exactly T lines. The i\-th line must contain all ki strings of the i\-th set separated by single spaces, ordered by non-decreasing length. Strings of equal length must be printed in the same relative order in which they occur in the input.

### Examples

#### Input

```
3
ab cd e j asd ljffg df
a a b b c c
xy yx zxy zx xzy xxx
```

#### Output

```
e j ab cd df asd ljffg
a a b b c c
xy yx zx zxy xzy xxx
```

#### Input

```
4
aabc ddfd fbbe f baaad
fddf badcf aedbe cdb ae bbd
ada bc eaced dadab b aabc fbee
bedaf edde fcaa adbf beec
```

#### Output

```
f aabc ddfd fbbe baaad
ae cdb bbd fddf badcf aedbe
b bc ada aabc fbee eaced dadab
edde fcaa adbf beec bedaf
```

### Notes

The intended solution is merge sort — a stable O(klog⁡k) sorting algorithm. Note that quick sort is **not** stable, so it cannot be used here without an additional tie-breaking key.

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab07/a.py)
