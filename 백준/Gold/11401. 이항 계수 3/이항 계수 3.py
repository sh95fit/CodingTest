MOD = 1_000_000_007
MAX = 4_000_000

factorial = [1] * (MAX + 1)
inv_factorial = [1] * (MAX + 1)

for i in range(1, MAX + 1):
    factorial[i] = factorial[i - 1] * i % MOD

inv_factorial[MAX] = pow(factorial[MAX], MOD - 2, MOD)
for i in range(MAX - 1, -1, -1):
    inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

def binomial_coefficient(n, k):
    if k < 0 or k > n:
        return 0
    return factorial[n] * inv_factorial[k] % MOD * inv_factorial[n - k] % MOD

n, k = map(int, input().split())
print(binomial_coefficient(n, k))
