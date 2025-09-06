def largest_rectangle(hist):

    stack = []

    max_area = 0

    hist.append(0)  # 마지막에 0을 추가해 스택을 모두 비우게 함

    for i, h in enumerate(hist):

        while stack and hist[stack[-1]] > h:

            height = hist[stack.pop()]

            width = i if not stack else i - stack[-1] - 1

            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area

# 입력 처리

N = int(input())

hist = [int(input()) for _ in range(N)]

print(largest_rectangle(hist))