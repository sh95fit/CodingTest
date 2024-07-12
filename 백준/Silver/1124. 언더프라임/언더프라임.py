def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    p = 3

    while p * p <= n:
        if n % p == 0:
            return False

        p += 2

    return True

def count_prime_factors(n):
    count = 0
    
    while n % 2 == 0:
        count += 1
        n //= 2

    p = 3

    while p * p <= n:
        while n % p == 0:
            count += 1
            n //= p

        p += 2

    if n > 2:
        count += 1

    return count

def is_underprime(n):
    num_factors = count_prime_factors(n)

    return is_prime(num_factors)

def count_underprimes(A, B):
    count = 0

    for i in range(A, B + 1):
        if is_underprime(i):
            count += 1

    return count

A, B = map(int, input().split())

print(count_underprimes(A, B))

