### Problem A: Greatest Common Divisor

Nurlan is helping his younger brother with a homework problem: given two positive integers a and b, find their **greatest common divisor** — the largest positive integer that divides both of them.

His brother wrote a straightforward program: check every integer from min(a,b) down to 1 and stop at the first common divisor. For gcd(12,18) it works fine — at most 12 checks. For gcd(1000000007,1000000009) it already has to check about a billion numbers, and for the values in this problem it would never finish at all.

Help Nurlan and write a program that is fast enough.

### Input format

The only line contains two integers a and b (1≤a,b≤1018).

### Output format

Print a single integer — the greatest common divisor of a and b.

### Examples

#### Input

```
1000000007 1000000009
```

#### Output

```
1
```

#### Input

```
12 18
```

#### Output

```
6
```

### Notes

In the first example both numbers are prime, so their only common divisor is 1.

In the second example 12\=2⋅2⋅3 and 18\=2⋅3⋅3, so the largest common divisor is 2⋅3\=6.
