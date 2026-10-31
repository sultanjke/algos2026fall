def correct_password(pattern, text, required):
    prefix = [0] * len(pattern)
    matched = 0

    for index in range(1, len(pattern)):
        while matched > 0 and pattern[index] != pattern[matched]:
            matched = prefix[matched - 1]
        if pattern[index] == pattern[matched]:
            matched += 1
        prefix[index] = matched

    matched = 0
    count = 0
    for letter in text:
        while matched > 0 and letter != pattern[matched]:
            matched = prefix[matched - 1]
        if letter == pattern[matched]:
            matched += 1
        if matched == len(pattern):
            count += 1
            if count >= required:
                return True
            matched = prefix[matched - 1]

    return False


pattern, required = input().split()
text = input().strip()
if correct_password(pattern, text, int(required)):
    print("YES")
else:
    print("NO")
