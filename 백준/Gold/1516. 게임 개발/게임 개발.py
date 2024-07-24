from collections import deque

def minimum_build_times(n, build_info):
    time = [0] * (n + 1)
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        info = build_info[i - 1]
        time[i] = info[0]

        for prereq in info[1:-1]:
            graph[prereq].append(i)
            indegree[i] += 1

    queue = deque()
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            result[i] = time[i]

    while queue:
        current = queue.popleft()

        for next_building in graph[current]:
            indegree[next_building] -= 1
            result[next_building] = max(result[next_building], result[current] + time[next_building])

            if indegree[next_building] == 0:
                queue.append(next_building)

    return result[1:]

n = int(input().strip())
build_info = []

for _ in range(n):
    build_info.append(list(map(int, input().strip().split())))

build_times = minimum_build_times(n, build_info)

for time in build_times:
    print(time)

