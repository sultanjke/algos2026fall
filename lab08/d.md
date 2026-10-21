## Submit a solution for D-108995. Restore the string

|  |  |
| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem D: 108995. Restore the string

Jonathan tried to write Rabin-Karp algorithm. He had a string S and he used the following formula to calculate hash of string: ∑i\=0|S|−1(Si−97)⋅2i Thus, he has written hashes of all prefixes of string S. Unfortunately, Jonathan forgot his string S. So, he asked your help in restoring this string.

### Input format

The first line of the input contains the only integer N - the length of string S (1 ⩽ N ⩽ 50).

The second line contains N integers pi - hashes of all prefixes of string S.

It is guaranteed that each hash does not exceed 2⋅1018.

### Output format

Print the string S.

### Examples

#### Input

```
5
7 15 59 147 371
```

#### Output

```
hello
```

#### Input

```
5
22 50 118 206 254
```

#### Output

```
world
```

### Notes

Use larger integer data structures (like “long long” In C++).

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab08/d.py)
