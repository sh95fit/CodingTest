import sys

input = sys.stdin.readline

def sieve(limit: int) -> list[int]:

    """limit 이하 소수 리스트 리턴"""

    is_prime = [True] * (limit + 1)

    is_prime[0:2] = [False, False]

    for num in range(2, int(limit ** 0.5) + 1):

        if is_prime[num]:

            step = num * num

            is_prime[step:limit + 1:num] = [False] * len(range(step, limit + 1, num))

    return [i for i, prime in enumerate(is_prime) if prime]

def consecutive_prime_sum_count(N: int) -> int:

    primes = sieve(N)

    l = r = 0

    curr = 0

    cnt = 0

    while True:

        if curr >= N:

            if curr == N:

                cnt += 1

            curr -= primes[l]

            l += 1

        else:

            if r == len(primes):

                break

            curr += primes[r]

            r += 1

    return cnt

if __name__ == "__main__":

    N = int(input().strip())

    print(consecutive_prime_sum_count(N))