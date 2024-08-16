def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for i in range(start*start, limit + 1, start):
                sieve[i] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]

def is_appropriate_key(s, primes):
    for prime in primes:
        if s % prime == 0:
            return False

        if prime * prime > s:
            break

    return True

def main():
    n = int(input())
    primes = generate_primes(10**6)

    for _ in range(n):
        s = int(input())

        if is_appropriate_key(s, primes):
            print("YES")

        else:
            print("NO")

main()

