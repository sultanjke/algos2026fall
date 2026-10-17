n = int(input())
numbers = list(map(int, input().split()))
answer = [0] * n
left = 0
right = n - 1

for position in range(n - 1, -1, -1):
    left_square = numbers[left] * numbers[left]
    right_square = numbers[right] * numbers[right]

    if left_square > right_square:
        answer[position] = left_square
        left += 1
    else:
        answer[position] = right_square
        right -= 1

print(" ".join(map(str, answer)))
