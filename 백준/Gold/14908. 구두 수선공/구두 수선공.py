N = int(input())
tasks = []

for i in range(1, N + 1):
    T, S = map(int, input().split())
    tasks.append((i, T, S))
    
tasks.sort(key=lambda x: (x[1] / x[2], x[0]))

print(' '.join(str(task[0]) for task in tasks))