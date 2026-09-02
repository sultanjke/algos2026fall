### Problem B: Binary Exponentiation

Compute a^n mod *m*.

The straightforward way — multiply a by itself n times — needs O(n) operations. For n up to 1018 that is hopeless: even at a billion multiplications per second it would take more than thirty years.

Binary exponentiation does the same job in O(log⁡n) multiplications. It is based on a simple observation: if n is even, then an\=(an/2)2, and if n is odd, then an\=a⋅an−1. For example, 210\=(25)2\=(2⋅24)2\=(2⋅(22)2)2 — only four multiplications instead of ten.

### Input format

The only line contains three integers a, n and m (1≤a≤1018, 0≤n≤1018, 1≤m≤109).

### Output format

Print a single integer — the value of anmodm.

### Examples

#### Input

```
2 10 1000000000
```

#### Output

```
1024
```

#### Input

```
5 0 1
```

#### Output

```
0
```

### Notes

In the first example 210\=1024, and 1024mod109\=1024.

In the second example m\=1. Every integer is divisible by 1, so the remainder is 0 — this holds for a0\=1 as well.