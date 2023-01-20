def solution(num_list, n):
    k = len(num_list)//n
    answer = []
    for i in range(k) :
        answer.append(num_list[0:n])
        del num_list[0:n]
    return answer