n = int(input())
powers = list(map(int, input().split()))
powers.sort()

prefix = [0]
for power in powers:
    prefix.append(prefix[-1] + power)

p = int(input())
answers = []

for round_number in range(p):
    power = int(input())
    left = 0
    right = n

    while left < right:
        middle = (left + right) // 2
        if powers[middle] <= power:
            left = middle + 1
        else:
            right = middle

    answers.append(f"{left} {prefix[left]}")

print("\n".join(answers))
