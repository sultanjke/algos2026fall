## A. Substring of a Repeated String

Time limit: 1 s · Memory limit: 256 MB

Given two strings `A` and `B`. Your task is to find the minimum number of times `A` has to be repeated such that `B` is a substring of it. If `B` cannot be found in `A` after it’s extension, return −1. If `A` already contains `B`, the number of repetitions is equal to one by default.

Input

Input contains two lines: the first line contains the string A, the second line contains the string B. Both strings consist of lowercase and uppercase Latin letters, and their lengths are between 1 and 3⋅105.

Output

Print the minimum number of repetitions of A such that B is a substring of the result. If B can never be a substring, no matter how many times A is repeated, print −1.

Note

For the first test case, answer is 3, because by repeating `A` three times (‘abcdabcdabcd‘), `B` is a substring of it. For the second case, we do not extend the string `A` and `B` is a substring of `A`. Number of repetitions of `A` is 1.

Examples

**Input 1**

```
abcd
cdabcdab
```

**Output 1**

```
3
```

**Input 2**

```
aaa
a
```

**Output 2**

```
1
```