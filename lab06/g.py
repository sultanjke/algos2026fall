def quick_sort(values):
    stack = [(0, len(values) - 1)]

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        pivot = values[(left + right) // 2]
        first = left
        second = right

        while first <= second:
            while values[first] < pivot:
                first += 1
            while values[second] > pivot:
                second -= 1
            if first <= second:
                values[first], values[second] = values[second], values[first]
                first += 1
                second -= 1

        if left < second:
            stack.append((left, second))
        if first < right:
            stack.append((first, right))


n = int(input())
originals = {}

for request in range(n):
    old, new = input().split()

    if old in originals:
        original = originals.pop(old)
    else:
        original = old

    originals[new] = original

users = []
for current, original in originals.items():
    users.append((original, current))

quick_sort(users)
print(len(users))

for original, current in users:
    print(original, current)
