## D. Modified Towns game

Time limit: 1 s · Memory limit: 256 MB

One day Olzhas was bored and he wanted to play the game `Towns` with friends. But the game has been slightly modified. In this game, each participant in his turn calls another real city of any country, the name of which begins with the maximum possible length of suffix, which ends with the name of the city of the previous participant. It was the turn of Olzhas and he should choose the name of the city. Help him with the choice of the name of the city.

Input

Given string P (1⩽|P|⩽1000) - the name of the city of the previous participant.

In the next line given N (1⩽N⩽103) - the number of city names that Olzhas know.

Next N lines represent name ai (1⩽|ai|⩽1000) of the cities. Each city name starts with an uppercase letter and other letters are lowercase.

Output

The first line should contain integer M - the number of possible names of the cities which could say Olzhas.

Each of the next M lines should consist of the possible names of the cities in the order of their input.

Examples

**Input 1**

```
Kokshetau
5
Astana
Tauemel
Tainan
Almaty
Budapest
```

**Output 1**

```
1
Tauemel
```

**Input 2**

```
Almaty
3
Yacuiba
Yurga
Moscow
```

**Output 2**

```
2
Yacuiba
Yurga
```