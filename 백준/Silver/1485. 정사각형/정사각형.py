def distance_squared(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def is_square(points):
    distances = []
    for i in range(4):
        for j in range(i + 1, 4):
            distances.append(distance_squared(points[i][0], points[i][1], points[j][0], points[j][1]))

    distances.sort()

    if distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]:
        return 1
    return 0

T = int(input())

for _ in range(T):
    points = []
    for _ in range(4):
        x, y = map(int, input().split())
        points.append((x, y))

    print(is_square(points))
