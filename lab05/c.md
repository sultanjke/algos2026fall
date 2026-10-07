## Submit a solution for C-Standard problem about soccer

|  |  |
| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem C: Standard problem about soccer

Kakyoin loves football and he goes to the final of the World Cup. At the stadium, he noticed that there are n rows, each can accommodate a distinct number of people. The price of the ticket depends on the row. If there are k (k > 0) free seats in the row, then the price of one ticket will be equal to k. What is the maximum amount of money stadium management can get if there are x people in line for a ticket?

### Input format

The first line consists of n and x (1⩽n,x⩽105). n denotes the number of seating rows in the stadium and x denotes the number of football fans waiting in line to get a ticket for the match.

Next line consists of n space separated integers a1, a2, a3, ..., an where ai (1⩽ai⩽105) denotes the number of empty seats initially in the i\-th row.

It is guaranteed that there are enough free seats for all visitors.

### Output format

Print one integer - the maximum amount of money the stadium can earn.

### Examples

#### Input

```
3 10
6 8 9
```

#### Output

```
67
```

#### Input

```
1 2
5
```

#### Output

```
9
```

### Notes

The answer may exceed the maximum value of a 32\-bit integer — use 64\-bit integers.