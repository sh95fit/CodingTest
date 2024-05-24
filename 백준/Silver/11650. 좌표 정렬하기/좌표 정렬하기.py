N = int(input())

points = []

for i in range(1, N + 1):

    x, y = map(int, input().split())

    points.append((x, y))

points.sort(key=lambda point: (point[0], point[1]))

for point in points:

    print(point[0], point[1])

