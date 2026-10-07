## Submit a solution for B-Rock Game

|  |  |
| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem B: Rock Game

We have a collection of rocks, each rock has a positive integer weight.

With each turn, we choose the two **heaviest** rocks and smash them together. Suppose the stones have weights x and y with x⩽y. If x\=y, both stones are totally destroyed. If x≠y, the stone of weight x is totally destroyed, and the stone of weight y has a new weight y−x.

At the end, there is at most 1 stone left. Output the weight of this stone (or 0 if there are no stones left).

### Input format

The first line contains integer N (1⩽N⩽105) - the number of stones.

The second line contains N integers ai (1⩽ai⩽109) - the weights of each stone.

### Output format

Print the weight of the remaining stone, or 0 if no one left.

### Examples

#### Input

```
6
2 7 4 1 8 1
```

#### Output

```
1
```

### Notes

We combine 7 and 8 to get 1 so the array converts to \[2,4,1,1,1\] then, we combine 2 and 4 to get 2 so the array converts to \[2,1,1,1\] then, we combine 2 and 1 to get 1 so the array converts to \[1,1,1\] then, we combine 1 and 1 to get 0 so the array converts to \[1\] then that’s the value of last stone.