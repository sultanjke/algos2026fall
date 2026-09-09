### Problem J: 195823. Zoro and Seven Sword Style.

**THE CODE TEMPLATE IS IN THE NOTE BELOW.**

Zoro got lost again, this time in the maze. Walking along a random corridor, he stumbles upon a mysterious door, which says that this is the exit from the maze. The door mechanism works on specific functions for the linked list. But due to the fact that the door is very old, the functions have been erased. Zoro discovered an ancient stone paneglyph nearby, which lists about each function:

1.  inserts — add a node on position p.

2.  remove — remove the node from position p.

3.  print — print all values of list separated by a space.

4.  replace — move the node from position p1 and to position p2. Position p2 is considered at the moment after its removal.

5.  reverse — reverse the entire list.

6.  cyclic\_left — do a cyclic shift to the left x times.

7.  cyclic\_right — do a cyclic shift to the right x times.

Also, there are indicated the commands that need to be executed in order for the door to open. It is known that each command calls a specific function. Help Zoro to restore functions.

### Input format

Each line of input starts with integer which indicates command:

-   If command 0, exit the program.

-   If command 1, then the same line of input contains numbers x (0≤x≤106) and p (0≤p). Add a new node with value x to the position p. It is guaranteed that p does not exceed the length of the list.

-   If command 2, then the same line of input contains number p (0≤p). Delete the node from position p. It is guaranteed that p is less than the length of the list.

-   If command 3, print the whole list. Print -1 if list is empty.

-   If command 4, then the same line of input contains numbers p1 and p2 (0≤p1,p2). Move node from position p1 to position p2. Position p2 is counted from the moment when we have already retrieved the node from position p1. It is guaranteed that p1 and p2 are less than the length of the list.

-   if command 5, reverse whole list.

-   If command 6, then the same line of input contains number x. Make left cyclic shift x (0≤x) times. It is guaranteed that x is less than the length of the list.

-   If command 7, then the same line of input contains number x. Make right cyclic shift x (0≤x) times. It is guaranteed that x is less than the length of the list.

**Subtasks**

1.  (20%) Implement each function in O(N2) or faster.

2.  (20%) Implement functions inserts, remove, print and replace in O(N).

3.  (20%) Implement functions inserts, remove, print and reverse in O(N).

4.  (20%) Implement functions inserts, remove, print, cyclic\_left and cyclic\_right in O(N).

5.  (20%) Implement all of the functions in O(N).

### Output format

For each `print` command, print all values of the list separated by single spaces.

**Note**

Each function except `print` must return the head of the linked list.

The statement above fully describes the input and output format, so you can write the whole program yourself. If you prefer to start from a ready-made template with the reading loop already written, take the one for your language:

C++ : [https://pastebin.com/BAG1n8Kp](https://pastebin.com/BAG1n8Kp)

Python : [https://pastebin.com/9mwkZnEh](https://pastebin.com/9mwkZnEh)

Java : [https://pastebin.com/jfhpYWYR](https://pastebin.com/jfhpYWYR)

_Just leave it to luck_

— Roronoa Zoro, _One Piece_

### Examples

#### Input

```
1 0 0
3
1 1 0
3
1 2 2
3
4 0 0
3
4 0 1
3
1 3 2
3
4 2 0
3
4 3 1
3
4 2 3
3
0
```

#### Output

```
0
1 0
1 0 2
1 0 2
0 1 2
0 1 3 2
3 0 1 2
3 2 0 1
3 2 1 0
```

#### Input

```
1 0 0
1 1 1
1 2 2
1 3 3
3
5
3
1 4 0
5
3
0
```

#### Output

```
0 1 2 3
3 2 1 0
0 1 2 3 4
```

#### Input

```
1 0 0
1 1 1
1 2 2
1 3 3
3
7 0
3
7 1
3
6 1
3
6 2
3
1 4 2
3
6 4
3
7 3
3
0
```

#### Output

```
0 1 2 3
0 1 2 3
3 0 1 2
0 1 2 3
2 3 0 1
2 3 4 0 1
1 2 3 4 0
3 4 0 1 2
```