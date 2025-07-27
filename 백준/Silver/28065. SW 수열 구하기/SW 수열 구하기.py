N = int(input())

ans = []
left = 1
right = N
turn = 0  

while left <= right:
    if turn % 2 == 0:
        ans.append(left)
        left += 1
    else:
        ans.append(right)
        right -= 1

    turn += 1

print(*ans)