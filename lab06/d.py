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
dates = []

for date_number in range(n):
    day, month, year = map(int, input().split("-"))
    dates.append((year, month, day))

quick_sort(dates)
answer = []

for year, month, day in dates:
    answer.append(f"{day:02d}-{month:02d}-{year:04d}")

print("\n".join(answer))
