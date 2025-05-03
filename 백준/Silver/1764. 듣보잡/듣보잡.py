import sys

input = sys.stdin.readline

n, m = map(int, input().split())

heard = set(input().strip() for _ in range(n))
seen = set(input().strip() for _ in range(m))

intersection = sorted(heard & seen)

print(len(intersection))
print("\n".join(intersection))
