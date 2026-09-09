a, b = map(int, input().split())

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print(a)
