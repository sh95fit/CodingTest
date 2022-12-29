def solution(t, p):
    answer = 0
    for i in range(len(t)+1-len(p)) :
        if int(p) >= int(t[i:i+len(p)]) :
            answer += 1
    return answer