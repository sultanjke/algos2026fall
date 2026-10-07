## Submit a solution for E-K-th sum

| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem E: K-th sum

Nurdana loves cookies! She stores all the cookies in separate boxes, but mom allows her to store only k boxes. Her dad is an assistant in this matter. He gives her a box in which there are n cookies. Help her calculate how many cookies she can have?

### Input format

The first line contains two integers q and k (1 ≤ q, k ≤ 105). Each of the following q lines contains one command.

There are two types of commands:

-   _insert_ n - dad gives a box with n cookies (0⩽n⩽109)

-   _print_ - print the maximum number of cookies Nurdana can have

### Output format

For each query of type _print_ output, on a separate line, the sum of the k largest of the numbers inserted so far.

If fewer than k numbers have been inserted, output the sum of all of them; if nothing has been inserted yet, output 0.

Equal values are counted separately: if the value 5 was inserted three times and k⩾3, all three copies contribute to the sum.

### Examples

#### Input

```
6 4
print
insert 9
insert 6
print
insert 10
print
```

#### Output

```
0
15
25
```

#### Input

```
7 2
insert 2
insert 6
insert 3
print
print
insert 1
print
```

#### Output

```
9
9
9
```

### Notes

This problem must be solved using a heap.

Use long long type for the sum of elements.

Since k is fixed, you don’t need to store all numbers, only k largest elements.

The answer can be as large as 105⋅109\=1014, so a 32\-bit integer is not enough.