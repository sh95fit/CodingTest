import sys, math

A, B = map(int, sys.stdin.readline().split())
max_p = int(math.isqrt(B))

is_prime = [True]*(max_p+1)
is_prime[0]=is_prime[1]=False

for i in range(2, int(max_p**0.5)+1):
    if is_prime[i]:
        is_prime[i*i:max_p+1:i] = [False]*(((max_p - i*i)//i)+1)

primes = [i for i, v in enumerate(is_prime) if v]
ans = 0

for p in primes:
    x = p*p  

    while x <= B:
        if x >= A:
            ans += 1

        x *= p

print(ans)