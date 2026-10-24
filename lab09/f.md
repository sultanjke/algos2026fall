## F. Simple KMP

Time limit: 1 s · Memory limit: 256 MB

Given two strings s1 and s2, find whether s1 is a substring of s2 and print indices of occurrences.

Input

Next two lines contain strings s1 (1⩽|s1|⩽105) and s2 (1⩽|s2|⩽105).

Output

In the first line print a single integer - the number of occurrences of string s1 in string s2. In the second line print indices of occurrences.

Note

Solve this task using Knuth-Morris-Pratt algorithm.

Examples

**Input 1**

```
abacaba
aba
```

**Output 1**

```
2
1 5
```