### Problem G: Cutting the Ropes

Aisha is preparing decorations for the university open day. She has n ropes; the i\-th of them is ai centimetres long.

For the decoration she needs exactly k pieces of rope, and all of them must be of the **same** length. A piece is always cut out of a single rope — ropes may not be tied together. Whatever is left over after cutting is simply thrown away, and it is fine to leave a whole rope untouched.

Aisha wants the pieces to be as long as possible. Find that length.

Note that the answer does not have to be an integer number of centimetres: the rope may be cut at any point.

### Input format

The first line contains two integers n and k — the number of ropes and the number of pieces Aisha needs (1≤n≤105, 1≤k≤105).

The second line contains n integers a1,a2,…,an — the lengths of the ropes in centimetres (1≤ai≤109).

### Output format

Print one real number — the greatest length such that k pieces of that length can be cut out of the ropes.

Your answer is accepted if its absolute or relative error does not exceed 10−6.

Print the answer with at least 9 digits after the decimal point (`printf("%.9f", ans)` in C++, `print(f"{ans:.9f}")` in Python): the default output of `cout « ans` keeps only 6 significant digits and is not enough.

### Examples

#### Input

```
4 11
802 743 457 539
```

#### Output

```
200.500000000
```

#### Input

```
3 3
5 5 5
```

#### Output

```
5.000000000
```

#### Input

```
3 4
5 5 5
```

#### Output

```
2.500000000
```

### Notes

In the first example the ropes are 802, 743, 457 and 539 centimetres long and 11 pieces are needed. With length 200.5 they give 4+3+2+2\=11 pieces, which is exactly enough. Any greater length yields fewer than 11 pieces.

In the second example three ropes of length 5 give exactly three pieces of length 5.

In the third example four pieces are needed. A length of 5 would give only three pieces, so the ropes have to be cut in half: at length 2.5 each rope yields two pieces, six in total, and no greater length works.

### Scoring

Group 1 (40 points): n≤1000.

Group 2 (60 points): no additional constraints.