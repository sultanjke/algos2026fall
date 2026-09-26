### Problem F: Robin Hood stealing the Gold

Robin Hood wants to steal the golden bars from the bank of High Sheriff aiming to distribute them to poor local people. There are N bags of golden bars, the i\-th bag has bags\[i\] bars. Sheriff has gone and will return in H hours.

Robin can steal K bars per hour. Each hour, he chooses a single bag of golden bars, and steals K bars from that bag. If there are less than K bars in the bag, he steals them all, and won’t steal any more during this hour.

Robin Hood wants to steal all of the golden bars before the Sheriff comes back.

Return the minimum number K such that Robin can steal ALL of the golden bars within H hours.

### Input format

The first line of the input contains two space-separated integers N(1≤N≤104),H(N≤H≤109), the number of bags of golden bars and the number of hours for which Sheriff has gone. The next line contains N space-separated integers (1≤bags\[i\]≤109) denoting the number of golden bars in each bag.

### Output format

Print the minimum number K such that Robin Hood can steal all of the N golden bars within the limit of H hours.

### Examples

#### Input

```
4 8
3 6 7 11
```

#### Output

```
4
```

#### Input

```
5 5
30 11 23 4 20
```

#### Output

```
30
```

#### Input

```
5 6
30 11 23 4 20
```

#### Output

```
23
```

### Notes

In the first example there are four bags with 3, 6, 7 and 11 bars and the Sheriff returns in 8 hours. With K\=4 Robin needs 1+2+2+3\=8 hours — exactly enough. With K\=3 he would need 1+2+3+4\=10 hours, which is too much, so 4 is the smallest suitable speed.

In the second example there are five bags and exactly five hours, so Robin gets one hour per bag and has to empty the largest bag in a single hour: the answer is 30.

In the third example he has one spare hour, which is enough to split the largest bag over two hours, and the answer drops to 23.

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab03/f.py)