import sys

def build_sa(s):

    n = len(s)

    k = 1

    sa = list(range(n))

    rank = [ord(c) for c in s]

    tmp = [0] * n

    while True:

        sa.sort(key=lambda x: (rank[x], rank[x+k] if x+k < n else -1))

        tmp[sa[0]] = 0

        for i in range(1, n):

            left = (rank[sa[i-1]], rank[sa[i-1]+k] if sa[i-1]+k < n else -1)

            right = (rank[sa[i]], rank[sa[i]+k] if sa[i]+k < n else -1)

            tmp[sa[i]] = tmp[sa[i-1]] + (left < right)

        rank, tmp = tmp, rank

        if rank[sa[-1]] == n-1:

            break

        k <<= 1

    return sa

def build_lcp(s, sa):

    n = len(s)

    rank = [0]*n

    for i in range(n):

        rank[sa[i]] = i

    h = 0

    lcp = [0]*(n-1)

    for i in range(n):

        if rank[i] == 0:

            continue

        j = sa[rank[i]-1]

        while i+h < n and j+h < n and s[i+h] == s[j+h]:

            h += 1

        lcp[rank[i]-1] = h

        if h > 0:

            h -= 1

    return lcp

def main():

    s = sys.stdin.readline().strip()

    n = len(s)

    sa = build_sa(s)

    lcp = build_lcp(s, sa)

    total = n*(n+1)//2

    ans = total - sum(lcp)

    print(ans)

if __name__ == "__main__":

    main()