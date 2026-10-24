## G. Another one prefix function problem

Time limit: 1 s · Memory limit: 256 MB

The string s was written many times in a row, after which a substring was taken from the resulting string and given to you. Your task is to determine the minimum possible length of the original string s.

Input

The only line contains string s (1⩽|s|⩽50000), consisting of uppercase and lowercase Latin letters.

Output

Print one integer — the minimum possible length of the original string.

Note

The answer is the smallest period of the given string, and the prefix function gives it directly: for a string of length n the period equals n−π\[n−1\].

Examples

**Input 1**

```
zzz
```

**Output 1**

```
1
```

**Input 2**

```
bcabcab
```

**Output 2**

```
3
```
