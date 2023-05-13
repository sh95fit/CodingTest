def solution(intStrs, k, s, l):
    answer = []
    boo = list(map((lambda x : int(x[s:s+l]) > k), intStrs)) 
    # list(map((lambda x : int(x[s:s+l]) if int(x[s:s+l]) > k), intStrs))
    for i, c in enumerate(boo) :
        if c :
            answer.append(int(intStrs[i][s:s+l]))
    return answer