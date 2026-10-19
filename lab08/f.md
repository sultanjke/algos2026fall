## Submit a solution for F-Substrings

|  |  |
| --- | --- |
| **Time limit:** | 3 s |
| **Real time limit:** | 6 s |
| **Memory limit:** | 512M |

### Problem F: Substrings

You have string S and q queries. Each query given a pair of integers L and R; the answer for a query is number of times substring from L to R appears in S as substring.

### Input format

In first line given string S (1≤|s|≤2000).

In second line given integer q (1≤q≤5∗104).

Then next q lines contains queries, each query is two integer L and R (1≤L≤R≤|s|), substring you must to check.

### Output format

Print q lines with one single integer, answer for each query.

### Examples

#### Input

```
abracadabra
5
1 1
1 2
3 4
1 5
1 4
```

#### Output

```
5
2
2
1
2
```
