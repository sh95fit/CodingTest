def largest_rectangle(hist):
    stack = []
    max_area = 0

    hist.append(0)  
    
    for i, h in enumerate(hist):
        while stack and hist[stack[-1]] > h:
            height = hist[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    hist.pop()

    return max_area

while True:
    line = input()

    if line == "0 0":
        break

    N, M = map(int, line.split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    height = [0] * M
    max_area = 0

    for row in matrix:
        for j in range(M):
            if row[j] == 1:
                height[j] += 1

            else:
                height[j] = 0

        max_area = max(max_area, largest_rectangle(height))

    print(max_area)