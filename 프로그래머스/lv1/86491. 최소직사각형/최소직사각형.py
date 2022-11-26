def solution(sizes):
    column = 0
    for i in range(len(sizes)) :
        if sizes[i][0] < sizes[i][1] :
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if column < sizes[i][1] :
            column = sizes[i][1]
    row = (max(sizes))[0]
    
    return(row*column)