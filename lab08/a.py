def digit_hash(text):
    result = 0
    power = 1
    modulo = 1000000007

    for digit in text:
        result = (result + (ord(digit) - 47) * power) % modulo
        power = power * 11 % modulo

    return result


def find_strings(values, count):
    present = set(values)
    answers = []

    for text in values:
        target = str(digit_hash(text))
        if target in present:
            answers.append(f'Hash of string "{text}" is {target}')
            if len(answers) == count:
                break

    return answers


input = open(0).readline
n = int(input())
values = []

for index in range(2 * n):
    values.append(input().strip())

print("\n".join(find_strings(values, n)))
