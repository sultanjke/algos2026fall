### Problem J: Boris vs Nursik

Boris and Nursik are playing the card game “drunkard”. All the cards are divided equally between the two players. On every move both players reveal the top card of their deck, and the one whose card is higher takes both revealed cards and puts them at the bottom of their own deck. The player who is left without cards loses.

The winner of a move first puts Boris’s card at the bottom of the deck and then Nursik’s card, so Nursik’s card ends up lowest.

The game is played with 10 cards with values from 0 to 9. A larger card beats a smaller one, with a single exception: the card 0 beats the card 9.

Write a program that simulates the game and determines the winner.

### Input format

The first line contains 5 integers separated by spaces — Boris’s cards. The second line contains Nursik’s 5 cards in the same format.

Every card value is an integer between 0 and 9, and all 10 values are distinct. The cards are listed from top to bottom, that is, each line starts with the card that will be revealed first.

### Output format

Print the word `Boris` or `Nursik` — the name of the winner — followed by the number of moves made before the win.

It can be shown that with 10 distinct cards the game always ends: no deal leads to an infinite loop.

### Examples

#### Input

```
1 3 5 7 9
2 4 6 8 0
```

#### Output

```
Nursik 5
```

### Notes

In the example Boris holds \[1,3,5,7,9\] and Nursik holds \[2,4,6,8,0\]. Nursik wins the first four moves (2\>1, 4\>3, 6\>5, 8\>7), and on the fifth move Boris’s last card 9 loses to 0 by the special rule. Boris is left without cards, so Nursik wins after 5 moves.
