import sys
input = sys.stdin.readline

def z_algorithm(s):
    n = len(s)
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z

s = input().strip()
n = len(s)
s_rev = s[::-1]
z = z_algorithm(s_rev)
m = int(input())

for _ in range(m):
    i = int(input())
    print(z[n - i] if i != n else n)