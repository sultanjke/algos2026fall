## Submit a solution for D-Experiment with Mixtures

|  |  |
| --- | --- |
| **Time limit:** | 3 s |
| **Real time limit:** | 6 s |
| **Memory limit:** | 256M |

### Problem D: Experiment with Mixtures

Mark is making an experiment with mixtures of different densities. For his experiment he wants all of the mixtures to have a density ⩾m.

He uses the following formula to obtain a combined mixture: dnew = dleast + 2⋅dsecond least, where dnew is the density of the new mixture, dleast is the smallest density among all mixtures and dsecond least is the second smallest density among all mixtures.

Mark repeats the mixing until he gets all the mixtures with the density ⩾m.

You are given the densities of mixtures. How many times Mark should mix his mixtures to get the densities of all mixtures ⩾m?

### Input format

The first line consists of integers n and m (1⩽n⩽106, 0⩽m⩽109), the number of mixtures and the minimum required density correspondingly.

The next line contains n space-separated integers di (0⩽di⩽109) describing the densities of mixtures.

### Output format

Print the number of operations that are needed to make all the densities ⩾m. If it is impossible, print −1.

### Examples

#### Input

```
3 10
1 1 1
```

#### Output

```
-1
```

#### Input

```
6 7
1 2 3 9 10 12
```

#### Output

```
2
```

### Notes

The density of a combined mixture can reach about 3⋅109, which does not fit into a 32\-bit integer type — use 64\-bit integers.