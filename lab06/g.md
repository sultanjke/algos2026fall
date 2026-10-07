## Submit a solution for G-Nurbol hacker

|  |  |
| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem G: Nurbol hacker

This is a continuation of the story about the Aslan and Password task from the last quiz. The story is that Nurbol successfully hacked Aslan’s Steam account. Aslan was of course upset, but he doesn’t give up. He decided to restore his Steam account. To do this, he wrote in support of Steam. Aslan gave them the nickname of his account. But it is possible for Nurbol to change the nickname of the account. And now Steam employees must understand what the new nickname is. Employees have logs of changing nicknames, the logs consist of n lines. The line itself consists of two words, the old nickname, and the new one. Help employees to display all original nicknames and new nicknames next to them.

### Input format

The first line is number n (1≤n≤1000) the number of requests to change the nickname. Next n lines consist of two strings, old nickname and new nickname.

Every nickname is a non-empty string of at most 20 Latin letters and digits; nicknames are case-sensitive, and the old nickname always differs from the new one.

It is guaranteed that a nickname belongs to one user forever: once some user has used a nickname, no other user can ever take it.

### Output format

The first line is the number q — the number of users who changed their nicknames.

Each of the next q lines contains two strings: the original nickname of a user and his current nickname. Print these lines **sorted by the original nickname in lexicographical order**.

### Examples

#### Input

```
2
Aslan Nurbol
Nurbol HackMachine
```

#### Output

```
1
Aslan HackMachine
```

#### Input

```
6
Sens3i Danya
S1mple Papa
M9snoyPovar AWPMaster
IAmNoob IAmPro
Papa Sanya
IAmPro IAmNoob
```

#### Output

```
4
IAmNoob IAmNoob
M9snoyPovar AWPMaster
S1mple Sanya
Sens3i Danya
```

### Notes

In the first test nickname "Aslan" was changed to nickname "Nurbol". Then this nickname was changed to "HackMachine". As a result, the original nickname "Aslan" became "HackMachine".