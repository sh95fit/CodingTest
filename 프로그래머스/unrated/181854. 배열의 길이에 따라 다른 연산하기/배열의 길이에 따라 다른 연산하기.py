def solution(arr, n):
    answer = []
    for i, a in enumerate(arr) :
        if len(arr)%2 != 0 and i%2==0 :
            answer.append(a+n)
        elif len(arr)%2 == 0 and i%2!=0 :
            answer.append(a+n)
        else :
            answer.append(a)
    return answer