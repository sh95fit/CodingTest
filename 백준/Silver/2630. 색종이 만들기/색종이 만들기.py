def count_paper(paper, x, y, size):   
    if size == 1:
        if paper[x][y] == 0:
            return (1, 0)  
        else:
            return (0, 1)      
   
    first_color = paper[x][y]
    all_same = True
   
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first_color:
                all_same = False
                break

        if not all_same:
            break
       
    if all_same:
        if first_color == 0:
            return (1, 0)  
        else:
            return (0, 1)  
       
    mid = size // 2
    white_count = 0
    blue_count = 0
   
    for dx in [0, mid]:
        for dy in [0, mid]:
            w, b = count_paper(paper, x + dx, y + dy, mid)
            white_count += w
            blue_count += b
    
    return (white_count, blue_count)

N = int(input())  
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = count_paper(paper, 0, 0, N)

print(white)
print(blue)

