import re

pattern = re.compile(r"(100+1+|01)+")

T = int(input())
results = []

for _ in range(T):
    signal = input().strip()

    if pattern.fullmatch(signal):
        results.append("YES")

    else:
        results.append("NO")

for result in results:
    print(result)

