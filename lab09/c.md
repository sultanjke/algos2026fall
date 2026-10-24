## C. Cyclic Shift

Time limit: 1 s · Memory limit: 256 MB

Tamerlan once wrote on a piece of paper a line consisting of large and small Latin letters, and then went to help Askar. When he returned, he found that his friend Alikhan had written another line of the same length under his line. Alikhan claims that he got his line by a cyclic shift of Tamerlan’s line a few steps to the right (a cyclic shift of the line `qwerty` by 2 positions to the right gives `ertyqw`). However, Alikhan is known for the fact that he can accidentally make a mistake in a large number of calculations, so Tamerlan is at a loss — whether to believe Alikhan?

Help him: find out by how many positions Alikhan’s line has to be cyclically shifted to the right in order to get Tamerlan’s line, or determine that this is impossible and Alikhan is mistaken.

Input

The first two lines of input data contain Tamerlan and Alikhan lines, respectively. The line lengths are the same, do not exceed 10000 and are not equal to 0.

Output

Print one integer — the smallest number of positions of a cyclic shift to the right that turns Alikhan’s line into Tamerlan’s line. If no shift gives Tamerlan’s line, print −1.

Note

A shift by 0 positions is allowed: if the two lines are already equal, the answer is 0.

The classic trick here is to glue Alikhan’s line to itself: every cyclic shift of it is a substring of the doubled line. So the task reduces to finding the first occurrence of Tamerlan’s line in the doubled one, which the prefix function does in linear time.

Examples

**Input 1**

```
zabcd
abcdz
```

**Output 1**

```
4
```

**Input 2**

```
abcde
decba
```

**Output 2**

```
-1
```
