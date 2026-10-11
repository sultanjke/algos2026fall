text = input().strip()
counts = [0] * 26

for letter in text:
    counts[ord(letter) - ord("a")] += 1

answer = []
for index in range(26):
    letter = chr(ord("a") + index)
    answer.append(letter * counts[index])

print("".join(answer))
