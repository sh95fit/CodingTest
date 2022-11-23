def solution(d, budget):
    d.sort()
    cnt = 0
    for i in range(len(d)) :
        if budget-d[i] >=0 :
            budget -= d[i]
            cnt+=1
    return cnt