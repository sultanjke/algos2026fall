def smallest_period(text):
    prefix = [0] * len(text)

    for index in range(1, len(text)):
        matched = prefix[index - 1]
        while matched > 0 and text[index] != text[matched]:
            matched = prefix[matched - 1]
        if text[index] == text[matched]:
            matched += 1
        prefix[index] = matched

    return len(text) - prefix[-1]


text = input().strip()
print(smallest_period(text))
