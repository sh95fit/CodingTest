def solution(n):
    answer = []
    
    c = 2
    
    while c != n :
        if n%c == 0 :
            n = n//c
            answer.append(c)
        else :
            c = c+1
    if n > 1 :
        answer.append(n)
    return sorted(list(set(answer)))