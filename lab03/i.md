### Problem I: Oshiete oshiete yo sono shikumi wo

There is only one road and n houses in the Tokyo, and all the houses are on this road. House numbered from 1 to n and appear in this order. There are ai ghouls living in the i−th house. Due to the RC-cells infection, k−1 roadblocks need to be installed between houses in Tokyo, so that k blocks of houses are detached. Kaneki Ken wants to divide ghouls so that the maximum number of ghouls over blocks (consecutive houses detached by roadblocks) is minimal. Help Kaneki find this number.

Subtasks
1\. (20%) n≤100
2\. (30%) n≤1000
3\. (50%) other tests

### Input format

The first line contains integers n and k (1≤k≤n≤105). The second line contains the elements of the array ai (1≤ai≤109).

### Output format

Print one integer — the minimum possible maximum number of ghouls in a block.

Note that the answer does not always fit into a 32\-bit integer type.

### Examples

#### Input

```
10 3
3 4 2 1 3 4 5 2 2 3
```

#### Output

```
12
```

#### Input

```
10 4
3 1 2 4 10 8 4 2 5 3
```

#### Output

```
12
```

#### Input

```
2 1
399265 867718
```

#### Output

```
1266983
```

### Notes

In the first example: (3+4+2+1), (3+4+5), (2+2+3)

### Scoring

Group 1 (20 points): n≤100.

Group 2 (30 points): n≤1000.

Group 3 (50 points): no additional constraints.