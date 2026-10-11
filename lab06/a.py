n = int(input())
text = input().strip()
counts = [0] * 26

for letter in text:
    counts[ord(letter) - ord("a")] += 1

alphabet = "aeioubcdfghjklmnpqrstvwxyz"
answer = []

for letter in alphabet:
    answer.append(letter * counts[ord(letter) - ord("a")])

print("".join(answer))
