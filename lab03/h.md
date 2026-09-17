### Problem H: K-subarray

You are given an array of non negative integers and a number k. Let’s define subarray as a non-empty _consecutive_ elements of an array. Among all subarrays of the given array, find the one, such that sum of its elements is no less than k and such that this subarray would contain minimum possible number of elements.

### Input format

First line contains two space separated numbers n k — number of elements in given array and number that was mentioned above, respectively (1≤n≤105, 0≤k≤109).

Second line contains n space separated numbers a1,a2,...,an — given array (0≤ai≤104).

It is guaranteed that at least one subarray’s sum is not less than k.

### Output format

Output a single integer x — the number of elements in the shortest subarray whose sum is not less than k.

### Examples

#### Input

```
3 12
3 5 7
```

#### Output

```
2
```

#### Input

```
6 19
3 6 1 4 5 2
```

#### Output

```
5
```

### Notes

In the first test case we have three elements. Subarrays are \[3\], \[3,5\], \[3,5,7\], \[5\], \[5,7\], \[7\]. Only two subarrays have sum that is not less than k\=12: \[3,5,7\], \[5,7\]. Out of these two subarrays, \[5,7\] has minimum possible length of 2.

**Hint**

For a fixed left end of subarray, sums of subarray increase, if we increase number of elements in it. So we can do binary search on right end of subarray for a fixed left end.

In order to quickly know sum of subarray we can calculate prefix sums. For example for the given array from the first test case prefix sums would be \[3,8,15\]. In order to get sum of second and third element, from prefix sum at position 3 we subtract prefix sum at position 1: 15−3\=12.

### Scoring

Group 1 (40 points) and group 2 (52 points): random and adversarial tests.

Group 3 (8 points): corner cases (k\=0, answer equal to 1, answer equal to n).