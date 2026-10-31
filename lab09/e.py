def shortest_length(text, copies):
    prefix = [0] * len(text)

    for index in range(1, len(text)):
        matched = prefix[index - 1]
        while matched > 0 and text[index] != text[matched]:
            matched = prefix[matched - 1]
        if text[index] == text[matched]:
            matched += 1
        prefix[index] = matched

    period = len(text) - prefix[-1]
    return len(text) + (copies - 1) * period


input = open(0).readline
t = int(input())
answers = []

for test in range(t):
    text, copies = input().split()
    answers.append(str(shortest_length(text, int(copies))))

print("\n".join(answers))
