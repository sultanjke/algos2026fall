## E. KH2O - potassium hydroxide???

Time limit: 1 s · Memory limit: 256 MB

One minion is learning chemistry but its going to be so hard. One day when he was doing an experiment with potassium and oxygen, he accidentally blew up the flask. Now this time he wants to be careful with the elements. It has an adjacency matrix where it is written which element can be added with which, and which cannot be added. The teacher gave him q different requests where each request has 3 chemical elements, it is necessary to say whether it is possible to add these 3 elements so that the flask does not explode.

Input

The first line contains two integers n, q (1≤n≤1000,1≤q≤100000) — the number of elements and number of queries.

The next n lines contains n integers a\[i\]\[j\], that means element i can be added to element j if a\[i\]\[j\] = 1 and if a\[i\]\[j\] = 0 they cannot be added.

Output

Print “YES” if we can add 3 elements, otherwise print “NO”.

Examples

**Input 1**

```
4 4
1 1 0 1
1 1 1 1
0 1 1 0
1 1 0 1
1 2 4
2 3 4
1 2 2
3 3 4
```

**Output 1**

```
YES
NO
YES
NO
```
