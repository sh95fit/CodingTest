def solution(num_list, n):
    answer = []
    for i in range(n, len(num_list)) :
        answer.append(num_list[i])
    answer = answer + num_list[:n]
    return answer