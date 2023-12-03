def solution(myString, pat):
    answer = 0
    for i in range(len(myString)) :
        try :
            if pat == myString[i:len(pat)+i] :
                answer +=1
        except :
            pass
    return answer