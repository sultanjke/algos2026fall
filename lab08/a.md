## Submit a solution for A-109670. Hash of digits

|  |  |
| --- | --- |
| **Time limit:** | 1500 ms |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem A: 109670. Hash of digits

You have N strings si consisting of digits and hashes hi of these strings, where hash of string si equal to hi. But one day You noticed that hashes and strings were mixed. You need to determine which of the numbers are hashes and which are strings consisting of digits. Also map each string to its hash. Hash should be calculated by formula below. All operations must be performed modulo 1e9+7: h\=(∑i\=0|s|−1(si−47)×11i)mod(109+7)

### Input format

Given the number N - number of strings (1≤N≤104). Following 2⋅N lines consist from strings and hashes. The length of each string does not exceed 100. It is guaranteed that for each string there is a corresponding hash.

### Output format

In each line print string with corresponding hash like in example below in order their input.

### Examples

#### Input

```
3
334368200
111
100000
266
123456789
93085
```

#### Output

```
Hash of string "111" is 266
Hash of string "123456789" is 334368200
Hash of string "93085" is 100000
```

#### Input

```
3
13903
3383080447314675044643313
9839
813695185
425675346
3461762860035486
```

#### Output

```
Hash of string "3383080447314675044643313" is 425675346
Hash of string "9839" is 13903
Hash of string "3461762860035486" is 813695185
```

### Notes

In first example, hash of string "111" was calculated as follows:

h\=((((49−47)×110)mod(1e9+7)+((49−47)×111)mod(1e9+7))mod(1e9+7)+ +((49−47)×112)mod(1e9+7))mod(1e9+7)\=2+22+242\=266

Note, that the resulting number should be positive.

[View solution](https://github.com/sultanjke/algos2026fall/blob/main/lab08/a.py)
