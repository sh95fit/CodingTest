import sys

input = sys.stdin.read

def next_greater_element():
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))

    result = [-1] * N
    stack = []

    for i in range(N):
        while stack and A[stack[-1]] < A[i]:
            idx = stack.pop()
            result[idx] = A[i]

        stack.append(i)

    print(' '.join(map(str, result)))

next_greater_element()