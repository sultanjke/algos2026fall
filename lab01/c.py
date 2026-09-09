a = int(input())

is_prime = a > 1
divisor = 2

while divisor * divisor <= a:
    if a % divisor == 0:
        is_prime = False
        break
    divisor = divisor + 1

if is_prime:
    print("YES")
else:
    print("NO")
