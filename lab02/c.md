### Problem C: Database

The KBTU database has crashed and the list of all students came back damaged: some names got duplicated. The way the crash worked, all copies of the same name always ended up in **consecutive** positions. For instance, the name “Dana” may occupy positions 2,3,4, but it can never occupy positions 2,3,5, because those are not consecutive.

Help the teachers get rid of the duplicates: keep only the first record of every group of equal neighbours, without changing the order of the list.

### Input format

The first line contains one integer N — the number of records (1≤N≤105).

Each of the next N lines contains one name: a non-empty string of at most 20 Latin letters. Both uppercase and lowercase letters may occur, and they are considered different: “Aa” and “aA” are two different names.

All records of the same name are guaranteed to occupy consecutive positions.

### Output format

On the first line print one integer — how many students are left after the duplicates are removed.

Then print those names, one per line, **in the same order in which they appear in the input**.

### Examples

#### Input

```
5
Alice
Dana
Dana
Dana
Bob
```

#### Output

```
3
Alice
Dana
Bob
```

#### Input

```
2
wow
kek
```

#### Output

```
2
wow
kek
```

#### Input

```
3
kek
wow
wow
```

#### Output

```
2
kek
wow
```

### Notes

In the first example “Dana” occupies positions 2,3,4, so two of the three records are dropped and three students remain: Alice, Dana and Bob — in exactly that order.

In the second example there is nothing to remove.

In the third example the two copies of “wow” stand next to each other, so one of them is dropped.