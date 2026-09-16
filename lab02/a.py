from collections import deque

t = int(input())

for test in range(t):
    n = int(input())
    letters = input().split()
    counts = {}
    queue = deque()
    answers = []

    for letter in letters:
        if letter not in counts:
            counts[letter] = 0
            queue.append(letter)
        counts[letter] = counts[letter] + 1

        while queue and counts[queue[0]] > 1:
            queue.popleft()

        if queue:
            answers.append(queue[0])
        else:
            answers.append("-1")

    print(*answers)
