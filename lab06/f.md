## Submit a solution for F-New GPA

|  |  |
| --- | --- |
| **Time limit:** | 3 s |
| **Real time limit:** | 6 s |
| **Memory limit:** | 256M |

### Problem F: New GPA

KBTU introduces new GPA calculation system. You’re given n students, their marks and number of credits for their subjects. Sort them by total GPA. It is calculated as ∑i\=1mgi∗ci∑i\=1mci, where m - student’s number of subjects, gi,ci - GPA and number of credits for i\-th subject respectively. GPA scale is given in the notes.

### Input format

First line contains one integer n (1≤n≤105). Each of the next n lines contains information about the i\-th student: his lastname, firstname, an integer mi (1≤mi≤10) - number of subjects for this student, then mi marks and number of credits for each subject.

### Output format

You should print sorted list of students. Each student should be printed in the following format: lastname firstname GPA. First, sort them by overall GPA **in ascending order**; if the GPA is equal, sort by lastname, then by firstname. GPA should be printed with three digits after decimal point.

The GPA must be printed exactly as `printf("%.3f", gpa)` prints it in C++ (equivalently, `cout « fixed « setprecision(3) « gpa`). This matters: for many students the GPA falls exactly on the rounding boundary, and other rounding rules give a different answer.

### Examples

#### Input

```
5
Issenbayev Yernur 4 A 4 D+ 2 B 3 A+ 4
Yermekbayeva Diana 3 A+ 4 B+ 3 B 1
Kadyrov Asman 2 A+ 4 A+ 4
Stepanenko Ivan 3 C+ 3 F 1 A+ 5
Bissimbayev Arystan 3 A+ 4 A+ 5 D 1
```

#### Output

```
Stepanenko Ivan 3.056
Issenbayev Yernur 3.308
Yermekbayeva Diana 3.688
Bissimbayev Arystan 3.700
Kadyrov Asman 4.000
```

### Notes

| A+ | 4.00 |
| --- | --- |
| A | 3.75 |
| B+ | 3.50 |
| B | 3.00 |
| C+ | 2.50 |
| C | 2.00 |
| D+ | 1.50 |
| D | 1.00 |
| F | 0 |