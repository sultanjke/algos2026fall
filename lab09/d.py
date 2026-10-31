def overlap(previous, city):
    text = city.lower() + "#" + previous
    prefix = [0] * len(text)

    for index in range(1, len(text)):
        matched = prefix[index - 1]
        while matched > 0 and text[index] != text[matched]:
            matched = prefix[matched - 1]
        if text[index] == text[matched]:
            matched += 1
        prefix[index] = matched

    return prefix[-1]


input = open(0).readline
previous = input().strip().lower()
n = int(input())
best = 1
answers = []

for city_number in range(n):
    city = input().strip()
    length = overlap(previous, city)
    if length > best:
        best = length
        answers = [city]
    elif length == best:
        answers.append(city)

print(len(answers))
print("\n".join(answers))
