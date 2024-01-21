def solution(arr):
    answer = arr
    n = len(arr)
    if (n&(n-1)) == 0 :
        return answer
    else :
        while (n&(n-1)) != 0 :
            answer.append(0)
            n+=1
    return answer