### Problem G: Jonathan the Poet

Jonathan the Poet has just finished a new poem, but something about the rhyme feels off. He is convinced that shifting the poem cyclically by K positions will fix it.

The poem is stored as a **singly linked list** of words: every word knows only which word comes after it. A cyclic shift by K moves the first K words to the very end, keeping their order, so the poem

w1 w2 … wK wK+1 … wN

turns into

wK+1 … wN w1 w2 … wK.

Jonathan is tired. Help him and print the shifted poem.

### Input format

The first line contains two integers N and K — the number of words in the poem and the size of the shift (1≤K<N≤105).

The second line contains N words separated by single spaces. Every word is a non-empty string of lowercase Latin letters, and the total length of all words does not exceed 3⋅105.

### Output format

Print the N words of the shifted poem, separated by single spaces.

### Examples

#### Input

```
5 2
the show must go on
```

#### Output

```
must go on the show
```

#### Input

```
5 3
another one bites the dust
```

#### Output

```
the dust another one bites
```

### Notes

In the first example N\=5 and K\=2: the first two words, “the” and “show”, move to the end.

In the second example K\=3, so “another one bites” moves to the end and the poem starts with “the dust”.