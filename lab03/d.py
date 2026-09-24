input = open(0).readline
n = int(input())
counts = [0] * 1001

for power in map(int, input().split()):
    counts[power] += 1

results = []
count = 0
total = 0

for power in range(1001):
    count += counts[power]
    total += power * counts[power]
    results.append(f"{count} {total}")

p = int(input())
answers = []

for round_number in range(p):
    power = int(input())
    answers.append(results[power])

print("\n".join(answers))
