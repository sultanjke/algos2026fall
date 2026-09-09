s1 = input()
s2 = input()

first = []
second = []

for letter in s1:
    if letter == "#":
        if first:
            first.pop()
    else:
        first.append(letter)

for letter in s2:
    if letter == "#":
        if second:
            second.pop()
    else:
        second.append(letter)

if first == second:
    print("Yes")
else:
    print("No")
