n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))
first_index = 0
second_index = 0
answer = []

while first_index < n and second_index < m:
    if first[first_index] <= second[second_index]:
        answer.append(str(first[first_index]))
        first_index += 1
    else:
        answer.append(str(second[second_index]))
        second_index += 1

while first_index < n:
    answer.append(str(first[first_index]))
    first_index += 1

while second_index < m:
    answer.append(str(second[second_index]))
    second_index += 1

print(" ".join(answer))
