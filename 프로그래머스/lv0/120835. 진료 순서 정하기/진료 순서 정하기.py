def solution(emergency):
    answer = [0 for i in range(len(emergency))]
    k = sorted(emergency, reverse = True)
    for i, j in enumerate(k) :
        answer[emergency.index(j)] = int(str(emergency[emergency.index(j)]).replace(str(j), str(i+1)))
    return answer