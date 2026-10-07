### Problem C: 111632. Christmas Gifts

Christmas is coming! Everyone is preparing gifts for their families. The Damir’s family is also preparing for this. The Damir’s family has many children, so the parents decided to buy n various gifts. Parents decided to number these gifts - i\-th as ai. They hang them on Christmas tree in socks, following the form binary search tree. In particular, they insert i\-th gift with the value ai following the rules of binary search tree.

As you know, Damir is the smallest among the whole family. Therefore, parents for the holiday allowed him to pick up his gift first. Damir knew that his gift has number k, but he mistakenly assumed that all the gifts below his gift were also intended for him. Now, parents are confused and want to find out what gifts Damir wants to grab for himself.

### Input format

The first line contains one integer n (1≤n≤103) — the number of gifts.

The second line contains n pairwise distinct integers ai (1≤ai≤103) — the numbers of the gifts in the order they are hung.

The third line contains one integer k (1≤k≤103). It is guaranteed that the array contains the number k.

### Output format

Print the numbers of the gifts of the subtree of k in **pre-order**: first the number of the current node, then the whole left subtree, then the whole right subtree. Print all the numbers in one line, separated by single spaces.

### Examples

#### Input

```
5
4 2 7 1 3
2
```

#### Output

```
2 1 3
```

### Notes

<img width="300" height="215" alt="a" src="https://github.com/sultanjke/algos2026fall/blob/main/assets/lab04/c.jpg" />

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab04/c.py)
