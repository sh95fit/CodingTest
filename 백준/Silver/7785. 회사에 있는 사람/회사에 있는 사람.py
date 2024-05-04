n = int(input())

log = {}

for _ in range(n):

    name, action = input().split()

    log[name] = action

# 마지막 상태가 "enter"인 사람들을 출력

for name, action in sorted(log.items(), reverse=True):

    if action == "enter":

        print(name)

