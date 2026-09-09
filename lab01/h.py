n = int(input())
ages = list(map(int, input().split()))

stack = []
answers = []

for age in ages:
    while stack and stack[-1] >= age:
        stack.pop()

    if stack:
        answers.append(stack[-1])
    else:
        answers.append(-1)

    stack.append(age)

print(*answers)
