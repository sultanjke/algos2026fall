## Submit a solution for B-Plagiarism

|  |  |
| --- | --- |
| **Time limit:** | 1 s |
| **Real time limit:** | 5 s |
| **Memory limit:** | 256M |

### Problem B: Plagiarism

Alimzhan wanted to check his students for cheating and he added the parasite word to his exam. He believes that students cheat if the parasite word occurs in the same place in two different results of two students. Alimzhan heard that two of his most beloved students were copied from each other. Help Alimzhan know how many times the parasite word is repeated in the same position in his beloved students’ results.

### Input format

The first line contains string s1 (1≤|s1|≤4⋅105), consisting of lowercase Latin letters — the result of the first student.

The second line contains string s2 (1≤|s2|≤4⋅105), consisting of lowercase Latin letters — the result of the second student.

The third line contains string t (1≤|t|≤4⋅105), consisting of lowercase Latin letters — the parasite word.

### Output format

Print one integer — the number of positions i such that the parasite word t occurs in s1 starting at position i and occurs in s2 starting at the same position i.

### Examples

#### Input

```
kbtuutbkkbtu
utbkkbtukbtu
kbtu
```

#### Output

```
1
```

#### Input

```
aaaaa
aaaaa
a
```

#### Output

```
5
```

#### Input

```
abracadabra
abacabaabac
ab
```

#### Output

```
2
```

### Notes

The strings are long, so comparing t with every position directly is too slow. Compute the hashes of all substrings of the needed length with the Rabin–Karp technique (prefix hashes and one precomputed power table) and compare hashes instead of strings.

A single hash can collide on adversarial data; a pair of hashes with two different moduli is the usual remedy.
