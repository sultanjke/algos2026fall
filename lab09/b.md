## B. Password

Time limit: 1 s · Memory limit: 256 MB

Thomas received a new password from his employee. Since Thomas always checks the information, he asks you to check if the password is correct.

It is known that the password is correct only if it occurs _at least_ K times on a piece of paper that the Bank Director gave to Thomas.

Input

The first line contains a string s and an integer K (3⩽|s|⩽105, 1⩽K⩽105), where s is a new password. The second line contains a string T (3⩽|T|⩽105), a string on a piece of paper.

Output

Print `YES` if password is correct, otherwise print `NO`

Examples

**Input 1**

```
hello 2
helloThomashelloArthurhelloJohnhello
```

**Output 1**

```
YES
```

**Input 2**

```
kbtu 4
kbtuIsTheBestPlaceInTheWorld
```

**Output 2**

```
NO
```