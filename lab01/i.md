### Problem I: Royal Flush

You are in a casino and the croupier offers you a game. There is a deck of N cards numbered from 1 to N, and the croupier shows you a trick:

-   take the top card and put it at the bottom of the deck;

-   take the new top card — it turns out to be the card numbered 1 — and put it aside;

-   take the top two cards and move them to the bottom of the deck, one by one;

-   take the new top card — it turns out to be the card numbered 2 — and put it aside;

-   …

-   repeat until no cards are left.

In other words, at step i the croupier moves i cards from the top to the bottom one by one and then puts the new top card aside, and that card must be the card numbered i.

Note that at step i the deck may contain fewer than i cards. In that case some cards are moved to the bottom several times, see the notes.

You are asked to repeat the trick. Find an initial arrangement of the deck that makes it work.

### Input format

The first line of the input contains the number of test cases T (1≤T≤100). Each of the next T lines contains a single integer N (1≤N≤1000) — the size of the deck for that test case.

### Output format

For each test case print N space-separated integers on a separate line — the order of the deck from the top card to the bottom one.

It can be shown that such an arrangement always exists, so you never have to report that the trick is impossible.

### Examples

#### Input

```
2
4
5
```

#### Output

```
2 1 4 3
3 1 4 5 2
```

#### Input

```
3
5
6
6
```

#### Output

```
3 1 4 5 2
4 1 6 3 2 5
4 1 6 3 2 5
```

### Notes

In the first test case of the example the deck \[2,1,4,3\] is processed as follows:

-   the initial deck is \[2,1,4,3\];

-   move one card to the bottom: \[1,4,3,2\];

-   put the card 1 aside: \[4,3,2\];

-   move two cards to the bottom, one by one: \[2,4,3\];

-   put the card 2 aside: \[4,3\];

-   move three cards to the bottom, one by one: \[4,3\]→\[3,4\]→\[4,3\]→\[3,4\];

-   put the card 3 aside: \[4\];

-   move four cards to the bottom — the only remaining card just returns to its place — and put the card 4 aside: the deck is empty.
