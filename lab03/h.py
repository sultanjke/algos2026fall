n, k = map(int, input().split())
numbers = list(map(int, input().split()))

left = 0
total = 0
answer = n

for right in range(n):
    total = total + numbers[right]

    while left <= right and total >= k:
        length = right - left + 1
        if length < answer:
            answer = length

        total = total - numbers[left]
        left = left + 1

    if answer == 1:
        break

print(answer)
