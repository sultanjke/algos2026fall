### Problem F: Equal Strings

You are given two strings typed on a keyboard. Each string consists of lowercase English letters and the # symbol, where # means that the backspace key was pressed: it deletes the last character typed so far. If backspace is pressed when nothing has been typed yet, nothing happens.

Determine whether the two strings produce the same text.

### Input format

The first line contains the string s1 and the second line contains the string s2 (1≤|s1|,|s2|≤105).

Both strings consist of lowercase English letters and the # symbol.

### Output format

Print “`Yes`” if the two strings produce the same text, and “`No`” otherwise.

### Examples

#### Input

```
abc##
a#b#a
```

#### Output

```
Yes
```

#### Input

```
ab#c
ad#c
```

#### Output

```
Yes
```

#### Input

```
a#c
bb##
```

#### Output

```
No
```

### Notes

In the first example `abc##` becomes `a`, and `a#b#a` also becomes `a`, so the answer is `Yes`.

In the second example `ab#c` becomes `ac` and `ad#c` becomes `ac`.

In the third example `a#c` becomes `c`, while `bb##` becomes the empty text, so the answer is `No`.