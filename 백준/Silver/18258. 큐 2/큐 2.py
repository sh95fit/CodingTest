import sys

from collections import deque

input = sys.stdin.readline

N = int(input())

q = deque()

output = []

for _ in range(N):

    cmd = input().split()

    if cmd[0] == "push":

        q.append(cmd[1])

    elif cmd[0] == "pop":

        output.append(q.popleft() if q else "-1")

    elif cmd[0] == "size":

        output.append(str(len(q)))

    elif cmd[0] == "empty":

        output.append("1" if not q else "0")

    elif cmd[0] == "front":

        output.append(q[0] if q else "-1")

    elif cmd[0] == "back":

        output.append(q[-1] if q else "-1")

sys.stdout.write("\n".join(output))