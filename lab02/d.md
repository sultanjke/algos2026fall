### Problem D: Reverse the Linked List

Aisha is writing a music player. The playlist is stored as a **singly linked list**: every song knows only which song comes after it, and nothing about the song before it.

She has just added a `Play in reverse` button. The player cannot step backwards — it can only follow next pointers — so pressing the button has to rebuild the list itself, turning every next pointer around.

Given a playlist, print it the way the player will see it after the button is pressed.

### Input format

The first line contains one integer n — the number of songs in the playlist (1≤n≤2⋅105).

The second line contains n integers a1,a2,…,an — the identifiers of the songs, listed from the head of the list to its tail (−109≤ai≤109).

### Output format

Print n integers separated by single spaces — the identifiers of the songs from the head of the reversed list to its tail.

### Examples

#### Input

```
5
1 2 3 4 5
```

#### Output

```
5 4 3 2 1
```

#### Input

```
1
-7
```

#### Output

```
-7
```

### Notes

In the first example the list 1→2→3→4→5 becomes 5→4→3→2→1.

In the second example the playlist holds a single song, so reversing it changes nothing.