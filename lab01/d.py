n = int(input())

count = 0
number = 1

while count < n:
    number = number + 1
    is_prime = True
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor = divisor + 1

    if is_prime:
        count = count + 1

print(number)
