import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nlist = list(map(int, input().split()))

print(sorted(nlist)[K-1])