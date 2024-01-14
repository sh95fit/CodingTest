def solution(arr, flag):
    answer = []
    for n,i in enumerate(flag) :
        if i :
            for i in range(arr[n]*2) :
                answer.append(arr[n])
        else :
            for i in range(arr[n]):
                answer.pop()
    return answer