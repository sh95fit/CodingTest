nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

difference = A - B

if len(difference) == 0:
    print(0)

else:
    print(len(difference))
    print(' '.join(map(str, sorted(difference))))

