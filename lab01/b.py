a, n, m = map(int, input().split())

result = 1 % m
a = a % m

while n > 0:
    if n % 2 == 1:
        result = result * a % m
    a = a * a % m
    n = n // 2

print(result)
