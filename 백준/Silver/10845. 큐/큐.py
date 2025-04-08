from collections import deque
import sys

input = sys.stdin.read
commands = input().splitlines()

n = int(commands[0])
queue = deque()

for i in range(1, n + 1):
    cmd = commands[i]

    if cmd.startswith("push"):
        _, num = cmd.split()
        queue.append(int(num))

    elif cmd == "pop":
        print(queue.popleft() if queue else -1)

    elif cmd == "size":
        print(len(queue))

    elif cmd == "empty":
        print(0 if queue else 1)

    elif cmd == "front":
        print(queue[0] if queue else -1)

    elif cmd == "back":
        print(queue[-1] if queue else -1)

