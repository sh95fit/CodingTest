def solution(a, d, included):
    answer = 0
    res = a
    for i in range(len(included)):
        if included[i] :
            answer += res
            res += d
        else :
            res += d
    return answer