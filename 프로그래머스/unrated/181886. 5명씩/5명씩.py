def solution(names):
    answer = []
    for i, n in enumerate(names) :
        if i%5 == 0 :
            answer.append(n)
    return answer