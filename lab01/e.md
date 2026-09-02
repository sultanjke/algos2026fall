### Problem E: Prime Factorization

Every integer greater than 1 can be written as a product of prime numbers, and this representation is unique up to the order of the factors. For example, 60\=2⋅2⋅3⋅5 and 210\=2⋅3⋅5⋅7.

Given an integer n, print its prime factorization.

Trying every divisor from 2 to n is far too slow for n up to 1012. A much smaller bound is enough — but be careful: once you stop, what is left of n may still be a prime factor that has to be printed.

### Input format

The only line contains a single integer n (2≤n≤1012).

### Output format

Print the prime factors of n in non-decreasing order, separated by single spaces. If a prime divides n several times, print it that many times.

### Examples

#### Input

```
60
```

#### Output

```
2 2 3 5
```

#### Input

```
210
```

#### Output

```
2 3 5 7
```

#### Input

```
999999999989
```

#### Output

```
999999999989
```

### Notes

In the first example 60\=2⋅2⋅3⋅5, and in the second one 210\=2⋅3⋅5⋅7.

In the third example n is a prime number, so its factorization consists of n itself.