M = int(input())

N = int(input())

prime_numbers = []

for num in range(M, N + 1):

    if num < 2:

        continue

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:

            is_prime = False

            break

    if is_prime:

        prime_numbers.append(num)

if prime_numbers:

    print(sum(prime_numbers))

    print(min(prime_numbers))

else:

    print(-1)

