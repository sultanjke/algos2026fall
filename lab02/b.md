### Problem B: Kuanyshbek

Kuanyshbek has been studying how multithreading works in operating systems. He wrote a program that starts a single thread which writes to a single file. Being careless, he actually launched **two** threads with different parameters writing into the same file. The OS lets only one thread write at a time, so the two threads took turns: the first record came from thread one, the second from thread two, the third from thread one again, and so on.

Kuanyshbek only needs the data of the first thread. Help him throw away everything the second thread wrote — that is, every element standing at an even position, counting from 1.

**Solve this problem with a linked list:** build the list, then delete every second node.

### Input format

The first line contains one integer N — how many records ended up in the file (1≤N≤99).

The second line contains N integers separated by single spaces — the records in the order they were written (1≤ai≤106).

### Output format

Print the values that are left in the list after every second one has been deleted, separated by single spaces — that is, the records at positions 1,3,5,…

### Examples

#### Input

```
5
1 2 3 4 5
```

#### Output

```
1 3 5
```

### Notes

In the example the records at positions 2 and 4 — the values 2 and 4 — came from the second thread and are deleted. The values 1, 3 and 5 are left.