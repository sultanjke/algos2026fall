n = int(input())
names = []

for i in range(n):
    name = input()
    if not names or names[-1] != name:
        names.append(name)

print(len(names))
for name in names:
    print(name)
