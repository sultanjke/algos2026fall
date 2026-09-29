### Problem A: 111284. Mountains

You are going to hike in the mountains. You have written directions (left or right) on a piece of paper, in which direction you need to turn on each of the branches of the path, following which you can reach the peak. In the mountains there are several peaks and you have recorded the path to each peak. Since you are a guide, you need to check the day before the hike which of the recorded paths is available. All paths start at one point at the foothills.

The path is presented in the form of "RRLLRLR", which means to reach the peak you need to turn right at the beginning, then right again, then left, left, right, left, right. Peak located after last turn and it is possible that it does not exist. You are given all the paths in the mountains that are available in the form of a Binary Search Tree and the paths to the peaks that are written on a piece of paper. You need to tell which of the paths written on the piece of paper is available.

<img width="600" height="215" alt="a" src="assets/a.jpg" />

### Input format

The first line contains two integers N and M (1≤N≤105, 1≤M≤2⋅104) — the number of nodes of the tree and the number of paths written on the piece of paper.

The second line contains N integers a1,a2,…,aN (1≤ai≤109) — the values that are inserted one by one, in this order, into an initially empty binary search tree. A value equal to the value of the current node goes to the left subtree.

Each of the next M lines contains one path pi (2≤|pi|≤100) — a string consisting only of the characters ’L’ and ’R’. The total length of all paths does not exceed 2⋅106.

### Output format

Print M lines, in the same order as the paths are given. The ith line should contain "YES" if the path pi leads to an existing node of the tree, and "NO" otherwise.

### Examples

#### Input

```
9 4
7 10 12 8 5 6 2 1 4
LLL
LRR
RL
RR
```

#### Output

```
YES
NO
YES
YES
```