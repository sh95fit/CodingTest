def solution(array, commands):
    num = []
    answer = []
    for i in range(len(commands)) :
        num.append(array[(commands[i][0]-1) : (commands[i][1])])
        num[i].sort()
        answer.append(num[i][commands[i][2]-1])
    return answer