def solution(array, n):
    list_n = []
    array.sort()
    for i in array:
        list_n.append(abs(n-i))
    answer = [array[list_n.index(min(list_n))]]
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]