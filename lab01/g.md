### Problem G: Balanced Sequence of Letters

You are given a string S consisting of lowercase Latin letters. Determine whether it is _balanced_.

A string is balanced if and only if it can be built by the following rules:

-   the empty string is balanced;

-   if the strings s and t are balanced, then their concatenation st is also balanced;

-   if the string s is balanced, then the string xsx is balanced for any lowercase Latin letter x.

For example, the string `abba` is balanced, but the string `abbb` is not.

### Input format

The only line contains the string S (1≤|S|≤105).

### Output format

Print “`YES`” if the string is balanced, and “`NO`” otherwise.

### Examples

#### Input

```
sbaabsss
```

#### Output

```
YES
```

#### Input

```
sbabasss
```

#### Output

```
NO
```

#### Input

```
baab
```

#### Output

```
YES
```

#### Input

```
abpa
```

#### Output

```
NO
```

### Notes

In the first example `sbaabsss` is the concatenation of `sbaabs` and `ss`. Here `sbaabs` is built as xsx with x\=s around the balanced string `baab`, and `ss` is built as xsx with x\=s around the empty string.

In the third example `baab` is built as xsx with x\=b around the balanced string `aa`.

The strings `sbabasss` and `abpa` of the second and fourth examples cannot be built by these rules.