## Submit a solution for C-Dominating Patterns

|  |  |
| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem C: Dominating Patterns

The archaeologists are going to decipher a very mysterious “language”. Now, they know many language patterns. Each pattern can be treated as a string of lowercase Latin letters. There is a large text they want to analyze. What matters most is that which patterns are the _dominating patterns_. _Frequency_ of the pattern is the number of its appearances in the text as a substring. Pattern is dominating if the frequency the pattern is is not less than the frequency of any other pattern. It is your job to find all dominating patterns.

### Input format

The input consists of multiple test cases.

The first line of each test case is an integer N (1≤N≤150) - the number of patterns. Each of the following N lines contain single string of length in range \[1,70\] - patterns. The next line contains a single string of length in range \[1,105\] - text.

At the end of the input file there is a 0 indicating the end of an input file.

### Output format

For each test case, output the dominating patterns. If there are several dominating patterns, output them in order they appear in the input.

### Examples

#### Input

```
2
aba
bab
ababababac
6
beta
alpha
haha
delta
dede
tata
dedeltalphahahahototatalpha
0
```

#### Output

```
4
aba
2
alpha
haha
```

### Notes

In the first test case, the frequency of pattern aba is 2, and of pattern bac is 1.

In the second test case, the frequency of patterns alpha and haha is 2, and all other patterns has frequency not exceeding 1.
