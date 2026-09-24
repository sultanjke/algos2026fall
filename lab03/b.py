def count_less(numbers, target):
    left = 0
    right = len(numbers)

    while left < right:
        middle = (left + right) // 2
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle

    return left


n, q = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
answers = []

for query in range(q):
    l1, r1, l2, r2 = map(int, input().split())

    if r1 < l2 or r2 < l1:
        first = count_less(numbers, r1 + 1) - count_less(numbers, l1)
        second = count_less(numbers, r2 + 1) - count_less(numbers, l2)
        answer = first + second
    else:
        start = min(l1, l2)
        end = max(r1, r2)
        answer = count_less(numbers, end + 1) - count_less(numbers, start)

    answers.append(str(answer))

print("\n".join(answers))
