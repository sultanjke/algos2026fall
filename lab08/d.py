n = int(input())
hashes = list(map(int, input().split()))
previous = 0
power = 1
answer = []

for value in hashes:
    letter = (value - previous) // power
    answer.append(chr(97 + letter))
    previous = value
    power *= 2

print("".join(answer))
