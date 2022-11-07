def solution(s):
    a = list(s)
    if len(s)%2 == 0 :
        answer = a[int(len(s)/2)-1 : int(len(s)/2)+1]
    else : 
        answer = a[int(len(s)/2)]
    answer = ''.join(answer)
    return answer