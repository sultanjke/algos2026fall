n = int(input())

factors = []
divisor = 2

while divisor * divisor <= n:
    while n % divisor == 0:
        factors.append(divisor)
        n = n // divisor
    divisor = divisor + 1

if n > 1:
    factors.append(n)

print(*factors)
