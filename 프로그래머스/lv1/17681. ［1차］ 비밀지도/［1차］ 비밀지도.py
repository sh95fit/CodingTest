def solution(n, arr1, arr2):
    answer = []
#    arr1 = list(map(bin, arr1))
#    arr2 = list(map(bin, arr2))
    for i in range(n) :
        answer.append(bin(int(arr1[i]) | int(arr2[i])))
        answer[i] = answer[i].replace("0b","")
        if len(answer[i]) != n :
            answer[i] = answer[i].zfill(n)
        answer[i] = answer[i].replace("1","#")
        answer[i] = answer[i].replace("0"," ")
    return answer

    